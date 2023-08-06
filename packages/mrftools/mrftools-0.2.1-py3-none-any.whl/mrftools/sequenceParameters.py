from __future__ import annotations
import numpy as np
import h5py
from mrftools import types
from matplotlib import pyplot as plt
import torch
import json as json
from mrftools import Units, SequenceUnits
from importlib.metadata import version  
import copy

Timepoint = np.dtype([('TR', np.float32), ('TE', np.float32), ('FA', np.float32), ('PH', np.float32), ('ID', np.int16)])

SequenceModuleClasses = {}
def register(cls):
    SequenceModuleClasses[cls.__name__] = cls
    return cls
    
class SequenceModule:
    def __init__(self, moduleType:types.ModuleType, units=None):
        self.moduleType = moduleType
        if(units != None):
            self.units = units
        else:
            self.units = SequenceUnits(Units.SECONDS, Units.DEGREES)

    def __str__(self):
        return "Module Type: " + self.moduleType.name
    
    @staticmethod
    def FromJson(jsonInput, units):
        moduleClass = SequenceModuleClasses[jsonInput.get("type")]
        module = moduleClass.FromJson(jsonInput)
        module.units = units
        return module


class AcquisitionModule(SequenceModule):
    def __init__(self, acquisitionType:types.AcquisitionType, timepoints=[], units=None):
        SequenceModule.__init__(self, moduleType=types.ModuleType.ACQUISITION, units=units) 
        self.acquisitionType = acquisitionType
        self.timepoints = timepoints 

    def Initialize(self, TRs:list(float), TEs:list(float), FAs:list(float), PHs:list(float), IDs:list(int)):
        self.timepoints = np.empty(len(TRs), dtype=Timepoint)
        if (len(TRs)!=len(TEs)) or (len(TRs)!=len(FAs)) or  (len(TRs)!=len(PHs)) or  (len(TRs)!=len(IDs)):
            print("Sequence Parameter Import Failed: TR/TE/FA/PH/ID files must have identical number of entries")
            return 
        for index in range(len(TRs)):
            self.timepoints[index] = (TRs[index], TEs[index], FAs[index], PHs[index], IDs[index])
        #print("Acquisition Module initialized with " + str(len(self.timepoints)) + " timepoint definitions")
    
    def ConvertUnits(self, targetUnits:SequenceUnits):
        if(self.units != targetUnits):
            scaledTimepoints = np.copy(self.timepoints)
            scaledTimepoints['TR'] = Units.Convert(self.timepoints['TR'], self.units.time, targetUnits.time)
            scaledTimepoints['TE'] = Units.Convert(self.timepoints['TE'], self.units.time, targetUnits.time)
            scaledTimepoints['FA'] = Units.Convert(self.timepoints['FA'], self.units.angle, targetUnits.angle)
            scaledTimepoints['PH'] = Units.Convert(self.timepoints['PH'], self.units.angle, targetUnits.angle)
            self.timepoints = scaledTimepoints
            self.units = targetUnits

    def CastToIntegers(self):
        scaledTimepoints = self.timepoints.astype(np.dtype([('TR', int), ('TE', int), ('FA', int), ('PH', int), ('ID', int)]))
        self.timepoints = scaledTimepoints
    
    def CastToFloats(self):
        scaledTimepoints = self.timepoints.astype(Timepoint)
        self.timepoints = scaledTimepoints

