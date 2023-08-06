import numpy as np
import h5py
from matplotlib import pyplot as plt
import torch
from tqdm import tqdm

from mrftools import DictionaryParameters, SequenceParameters

class Simulation: 
    def __init__(self,sequenceParameters, dictionaryParameters, name="", numSpins=1, times=[], timeDomainResults=[], results=[], truncationMatrix=[], truncatedResults=[], singularValues=[]):
        self.sequenceParameters = sequenceParameters
        self.dictionaryParameters = dictionaryParameters
        self.numSpins = numSpins
        self.times = times
        self.timeDomainResults = timeDomainResults
        self.results = results
        self.truncationMatrix = truncationMatrix
        self.truncatedResults = truncatedResults
        self.singularValues = singularValues
        if not name:
            self.name = sequenceParameters.name + "_" + dictionaryParameters.name + "_" + str(numSpins)
        else:
            self.name = name

    def Execute(self, numBatches=1, device=None):
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")
        dictEntriesPerBatch = int(len(self.dictionaryParameters.entries)/numBatches)
        print("Simulating " + str(numBatches) + " batch(s) of ~" + str(dictEntriesPerBatch) + " dictionary entries")
        singleResult = self.sequenceParameters.Simulate(self.dictionaryParameters.entries[0], 1)
        self.numTimepoints = np.shape(singleResult[1][0])[0]
        self.numReadoutPoints = np.shape(singleResult[2][0])[0]
        Mxy = np.zeros((self.numTimepoints, len(self.dictionaryParameters.entries)), np.complex128)
        ReadoutMxy = np.zeros((self.numReadoutPoints, len(self.dictionaryParameters.entries)), np.complex128)
        with tqdm(total=numBatches) as pbar:
            for i in range(numBatches):
                firstDictEntry = i*dictEntriesPerBatch
                if i == (numBatches-1):
                    lastDictEntry = len(self.dictionaryParameters.entries)
                else:
                    lastDictEntry = firstDictEntry+dictEntriesPerBatch
                batchDictionaryEntries = self.dictionaryParameters.entries[firstDictEntry:lastDictEntry]
                allResults = self.sequenceParameters.Simulate(batchDictionaryEntries, self.numSpins, device=device)
                Mx = torch.mean(allResults[1][0], axis=1)
                My = torch.mean(allResults[1][1], axis=1)
                Mxy[:,firstDictEntry:lastDictEntry] = Mx+(My*1j) 
                ReadoutMx = torch.mean(allResults[2][0], axis=1)
                ReadoutMy = torch.mean(allResults[2][1], axis=1)
                ReadoutMxy[:,firstDictEntry:lastDictEntry] = ReadoutMx+(ReadoutMy*1j)
                pbar.update(1)
        self.times = allResults[0]
        self.timeDomainResults = Mxy
        self.results = ReadoutMxy
        return self.results
    
    @staticmethod
    def GetInnerProducts(querySignals, dictionarySignals):  
        querySignalsTransposed = querySignals.transpose()
        normalizedQuerySignals = querySignalsTransposed / np.linalg.norm(querySignalsTransposed, axis=1)[:,None]
        simulationResultsTransposed = dictionarySignals.transpose()
        normalizedSimulationResultsTransposed = simulationResultsTransposed / np.linalg.norm(simulationResultsTransposed, axis=1)[:,None]
        innerProducts = np.inner(normalizedQuerySignals, normalizedSimulationResultsTransposed)
        return innerProducts

    def CalculateSVD(self, desiredSVDPower=0.99, truncationNumberOverride=None):
        dictionary = self.results.transpose()
        dictionaryNorm = np.sqrt(np.sum(np.power(np.abs(dictionary[:,:]),2),1))
        dictionaryShape = np.shape(dictionary)
        normalizedDictionary = np.zeros_like(dictionary)
        for i in range(dictionaryShape[0]):
            normalizedDictionary[i,:] = dictionary[i,:]/dictionaryNorm[i]
        (u,s,v) = np.linalg.svd(normalizedDictionary, full_matrices=False)
        self.singularValues = s
        if truncationNumberOverride == None:
            (truncationNumber, totalSVDPower) = self.GetTruncationNumberFromDesiredPower(desiredSVDPower)
        else:
            truncationNumber = truncationNumberOverride
            totalSVDPower = self.GetPowerFromDesiredTruncationNumber(truncationNumber)
        vt = np.transpose(v)
        self.truncationMatrix = vt[:,0:truncationNumber]
        self.truncatedResults = np.matmul(normalizedDictionary,self.truncationMatrix).transpose()
        return (truncationNumber, totalSVDPower)

    def GetTruncationNumberFromDesiredPower(self, desiredSVDPower):
        singularVectorPowers = self.singularValues/np.sum(self.singularValues)
        totalSVDPower=0; numSVDComponents=0
        for singularVectorPower in singularVectorPowers:
            totalSVDPower += singularVectorPower
            numSVDComponents += 1
            if totalSVDPower > desiredSVDPower:
                break
        return numSVDComponents, totalSVDPower

    def GetPowerFromDesiredTruncationNumber(self, desiredTruncationNumber):
        singularVectorPowers = self.singularValues/np.sum(self.singularValues)
        totalSVDPower=np.sum(singularVectorPowers[0:desiredTruncationNumber])
        return totalSVDPower

    def Export(self, filename, force=False, includeFullResults=True, includeSVDResults=True):
        if ".mrf" in filename:
            outfile = h5py.File(filename, "a")
            try:
                outfile.create_group("simulations")
            except:
                pass
            if (self.name in list(outfile["simulations"].keys())) and not force:
                print("Simulation '" + self.name + "' already exists in .mrf file. Specify 'force' to overwrite")
            else:
                try:
                    del outfile["simulations"][self.name]
                except:
                    pass
                simulation = outfile["simulations"].create_group(self.name)
                simulation.attrs.create("name", self.name)
                simulation.attrs.create("numTimepoints", self.numTimepoints)
                simulation.attrs.create("phaseRange", self.phaseRange)
                simulation.attrs.create("numSpins", self.numSpins)
                self.sequenceParameters.Export(filename, force)
                simulation["sequenceParameters"] = outfile["/sequenceParameters/"+self.sequenceParameters.name]
                self.dictionaryParameters.Export(filename, force)
                simulation["dictionaryParameters"] = outfile["/dictionaryParameters/"+self.dictionaryParameters.name]
                if(includeFullResults):
                    simulation["results"] = self.results
                else:
                    simulation["results"] = []
                if(includeFullResults):
                    simulation["truncationMatrix"] = self.truncationMatrix
                    simulation["truncatedResults"] = self.truncatedResults
                else:
                    simulation["truncationMatrix"] = []
                    simulation["truncatedResults"] = []

                outfile.close()
        else:
            print("Input is not a .mrf file")

    def Plot(self, dictionaryEntryNumbers=[], plotTruncated=False, plotTimeDomain=False):
        if dictionaryEntryNumbers == []:
            dictionaryEntryNumbers = [int(len(self.dictionaryParameters.entries)/2)]
        ax = plt.subplot(1,1,1)
        if not plotTimeDomain:
            if not plotTruncated:
                for entry in dictionaryEntryNumbers:
                    plt.plot(abs(self.results[:,entry]), label=str(self.dictionaryParameters.entries[entry]))
            else:
                for entry in dictionaryEntryNumbers:
                    plt.plot(abs(self.truncatedResults[:,entry]), label=str(self.dictionaryParameters.entries[entry]))
        else:
            for entry in dictionaryEntryNumbers:
                plt.plot(self.times, abs(self.timeDomainResults[:,entry]), label=str(self.dictionaryParameters.entries[entry]))
        ax.legend()

    def GetAverageResult(self, indices):
        return np.average(self.results[:,indices], 1)

    def FindPatternMatches(self, querySignals, useSVD=False, truncationNumber=25):
        if querySignals.ndim == 1:
            querySignals = querySignals[:,None]
        if not useSVD:
            querySignalsTransposed = querySignals.transpose()
            normalizedQuerySignal = querySignalsTransposed / np.linalg.norm(querySignalsTransposed, axis=1)[:,None]
            simulationResultsTransposed = self.results.transpose()
            normalizedSimulationResultsTransposed = simulationResultsTransposed / np.linalg.norm(simulationResultsTransposed, axis=1)[:,None]
            innerProducts = np.inner(normalizedQuerySignal, normalizedSimulationResultsTransposed)
            return np.argmax(abs(innerProducts), axis=1)
        else:
            if self.truncatedResults[:] == []:
                self.CalculateSVD(truncationNumber)
            signalsTransposed = querySignals.transpose()
            signalSVDs = np.matmul(signalsTransposed, self.truncationMatrix)
            normalizedQuerySignalSVDs = signalSVDs / np.linalg.norm(signalSVDs, axis=1)[:,None]
            simulationResultsTransposed = self.truncatedResults.transpose()
            normalizedSimulationResultsTransposed = simulationResultsTransposed / np.linalg.norm(simulationResultsTransposed, axis=1)[:,None]
            innerProducts = np.inner(normalizedQuerySignalSVDs, normalizedSimulationResultsTransposed)
            return np.argmax(abs(innerProducts), axis=1)

    @staticmethod
    def Import(filename, simulationName):
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            simulationGroup = infile["simulations"][simulationName]
            simulationName = simulationGroup.attrs.get("name")
            simulationNumTimepoints = simulationGroup.attrs.get("numTimepoints")
            simulationPhaseRange = simulationGroup.attrs.get("phaseRange")
            simulationNumSpins = simulationGroup.attrs.get("numSpins")
            simulationResults = simulationGroup["results"][:]
            simulationTruncationMatrix = simulationGroup["truncationMatrix"][:]
            simulationTruncatedResults = simulationGroup["truncatedResults"][:]
            sequenceParametersGroup = simulationGroup["sequenceParameters"]
            importedSequenceParameters = SequenceParameters(sequenceParametersGroup.attrs.get("name"), sequenceParametersGroup["timepoints"][:])
            dictionaryParametersGroup = simulationGroup["dictionaryParameters"]
            importedDictionaryParameters = DictionaryParameters(dictionaryParametersGroup.attrs.get("name"), dictionaryParametersGroup["entries"][:])
            new_simulation = Simulation(importedSequenceParameters, importedDictionaryParameters, simulationName, simulationNumTimepoints, simulationPhaseRange, simulationNumSpins, simulationResults, simulationTruncationMatrix, simulationTruncatedResults)
            infile.close()
            return new_simulation
        else:
            print("Input is not a .mrf file")
    
    @staticmethod
    def GetAvailableSimulations(filename):
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            return list(infile["simulations"].keys())
        else:
            print("Input is not a .mrf file")

