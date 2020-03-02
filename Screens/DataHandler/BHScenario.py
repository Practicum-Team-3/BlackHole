from Screens.DataHandler.BHMachine import BHMachine
import json

class BHScenario(object):
    def __init__(self, scenarioJSON=''):
        self.scenario_name = ''
        self.id = ''
        self.creation_date = ''
        self.last_accessed = ''
        self.exploit_info = None
        self.vulnerability_info = None
        self.POVMachines = []#array of BHMachines
        self.victimMachines = []#array of BHMachines
        self.network_settings = None

        if scenarioJSON != '':
            self.fromJSON(scenarioJSON)

    def setName(self, newName):
        self.scenario_name = newName


    #returns the list of POV machines
    def getPOVMachines(self):
        return self.POVMachines


    #returns the list of victim machines
    def getVictimMachines(self):
        return self.victimMachines


    #deletes the pov machine with the given machineID
    def deletePOVMachine(self, machineID):
        for i in range(len(self.POVMachines)):
            if self.POVMachines[i].getMachineID() == machineID:
                self.POVMachines.pop(i)
                return True
        return False

    #deletes the victim machine with given machineID
    def deleteVictimMachine(self, machineID):
        for i in range(len(self.victimMachines)):
            if self.victimMachines[i].getMachineID() == machineID:
                self.victimMachines.pop(i)
                return True
        return False

    #appends a new machines to the corresponding list
    def addMachine(self, BHMachine):
        if BHMachine.isVictim():
            if len(self.victimMachines) > 0:
                BHMachine.setMachineID(self.victimMachines[len(self.victimMachines) - 1].getMachineID() + 1)
            else:
                BHMachine.setMachineID(1)
            self.victimMachines.append(BHMachine)

        else:
            if len(self.POVMachines) > 0:
                BHMachine.setMachineID(self.POVMachines[len(self.victimMachines) - 1].getMachineID() + 1)
            else:
                BHMachine.setMachineID(1)
            self.POVMachines.append(BHMachine)


    #Replaces the machine 
    def replaceMachine(self, id, BHMachine, inVictims):
        if inVictims:
            for i in range(len(self.victimMachines)): 
                if self.victimMachines[i].getMachineID() == id:
                    self.victimMachines.pop(i)
                    self.victimMachines.insert(i, BHMachine)
        else:
            for i in range(len(self.POVMachines)): 
                if self.POVMachines[i].getMachineID() == id:
                    self.POVMachines.pop(i)
                    self.POVMachines.insert(i, BHMachine)

    #populates this object from a JSON string
    def fromJSON(self, jsonObject):
        self.scenario_name = jsonObject['scenario_name']
        self.id = jsonObject['id']
        self.creation_date = jsonObject['creation_date']
        self.last_accessed = jsonObject['last_accessed']
        self.exploit_info = BHExploitInfo(jsonObject['exploit_info'])
        self.vulnerability_info = BHVulnerabilityInfo(jsonObject['vulnerability_info'])
        self.POVMachines = self.getPOVObjsFromDict(jsonObject['machines'])
        self.victimMachines = self.getVictimObjsFromDict(jsonObject['machines'])
        self.network_settings = BHNetworkSettings(jsonObject['network_settings'])

    #returns a JSON string representation of this object
    def toJSON(self):
        pass

    #receives a list of machine dictionaries and returns a list of objects with the POV machines
    def getPOVObjsFromDict(self, machineJSONArray):
        POVObjectsArray = []
        for i in range(len(machineJSONArray)):
            if machineJSONArray[i]['type'] == 'pov':
                newPOVMachine = BHMachine()
                newPOVMachine.fromJSON(machineJSONArray[i])
                POVObjectsArray.append(newPOVMachine)

        return POVObjectsArray

    #receives a list of machine dictionaries and returns a list of objects with the victim machines
    def getVictimObjsFromDict(self, machineJSONArray):
        victimObjectsArray = []
        for i in range(len(machineJSONArray)):
            if machineJSONArray[i]['type'] == 'victim':
                newVictimMachine = BHMachine()
                newVictimMachine.fromJSON(machineJSONArray[i])
                victimObjectsArray.append(newVictimMachine)
                
        return victimObjectsArray



#HELPER CLASSES
class BHExploitInfo(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def getDict(self):
        return self.dictionary


class BHVulnerabilityInfo(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary
    
    def getDict(self):
        return self.dictionary


class BHNetworkSettings(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary
    
    def getDict(self):
        return self.dictionary