@register
class FISPAcquisitionModule(AcquisitionModule):
    def __init__(self, timepoints=[], dephasingRange=360, units=None):
        AcquisitionModule.__init__(self, acquisitionType=types.AcquisitionType.FISP, timepoints=timepoints, units=units) 
        self.dephasingRange = dephasingRange

    def __str__(self):
        return SequenceModule.__str__(self) + " || Acquisition Type: " + self.acquisitionType.name + " || Dephasing Range (# of pi): " + f'{self.dephasingRange/np.pi:7.5f}' + " || Timepoints: \n" + str(self.timepoints)
    
    def __dict__(self):
        timepointDict = [dict(zip(self.timepoints.dtype.names,x.tolist())) for x in self.timepoints]
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "timepoints": timepointDict,
            "dephasingRange":self.dephasingRange
        }
        return moduleDict

    @staticmethod
    def FromJson(jsonInput):
        dephasingRange = jsonInput.get("dephasingRange")
        timepointsJson = jsonInput.get("timepoints")
        if(dephasingRange != None and timepointsJson != None):
            timepoints = []
            for timepointJson in timepointsJson:
                timepoints.append(tuple(timepointJson.values()))
            timepoints = np.array(timepoints, dtype=Timepoint)         
            return FISPAcquisitionModule(timepoints, dephasingRange)   
        else:
            print("FISPAcquisitionModule requires dephasingRange and timepoints")

    def Simulate(self, dictionaryEntries, numSpins, device=None, inputMx=None, inputMy=None, inputMz=None): 
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")    
        T1s = torch.tensor(dictionaryEntries['T1']).to(device)
        T2s = torch.tensor(dictionaryEntries['T2']).to(device)
        B1s = torch.tensor(dictionaryEntries['B1']).to(device)
        TRs = torch.tensor(self.timepoints['TR'].copy()).to(device)
        TEs = torch.tensor(self.timepoints['TE'].copy()).to(device)
        FAs = torch.tensor(self.timepoints['FA'].copy()).to(device)
        PHs = torch.tensor(self.timepoints['PH'].copy()).to(device)

        numTimepoints = len(self.timepoints); numDictionaryEntries = len(dictionaryEntries)
        phaseValues = np.linspace(-1*self.dephasingRange/2, self.dephasingRange/2, numSpins)

        spinOffresonances = torch.tensor(phaseValues).to(device)
        spinOffresonances = torch.deg2rad(spinOffresonances)
        FAs = torch.deg2rad(FAs)
        PHs = torch.deg2rad(PHs)

        Mx0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        My0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        Mz0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        Time = torch.zeros((numTimepoints))

        Mx = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        My = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        Mz = torch.zeros((numSpins, numDictionaryEntries)).to(device)    


        phaseValueCosines = torch.cos(spinOffresonances)
        phaseValueSines = torch.sin(spinOffresonances)
        
        if(inputMx is not None):
            if(torch.numel(inputMx) == numSpins*numDictionaryEntries and torch.numel(inputMy) == numSpins*numDictionaryEntries and torch.numel(inputMz) == numSpins*numDictionaryEntries):
                Mx = inputMx
                My = inputMy
                Mz = inputMz
            else:
                if(torch.numel(inputMx) == 1 and torch.numel(inputMy) == 1 and torch.numel(inputMz) == 1 ):
                    Mx = torch.ones(numSpins, numDictionaryEntries) * inputMx
                    My = torch.ones(numSpins, numDictionaryEntries) * inputMy
                    Mz = torch.ones(numSpins, numDictionaryEntries) * inputMz
                else: 
                    print("Simulation Failed: Number of input magnetization states doesn't equal number of requested spins to simulate.")
                    return
        Mx = Mx.to(device);  My = My.to(device); Mz = Mz.to(device); 
        with torch.no_grad():
            accumulatedTime = 0
            for iTimepoint in range(numTimepoints):
                fa = FAs[iTimepoint] * B1s
                tr = TRs[iTimepoint]
                te = TEs[iTimepoint]
                ph = PHs[iTimepoint]
                tre = tr-te

                Time[iTimepoint] = accumulatedTime
                accumulatedTime = accumulatedTime + tr

                At2te = torch.exp(-1*te/T2s)
                At1te = torch.exp(-1*te/T1s)
                Bt1te = 1-At1te
                
                At2tr = torch.exp(-1*tre/T2s)
                At1tr = torch.exp(-1*tre/T1s)
                Bt1tr = 1-At1tr

                # M2 = Rphasep*Rflip*Rphasem*M1;       % RF effect  

                # Applying Rphasem = [cos(-iph) -sin(-iph) 0; sin(-iph) cos(-iph) 0; 0 0 1];  
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = torch.multiply(torch.cos(-ph),Mxi) - torch.multiply(torch.sin(-ph), Myi)
                My = torch.multiply(torch.sin(-ph),Mxi) + torch.multiply(torch.cos(-ph), Myi)
                Mz = Mzi

                # Applying flip angle = [1 0 0; 0 cos(randflip(ii)) -sin(randflip(ii)); 0 sin(randflip(ii)) cos(randflip(ii))];
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = Mxi
                My = torch.multiply(torch.cos(fa),Myi)-torch.multiply(torch.sin(fa),Mzi)
                Mz = torch.multiply(torch.sin(fa),Myi)+torch.multiply(torch.cos(fa),Mzi)

                # Applying Rphasep = [cos(iph) -sin(iph) 0; sin(iph) cos(iph) 0; 0 0 1];  
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = torch.multiply(torch.cos(ph),Mxi) - torch.multiply(torch.sin(ph), Myi)
                My = torch.multiply(torch.sin(ph),Mxi) + torch.multiply(torch.cos(ph), Myi)
                Mz = Mzi

                # Relaxation over TE
                Mx = torch.multiply(Mx, At2te)
                My = torch.multiply(My, At2te)
                Mz = torch.multiply(Mz, At1te)+Bt1te

                # Reading value after TE and before TRE 
                Mx0[iTimepoint,:,:]=Mx.cpu()
                My0[iTimepoint,:,:]=My.cpu()
                Mz0[iTimepoint,:,:]=Mz.cpu()

                # Relaxation over TRE (TR-TE) 
                Mx = Mx*At2tr
                My = My*At2tr
                Mz = Mz*At1tr+Bt1tr

                # Applying off-resonance to spins
                Mxi = Mx.t()
                Myi = My.t()
                Mx = (torch.multiply(phaseValueCosines,Mxi) - torch.multiply(phaseValueSines,Myi)).t()
                My = (torch.multiply(phaseValueSines,Mxi) + torch.multiply(phaseValueCosines,Myi)).t()
                del fa, tr, te, tre, At2te, At1te, Bt1te, At2tr, At1tr, Bt1tr, Mxi, Myi, Mzi
        del T1s, T2s, B1s, FAs, PHs, spinOffresonances, Mx, My, Mz
        return Time,Mx0,My0,Mz0 

@register
class TRUEFISPAcquisitionModule(AcquisitionModule):
    def __init__(self, timepoints=[], units=None):
            AcquisitionModule.__init__(self, acquisitionType=types.AcquisitionType.TRUEFISP, timepoints=timepoints, units=units) 

    def __str__(self):
        return SequenceModule.__str__(self) + " || Acquisition Type: " + self.acquisitionType.name + " || Timepoints: \n" + str(self.timepoints)
    
    def __dict__(self):
        timepointDict = [dict(zip(self.timepoints.dtype.names,x.tolist())) for x in self.timepoints]
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "timepoints": timepointDict
        }
        return moduleDict
    
    @staticmethod
    def FromJson(jsonInput):
        timepointsJson = jsonInput.get("timepoints")
        if(timepointsJson != None):
            timepoints = []
            for timepointJson in timepointsJson:
                timepoints.append(tuple(timepointJson.values()))
            timepoints = np.array(timepoints, dtype=Timepoint)         
            return TRUEFISPAcquisitionModule(timepoints) 
        else:
            print("TRUEFISPAcquisitionModule requires timepoints")
    
    def Simulate(self, dictionaryEntries, numSpins, device=None, inputMx=None, inputMy=None, inputMz=None): 
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")    
        T1s = torch.tensor(dictionaryEntries['T1']).to(device)
        T2s = torch.tensor(dictionaryEntries['T2']).to(device)
        B1s = torch.tensor(dictionaryEntries['B1']).to(device)
        TRs = torch.tensor(self.timepoints['TR'].copy()).to(device)
        TEs = torch.tensor(self.timepoints['TE'].copy()).to(device)
        FAs = torch.tensor(self.timepoints['FA'].copy()).to(device)
        PHs = torch.tensor(self.timepoints['PH'].copy()).to(device)

        numTimepoints = len(self.timepoints); numDictionaryEntries = len(dictionaryEntries)
        Mx0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        My0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        Mz0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        Time = torch.zeros((numTimepoints))

        Mx = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        My = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        Mz = torch.zeros((numSpins, numDictionaryEntries)).to(device)    
        FAs = torch.deg2rad(FAs)
        PHs = torch.deg2rad(PHs)
        
        if(inputMx is not None):
            if(torch.numel(inputMx) == numSpins*numDictionaryEntries and torch.numel(inputMy) == numSpins*numDictionaryEntries and torch.numel(inputMz) == numSpins*numDictionaryEntries):
                Mx = inputMx
                My = inputMy
                Mz = inputMz
            else:
                if(torch.numel(inputMx) == 1 and torch.numel(inputMy) == 1 and torch.numel(inputMz) == 1 ):
                    Mx = torch.ones(numSpins, numDictionaryEntries) * inputMx
                    My = torch.ones(numSpins, numDictionaryEntries) * inputMy
                    Mz = torch.ones(numSpins, numDictionaryEntries) * inputMz
                else: 
                    print("Simulation Failed: Number of input magnetization states doesn't equal number of requested spins to simulate.")
                    return
        Mx = Mx.to(device);  My = My.to(device); Mz = Mz.to(device); 

        with torch.no_grad():
            accumulatedTime = 0
            for iTimepoint in range(numTimepoints):
                fa = FAs[iTimepoint] * B1s
                tr = TRs[iTimepoint]
                te = TEs[iTimepoint]
                ph = PHs[iTimepoint]
                tre = tr-te
                
                Time[iTimepoint] = accumulatedTime
                accumulatedTime = accumulatedTime + tr

                At2te = torch.exp(-1*te/T2s)
                At1te = torch.exp(-1*te/T1s)
                Bt1te = 1-At1te
                
                At2tr = torch.exp(-1*tre/T2s)
                At1tr = torch.exp(-1*tre/T1s)
                Bt1tr = 1-At1tr

                # M2 = Rphasep*Rflip*Rphasem*M1;       % RF effect  

                # Applying Rphasem = [cos(-iph) -sin(-iph) 0; sin(-iph) cos(-iph) 0; 0 0 1];  
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = torch.multiply(torch.cos(-ph),Mxi) - torch.multiply(torch.sin(-ph), Myi)
                My = torch.multiply(torch.sin(-ph),Mxi) + torch.multiply(torch.cos(-ph), Myi)
                Mz = Mzi

                # Applying flip angle = [1 0 0; 0 cos(randflip(ii)) -sin(randflip(ii)); 0 sin(randflip(ii)) cos(randflip(ii))];
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = Mxi
                My = torch.multiply(torch.cos(fa),Myi)-torch.multiply(torch.sin(fa),Mzi)
                Mz = torch.multiply(torch.sin(fa),Myi)+torch.multiply(torch.cos(fa),Mzi)

                # Applying Rphasep = [cos(iph) -sin(iph) 0; sin(iph) cos(iph) 0; 0 0 1];  
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = torch.multiply(torch.cos(ph),Mxi) - torch.multiply(torch.sin(ph), Myi)
                My = torch.multiply(torch.sin(ph),Mxi) + torch.multiply(torch.cos(ph), Myi)
                Mz = Mzi

                # Relaxation over TE
                Mx = torch.multiply(Mx, At2te)
                My = torch.multiply(My, At2te)
                Mz = torch.multiply(Mz, At1te)+Bt1te

                # Reading value after TE and before TRE 
                Mx0[iTimepoint,:,:]=Mx.cpu()
                My0[iTimepoint,:,:]=My.cpu()
                Mz0[iTimepoint,:,:]=Mz.cpu()

                # Relaxation over TRE (TR-TE) 
                Mx = Mx*At2tr
                My = My*At2tr
                Mz = Mz*At1tr+Bt1tr
                del fa, tr, te, tre, At2te, At1te, Bt1te, At2tr, At1tr, Bt1tr, Mxi, Myi, Mzi
        del T1s, T2s, B1s, FAs, PHs, Mx, My, Mz
        return Time,Mx0,My0,Mz0

class PreparationModule(SequenceModule):
    def __init__(self, preparationType:types.PreparationType, units=None):
        SequenceModule.__init__(self, moduleType=types.ModuleType.PREPARATION, units=units) 
        self.preparationType = preparationType
    def __str__(self):
        return SequenceModule.__str__(self) + " || Preparation Type: " + self.preparationType.name


class RFPreparationModule(PreparationModule):
    def __init__(self, rfType:types.RFType, units=None):
        PreparationModule.__init__(self, preparationType=types.PreparationType.RF, units=units) 
        self.rfType = rfType
    def __str__(self):
        return PreparationModule.__str__(self) + " || RF Type: " + self.rfType.name
    
@register
class InversionModule(RFPreparationModule):
    def __init__(self, totalDuration, rfDuration=0, rfPhase=0, units=None):
        RFPreparationModule.__init__(self, rfType=types.RFType.INVERSION, units=units) 
        self.totalDuration = totalDuration   # Seconds
        self.rfDuration = rfDuration         # Seconds
        self.rfPhase = rfPhase               # Degrees -- should it be? Matches the timeseries spec
        if(rfDuration != None):
            self.rfDuration = rfDuration
        else:
            self.rfDuration = 0
        if(rfPhase != None):
            self.rfPhase = rfPhase
        else:
            self.rfPhase = 0

    def __str__(self):
        return RFPreparationModule.__str__(self) + " || Total Duration (s): " + f'{self.totalDuration:7.5f}'  + " || RF Duration (s): " + f'{self.rfDuration:7.5f}' + " || RF Phase (degrees): " + f'{self.rfPhase:7.5f}'
    
    def __dict__(self):
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "totalDuration": self.totalDuration,
            "rfDuration": self.rfDuration,
            "rfPhase": self.rfPhase
        }
        return moduleDict
    
    def ConvertUnits(self, targetUnits:SequenceUnits):
        if(self.units != targetUnits):
            self.totalDuration =  Units.Convert(self.totalDuration, self.units.time, targetUnits.time)
            self.rfDuration =  Units.Convert(self.rfDuration, self.units.time, targetUnits.time)
            self.rfPhase =  Units.Convert(self.rfPhase, self.units.angle, targetUnits.angle)
            self.units = targetUnits

    def CastToIntegers(self):
        self.totalDuration = int(self.totalDuration)
        self.rfDuration = int(self.rfDuration)
        self.rfPhase = int(self.rfPhase)
    
    def CastToFloats(self):
        self.totalDuration = float(self.totalDuration)
        self.rfDuration = float(self.rfDuration)
        self.rfPhase = float(self.rfPhase)

    @staticmethod
    def FromJson(jsonInput):
        totalDuration = jsonInput.get("totalDuration")
        rfDuration = jsonInput.get("rfDuration")
        rfPhase = jsonInput.get("rfPhase")      
        if (totalDuration != None):
            return InversionModule(totalDuration, rfDuration, rfPhase) 
        else:
            print("InversionModule requires totalDuration")

    def Simulate(self, dictionaryEntries, numSpins, device=None, inputMx=None, inputMy=None, inputMz=None): 
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")    
        T1s = torch.tensor(dictionaryEntries['T1']).to(device)
        T2s = torch.tensor(dictionaryEntries['T2']).to(device)
        B1s = torch.tensor(dictionaryEntries['B1']).to(device)

        numDictionaryEntries = len(dictionaryEntries)
        Mx0 = torch.zeros((1, numSpins, numDictionaryEntries))
        My0 = torch.zeros((1, numSpins, numDictionaryEntries))
        Mz0 = torch.zeros((1, numSpins, numDictionaryEntries))
        Time = torch.zeros((1))

        Mx = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        My = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        Mz = torch.zeros((numSpins, numDictionaryEntries)).to(device)    
        FA = torch.deg2rad(torch.tensor(180))
        PH = torch.deg2rad(torch.tensor(self.rfPhase))
        TR = self.totalDuration - self.rfDuration # Only allow for relaxation in the wait time after the RF is applied
            
        if(inputMx is not None):
            if(torch.numel(inputMx) == numSpins*numDictionaryEntries and torch.numel(inputMy) == numSpins*numDictionaryEntries and torch.numel(inputMz) == numSpins*numDictionaryEntries):
                Mx = inputMx
                My = inputMy
                Mz = inputMz
            else:
                if(torch.numel(inputMx) == 1 and torch.numel(inputMy) == 1 and torch.numel(inputMz) == 1 ):
                    Mx = (torch.ones(numSpins, numDictionaryEntries) * inputMx)
                    My = (torch.ones(numSpins, numDictionaryEntries) * inputMy)
                    Mz = (torch.ones(numSpins, numDictionaryEntries) * inputMz)
                else: 
                    print("Simulation Failed: Number of input magnetization states doesn't equal number of requested spins to simulate.")
                    return
        else:
            Mx = torch.zeros(numSpins, numDictionaryEntries)
            My = torch.zeros(numSpins, numDictionaryEntries)
            Mz = torch.ones(numSpins, numDictionaryEntries)

        Mx = Mx.to(device);  My = My.to(device); Mz = Mz.to(device); 

        with torch.no_grad():
                fa = FA
                tr = TR
                ph = PH
                At2tr = torch.exp(-1*tr/T2s)
                At1tr = torch.exp(-1*tr/T1s)
                Bt1tr = 1-At1tr

                # M2 = Rphasep*Rflip*Rphasem*M1;       % RF effect  
                # Applying Rphasem = [cos(-iph) -sin(-iph) 0; sin(-iph) cos(-iph) 0; 0 0 1];  
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = torch.multiply(torch.cos(-ph),Mxi) - torch.multiply(torch.sin(-ph), Myi)
                My = torch.multiply(torch.sin(-ph),Mxi) + torch.multiply(torch.cos(-ph), Myi)
                Mz = Mzi

                # Applying flip angle = [1 0 0; 0 cos(randflip(ii)) -sin(randflip(ii)); 0 sin(randflip(ii)) cos(randflip(ii))];
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = Mxi
                My = torch.multiply(torch.cos(fa),Myi)-torch.multiply(torch.sin(fa),Mzi)
                Mz = torch.multiply(torch.sin(fa),Myi)+torch.multiply(torch.cos(fa),Mzi)

                # Applying Rphasep = [cos(iph) -sin(iph) 0; sin(iph) cos(iph) 0; 0 0 1];  
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = torch.multiply(torch.cos(ph),Mxi) - torch.multiply(torch.sin(ph), Myi)
                My = torch.multiply(torch.sin(ph),Mxi) + torch.multiply(torch.cos(ph), Myi)
                Mz = Mzi

                # Relaxation over prep duration
                Mx = torch.multiply(Mx, At2tr)
                My = torch.multiply(My, At2tr)
                Mz = torch.multiply(Mz, At1tr)+Bt1tr

                # Reading value after TR and before TRE 
                Mx0[0,:,:]=Mx.cpu()
                My0[0,:,:]=My.cpu()
                Mz0[0,:,:]=Mz.cpu()
                Time[0] = self.totalDuration

                del fa, tr, At2tr, At1tr, Bt1tr, Mxi, Myi, Mzi
        del T1s, T2s, B1s, FA, TR, PH, Mx, My, Mz
        return Time,Mx0,My0,Mz0

@register
class T2PreparationModule(RFPreparationModule):
    def __init__(self, echoTime, rfDuration=0, units=None):
        RFPreparationModule.__init__(self, rfType=types.RFType.COMPOSITE, units=units) 
        self.echoTime = echoTime         # Seconds
        if rfDuration != None:
            self.rfDuration = rfDuration         # Seconds
        else: 
            self.rfDuration = 0

    def __str__(self):
        return RFPreparationModule.__str__(self) + " || Echo Time (s): " + f'{self.echoTime:7.5f}' + " || RF Duration (s): " + f'{self.rfDuration:7.5f}'
        
    def __dict__(self):
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "echoTime": self.echoTime,
            "rfDuration": self.rfDuration
        }
        return moduleDict
    
    def ConvertUnits(self, targetUnits:SequenceUnits):
        if(self.units != targetUnits):
            self.echoTime =  Units.Convert(self.echoTime, self.units.time, targetUnits.time)
            self.rfDuration =  Units.Convert(self.rfDuration, self.units.time, targetUnits.time)
            self.units = targetUnits

    def CastToIntegers(self):
        self.echoTime = int(self.echoTime)
        self.rfDuration = int(self.rfDuration)

    def CastToFloats(self):
        self.echoTime = float(self.echoTime)
        self.rfDuration = float(self.rfDuration)

    @staticmethod
    def FromJson(jsonInput):  
        echoTime = jsonInput.get("echoTime")
        rfDuration = jsonInput.get("rfDuration")
        if echoTime != None:
            return T2PreparationModule(echoTime, rfDuration)
        else:
            print("SpoilerModule requires echoTime")
            
    def Simulate(self, dictionaryEntries, numSpins, device=None, inputMx=None, inputMy=None, inputMz=None): 
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")    
        T1s = torch.tensor(dictionaryEntries['T1']).to(device)
        T2s = torch.tensor(dictionaryEntries['T2']).to(device)
        B1s = torch.tensor(dictionaryEntries['B1']).to(device)
        numDictionaryEntries = len(dictionaryEntries)

        Mx = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        My = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        Mz = torch.zeros((numSpins, numDictionaryEntries)).to(device) 

        TR = torch.tensor([self.echoTime/4, self.echoTime/2, self.echoTime/4, 0])
        FA = torch.deg2rad(torch.tensor([90, 180, 180, 90]))
        PH = torch.deg2rad(torch.tensor([90,   0, 180,270]))

        Mx0 = torch.zeros((len(TR), numSpins, numDictionaryEntries))
        My0 = torch.zeros((len(TR), numSpins, numDictionaryEntries))
        Mz0 = torch.zeros((len(TR), numSpins, numDictionaryEntries))
        Time = torch.zeros((len(TR)))
        #TR = self.totalDuration - self.rfDuration # Only allow for relaxation in the wait time after the RF is applied
            
        if(inputMx is not None):
            if(torch.numel(inputMx) == numSpins*numDictionaryEntries and torch.numel(inputMy) == numSpins*numDictionaryEntries and torch.numel(inputMz) == numSpins*numDictionaryEntries):
                Mx = inputMx
                My = inputMy
                Mz = inputMz
            else:
                if(torch.numel(inputMx) == 1 and torch.numel(inputMy) == 1 and torch.numel(inputMz) == 1 ):
                    Mx = (torch.ones(numSpins, numDictionaryEntries) * inputMx)
                    My = (torch.ones(numSpins, numDictionaryEntries) * inputMy)
                    Mz = (torch.ones(numSpins, numDictionaryEntries) * inputMz)
                else: 
                    print("Simulation Failed: Number of input magnetization states doesn't equal number of requested spins to simulate.")
                    return
        else:
            Mx = torch.zeros(numSpins, numDictionaryEntries)
            My = torch.zeros(numSpins, numDictionaryEntries)
            Mz = torch.ones(numSpins, numDictionaryEntries)

        Mx = Mx.to(device);  My = My.to(device); Mz = Mz.to(device); 

        with torch.no_grad():
            accumulatedTime = 0
            for iFlip in range(len(FA)):
                fa = FA[iFlip]
                tr = TR[iFlip]
                ph = PH[iFlip]
                
                Time[iFlip] = accumulatedTime
                accumulatedTime = accumulatedTime + tr

                At2tr = torch.exp(-1*tr/T2s)
                At1tr = torch.exp(-1*tr/T1s)
                Bt1tr = 1-At1tr

                # M2 = Rphasep*Rflip*Rphasem*M1;       % RF effect  
                # Applying Rphasem = [cos(-iph) -sin(-iph) 0; sin(-iph) cos(-iph) 0; 0 0 1];  
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = torch.multiply(torch.cos(-ph),Mxi) - torch.multiply(torch.sin(-ph), Myi)
                My = torch.multiply(torch.sin(-ph),Mxi) + torch.multiply(torch.cos(-ph), Myi)
                Mz = Mzi

                # Applying flip angle = [1 0 0; 0 cos(randflip(ii)) -sin(randflip(ii)); 0 sin(randflip(ii)) cos(randflip(ii))];
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = Mxi
                My = torch.multiply(torch.cos(fa),Myi)-torch.multiply(torch.sin(fa),Mzi)
                Mz = torch.multiply(torch.sin(fa),Myi)+torch.multiply(torch.cos(fa),Mzi)

                # Applying Rphasep = [cos(iph) -sin(iph) 0; sin(iph) cos(iph) 0; 0 0 1];  
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = torch.multiply(torch.cos(ph),Mxi) - torch.multiply(torch.sin(ph), Myi)
                My = torch.multiply(torch.sin(ph),Mxi) + torch.multiply(torch.cos(ph), Myi)
                Mz = Mzi

                # Relaxation over delay duration
                Mx = torch.multiply(Mx, At2tr)
                My = torch.multiply(My, At2tr)
                Mz = torch.multiply(Mz, At1tr)+Bt1tr

                Mx0[iFlip,:,:]=Mx.cpu()
                My0[iFlip,:,:]=My.cpu()
                Mz0[iFlip,:,:]=Mz.cpu()

                #Spoil at end

                del fa, tr, At2tr, At1tr, Bt1tr, Mxi, Myi, Mzi
        del T1s, T2s, B1s, FA, TR, PH, Mx, My, Mz
        return Time,Mx0,My0,Mz0


class GradientPreparationModule(PreparationModule):
    def __init__(self, gradientType:types.GradientType, units=None):
        PreparationModule.__init__(self, preparationType=types.PreparationType.GRADIENT, units=units) 
        self.gradientType = gradientType
    def __str__(self):
        return PreparationModule.__str__(self) + " || Gradient Type: " + self.gradientType.name
    
@register
class SpoilerModule(GradientPreparationModule):
    def __init__(self, dephasingRange, totalDuration, gradientDuration=None, units=None):
        GradientPreparationModule.__init__(self, gradientType=types.GradientType.SPOILER, units=units) 
        self.dephasingRange = dephasingRange       # Degrees
        self.totalDuration = totalDuration         # Seconds
        if(gradientDuration != None):
            self.gradientDuration = gradientDuration   # Seconds
        else:
            self.gradientDuration = 0

    def __str__(self):
        return GradientPreparationModule.__str__(self) + " || Dephasing Range (degrees): " + f'{self.dephasingRange:7.5f}' + " || Total Duration (s): " + f'{self.totalDuration:7.5f}'  + " || Gradient Duration (s): " + f'{self.gradientDuration:7.5f}'
            
    def __dict__(self):
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "dephasingRange": self.dephasingRange,
            "totalDuration": self.totalDuration,
            "gradientDuration": self.gradientDuration
        }
        return moduleDict
    
    def ConvertUnits(self, targetUnits:SequenceUnits):
        if(self.units != targetUnits):
            self.dephasingRange =  Units.Convert(self.dephasingRange, self.units.angle, targetUnits.angle)
            self.totalDuration =  Units.Convert(self.totalDuration, self.units.time, targetUnits.time)
            self.gradientDuration =  Units.Convert(self.gradientDuration, self.units.time, targetUnits.time)
            self.units = targetUnits

    def CastToIntegers(self):
        self.dephasingRange = int(self.dephasingRange)
        self.totalDuration = int(self.totalDuration)
        self.gradientDuration = int(self.gradientDuration)

    def CastToFloats(self):
        self.dephasingRange = float(self.dephasingRange)
        self.totalDuration = float(self.totalDuration)
        self.gradientDuration = float(self.gradientDuration)

    @staticmethod
    def FromJson(jsonInput):  
        dephasingRange = jsonInput.get("dephasingRange")
        totalDuration = jsonInput.get("totalDuration")
        gradientDuration = jsonInput.get("gradientDuration")
        if totalDuration != None and dephasingRange != None:
            return SpoilerModule(dephasingRange, totalDuration, gradientDuration)
        else:
            print("SpoilerModule requires dephasingRange and totalDuration")
        
    def Simulate(self, dictionaryEntries, numSpins, device=None, inputMx=None, inputMy=None, inputMz=None): 
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")    
        T1s = torch.tensor(dictionaryEntries['T1']).to(device)
        T2s = torch.tensor(dictionaryEntries['T2']).to(device)
        B1s = torch.tensor(dictionaryEntries['B1']).to(device)

        numDictionaryEntries = len(dictionaryEntries)
        phaseValues = np.linspace(-1*self.dephasingRange/2, self.dephasingRange/2, numSpins)
        spinOffresonances = torch.tensor(phaseValues).to(device)
        spinOffresonances = torch.deg2rad(spinOffresonances)

        Mx0 = torch.zeros((1, numSpins, numDictionaryEntries))
        My0 = torch.zeros((1, numSpins, numDictionaryEntries))
        Mz0 = torch.zeros((1, numSpins, numDictionaryEntries))
        Time = torch.zeros((1))

        Mx = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        My = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        Mz = torch.zeros((numSpins, numDictionaryEntries)).to(device)    
        TR = self.totalDuration - self.gradientDuration # Only allow for relaxation in the wait time after the dephasing is applied
        
        phaseValueCosines = torch.cos(spinOffresonances)
        phaseValueSines = torch.sin(spinOffresonances)

        if(inputMx is not None):
            if(torch.numel(inputMx) == numSpins*numDictionaryEntries and torch.numel(inputMy) == numSpins*numDictionaryEntries and torch.numel(inputMz) == numSpins*numDictionaryEntries):
                Mx = inputMx
                My = inputMy
                Mz = inputMz
            else:
                if(torch.numel(inputMx) == 1 and torch.numel(inputMy) == 1 and torch.numel(inputMz) == 1 ):
                    Mx = torch.ones(numSpins, numDictionaryEntries) * inputMx
                    My = torch.ones(numSpins, numDictionaryEntries) * inputMy
                    Mz = torch.ones(numSpins, numDictionaryEntries) * inputMz
                else: 
                    print("Simulation Failed: Number of input magnetization states doesn't equal number of requested spins to simulate.")
                    return
        else:
            Mx = torch.zeros(numSpins, numDictionaryEntries)
            My = torch.zeros(numSpins, numDictionaryEntries)
            Mz = torch.ones(numSpins, numDictionaryEntries)

        Mx = Mx.to(device);  My = My.to(device); Mz = Mz.to(device); 

        with torch.no_grad():
                tr = TR
                At2tr = torch.exp(-1*tr/T2s)
                At1tr = torch.exp(-1*tr/T1s)
                Bt1tr = 1-At1tr

                # Applying off-resonance to spins
                Mxi = Mx.t()
                Myi = My.t()
                Mx = (torch.multiply(phaseValueCosines,Mxi) - torch.multiply(phaseValueSines,Myi)).t()
                My = (torch.multiply(phaseValueSines,Mxi) + torch.multiply(phaseValueCosines,Myi)).t()

                # Relaxation over prep duration
                Mx = torch.multiply(Mx, At2tr)
                My = torch.multiply(My, At2tr)
                Mz = torch.multiply(Mz, At1tr)+Bt1tr

                # Reading value after TR and before TRE 
                Mx0[0,:,:]=Mx.cpu()
                My0[0,:,:]=My.cpu()
                Mz0[0,:,:]=Mz.cpu()
                Time[0] = self.totalDuration

                del tr, At2tr, At1tr, Bt1tr, Mxi, Myi
        del T1s, T2s, B1s, TR, Mx, My, Mz
        return Time,Mx0,My0,Mz0


class RecoveryModule(SequenceModule):
    def __init__(self, recoveryType:types.RecoveryType, units=None):
        SequenceModule.__init__(self, moduleType=types.ModuleType.RECOVERY, units=units) 
        self.recoveryType = recoveryType
    def __str__(self):
        return SequenceModule.__str__(self) + " || Recovery Type: " + self.recoveryType.name

@register 
class DeadtimeRecoveryModule(RecoveryModule):
    def __init__(self, totalDuration, units=None):
        RecoveryModule.__init__(self, recoveryType=types.RecoveryType.DEADTIME, units=units) 
        self.totalDuration = totalDuration   # Seconds

    def __str__(self):
        return RecoveryModule.__str__(self) + " || Total Duration (s): " + f'{self.totalDuration:7.5f}'
    
    def __dict__(self):
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "totalDuration": self.totalDuration,
        }
        return moduleDict
        
    def ConvertUnits(self, targetUnits:SequenceUnits):
        if(self.units != targetUnits):
            self.totalDuration =  Units.Convert(self.totalDuration, self.units.time, targetUnits.time)
            self.units = targetUnits

    def CastToIntegers(self):
        self.totalDuration = int(self.totalDuration)
    
    def CastToFloats(self):
        self.totalDuration = float(self.totalDuration)

    @staticmethod
    def FromJson(jsonInput):  
        totalDuration = jsonInput.get("totalDuration")
        if totalDuration != None:
            return DeadtimeRecoveryModule(totalDuration)
        else:
            print("DeadtimeRecoveryModule requires totalDuration")
    
    def Simulate(self, dictionaryEntries, numSpins, device=None, inputMx=None, inputMy=None, inputMz=None): 
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")    
        T1s = torch.tensor(dictionaryEntries['T1']).to(device)
        T2s = torch.tensor(dictionaryEntries['T2']).to(device)
        B1s = torch.tensor(dictionaryEntries['B1']).to(device)

        numDictionaryEntries = len(dictionaryEntries)
        Mx0 = torch.zeros((1, numSpins, numDictionaryEntries))
        My0 = torch.zeros((1, numSpins, numDictionaryEntries))
        Mz0 = torch.zeros((1, numSpins, numDictionaryEntries))
        Time = torch.zeros((1))

        Mx = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        My = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        Mz = torch.zeros((numSpins, numDictionaryEntries)).to(device)    
        TR = self.totalDuration
            
        if(inputMx is not None):
            if(torch.numel(inputMx) == numSpins*numDictionaryEntries and torch.numel(inputMy) == numSpins*numDictionaryEntries and torch.numel(inputMz) == numSpins*numDictionaryEntries):
                Mx = inputMx
                My = inputMy
                Mz = inputMz
            else:
                if(torch.numel(inputMx) == 1 and torch.numel(inputMy) == 1 and torch.numel(inputMz) == 1 ):
                    Mx = (torch.ones(numSpins, numDictionaryEntries) * inputMx)
                    My = (torch.ones(numSpins, numDictionaryEntries) * inputMy)
                    Mz = (torch.ones(numSpins, numDictionaryEntries) * inputMz)
                else: 
                    print("Simulation Failed: Number of input magnetization states doesn't equal number of requested spins to simulate.")
                    return
        else:
            Mx = torch.zeros(numSpins, numDictionaryEntries)
            My = torch.zeros(numSpins, numDictionaryEntries)
            Mz = torch.ones(numSpins, numDictionaryEntries)

        Mx = Mx.to(device);  My = My.to(device); Mz = Mz.to(device); 

        with torch.no_grad():
                tr = TR
                At2tr = torch.exp(-1*tr/T2s)
                At1tr = torch.exp(-1*tr/T1s)
                Bt1tr = 1-At1tr

                # Relaxation over prep duration
                Mx = torch.multiply(Mx, At2tr)
                My = torch.multiply(My, At2tr)
                Mz = torch.multiply(Mz, At1tr)+Bt1tr

                # Reading value after TR and before TRE 
                Mx0[0,:,:]=Mx.cpu()
                My0[0,:,:]=My.cpu()
                Mz0[0,:,:]=Mz.cpu()
                Time[0] = self.totalDuration
                del tr, At2tr, At1tr, Bt1tr
        del T1s, T2s, B1s, TR, Mx, My, Mz
        return Time,Mx0,My0,Mz0

class SequenceParameters:
    def __init__(self, name:str, modules=[], version="dev", sequenceUnits=SequenceUnits(Units.SECONDS,Units.DEGREES)):
        self.name = name
        self.modules = modules 
        self.version = version
        self.units = sequenceUnits

    def __str__(self):
        moduleDescriptions = ""
        for module in self.modules:
            moduleDescriptions = moduleDescriptions + str(module) + "\n------------------\n"
        return "Sequence: " + self.name + "\nModules:\n------------------\n" + moduleDescriptions
    
    def __dict__(self):
        mrftools_version = version("mrftools")
        sequenceDict  = {
            "name": self.name,
            "version": self.version,
            "units" : self.units.__dict__(),
            "modules": []
        }
        for module in self.modules:
            sequenceDict.get("modules").append(module.__dict__())
        sequenceParametersDict = {
            "mrftools_version":mrftools_version,
            "sequence":sequenceDict
        }
        return sequenceParametersDict

    def ConvertUnits(self, newUnits):
        if (self.units.time != newUnits.time) or (self.units.angle != newUnits.angle):
            for module in self.modules:
                module.ConvertUnits(newUnits)
            self.units = newUnits

    def CastToIntegers(self):
        for module in self.modules:
            module.CastToIntegers() 

    def CastToFloats(self):
        for module in self.modules:
            module.CastToFloats() 
    
    ## Cast to integers during export is NOT a lossless process, so that simulations run on the exported data match scanner execution
    def ExportToJson(self, baseFilepath="", exportUnits=SequenceUnits(Units.MICROSECONDS, Units.CENTIDEGREES), castToIntegers=True):
        originalUnits = self.units
        self.ConvertUnits(exportUnits)
        if castToIntegers:
            self.CastToIntegers()
        sequenceFilename = baseFilepath+self.name+"_"+self.version+".sequence"
        with open(sequenceFilename, 'w') as outfile:
            json.dump(self.__dict__(), outfile, indent=2)
        if castToIntegers:
            self.CastToFloats()
        self.ConvertUnits(originalUnits)
    
    def Simulate(self, dictionaryEntries, numSpins, device=None):
        if self.units.time != Units.SECONDS or self.units.angle != Units.DEGREES:
            print("Sequence Units are not the required Seconds/Degrees. Converting before simulation. ")
            self.ConvertUnits(SequenceUnits(Units.SECONDS, Units.DEGREES))
            
        Time = torch.zeros([1]); 
        Mx0 = torch.zeros([1,numSpins, len(dictionaryEntries)]); ReadoutMx0 = torch.zeros([1,numSpins, len(dictionaryEntries)]); 
        My0 = torch.zeros([1,numSpins, len(dictionaryEntries)]); ReadoutMy0 = torch.zeros([1,numSpins, len(dictionaryEntries)]); 
        Mz0 = torch.ones([1,numSpins, len(dictionaryEntries)]);  ReadoutMz0 = torch.ones([1,numSpins, len(dictionaryEntries)])

        for module in self.modules:
            resultTime, resultMx0, resultMy0, resultMz0 = module.Simulate(dictionaryEntries, numSpins, device=device, inputMx=Mx0[-1,:,:], inputMy=My0[-1,:,:], inputMz=Mz0[-1,:,:])
            Time = torch.cat((Time, resultTime+Time[-1])); Mx0 = torch.cat((Mx0, resultMx0)); My0 = torch.cat((My0, resultMy0)); Mz0 = torch.cat((Mz0, resultMz0)); 
            if(issubclass(module.__class__, AcquisitionModule)):
                ReadoutMx0 = torch.cat((ReadoutMx0, resultMx0))
                ReadoutMy0 = torch.cat((ReadoutMy0, resultMy0))
                ReadoutMz0 = torch.cat((ReadoutMz0, resultMz0))
        return Time, (Mx0, My0, Mz0), (ReadoutMx0, ReadoutMy0, ReadoutMz0)

    @staticmethod
    def FromJson(inputJson):
        mrftoolsVersion = inputJson.get("mrftools_version")
        print("Input file mrttools Version:", mrftoolsVersion)

        sequenceJson = inputJson.get("sequence")
        sequenceName = sequenceJson.get("name")
        sequenceVersion = sequenceJson.get("version")
        unitsJson = sequenceJson.get("units")
        sequenceUnits = SequenceUnits.FromJson(unitsJson)
        modulesJson = sequenceJson.get("modules")
        sequenceModules = []
        for moduleJson in modulesJson:
            sequenceModules.append(SequenceModule.FromJson(moduleJson, sequenceUnits))

        return SequenceParameters(sequenceName,sequenceModules, sequenceVersion, sequenceUnits)
    
"""
    def Export(self, filename:str, force=False):
        if ".mrf" in filename:
            outfile = h5py.File(filename, "a")
            try:
                outfile.create_group("sequenceParameters")
            except:
                pass
            if (self.name in list(outfile["sequenceParameters"].keys())) and not force:
                print("Sequence Parameter set '" + self.name + "' already exists in .mrf file. Specify 'force' to overwrite")
            else:
                try:
                    del outfile["sequenceParameters"][self.name]
                except:
                    pass
                sequenceParameters = outfile["sequenceParameters"].create_group(self.name)
                sequenceParameters.attrs.create("name", self.name)
                sequenceParameters.attrs.create("type", self.type.name)
                sequenceParameters["timepoints"] = self.timepoints
                outfile.close()
        else:
            print("Input is not a .mrf file")

"""