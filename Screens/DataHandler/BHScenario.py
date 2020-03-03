import json
import copy
from Screens.DataHandler.BHMachine import BHMachine

from  Screens.DataHandler.BHDataDefaults import *

class BHScenario(object):


    def __init__(self, scenarioJSON = None):
#        self.scenario_name = ''
#        self.id = ''
#        self.description = ""
#        self.creation_date = ''
#        self.last_accessed = ''
#        self.exploit_info = None
#        self.vulnerability_info = None
        self.POVMachines = []#array of BHMachines
        self.victimMachines = []#array of BHMachines
#        self.network_settings = None
        self.scenarioJSON = {}

        if scenarioJSON == None:
            self.fromJSON(json.loads(NEWSCENARIO))
        else:
            self.fromJSON(scenarioJSON)


# === NAME
    def setName(self, newName):
        self.scenarioJSON["scenario_name"] = newName

    def getName(self):
        return self.scenarioJSON["scenario_name"]
# === ID
    def setId(self, id):
        self.scenarioJSON["scenario_id"] = id

    def getId(self):
        return self.scenarioJSON["scenario_id"]

# === Description
    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return "elf.description"
# ===
    #returns the list of POV machines
    def getPOVMachines(self):
        return self.POVMachines


    #returns the list of victim machines
    def getVictimMachines(self):
        return self.victimMachines

# ===
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
    def addMachine(self, machine):
        if machine.getIsVictim():
            if len(self.victimMachines) > 0:
                machine.setMachineID(self.victimMachines[len(self.victimMachines) - 1].getMachineID() + 1)
            else:
                machine.setMachineID(1)
            self.victimMachines.append(machine)

        else:
            if len(self.POVMachines) > 0:
                machine.setMachineID(self.POVMachines[len(self.victimMachines) - 1].getMachineID() + 1)
            else:
                machine.setMachineID(1)
            self.POVMachines.append(machine)


    #Replaces a machine with a specific ID for another
    def replaceMachine(self, id, machine, inVictims):
        if inVictims:
            for i in range(len(self.victimMachines)):
                if self.victimMachines[i].getMachineID() == id:
                    self.victimMachines.pop(i)
                    self.victimMachines.insert(i, machine)
        else:
            for i in range(len(self.POVMachines)): 
                if self.POVMachines[i].getMachineID() == id:
                    self.POVMachines.pop(i)
                    self.POVMachines.insert(i, machine)

    #populates this object from a JSON string
    def fromJSON(self, jsonObject):
        self.scenarioJSON = jsonObject

#        self.scenario_name = jsonObject['scenario_name']
#        self.id = jsonObject['id']
#        self.creation_date = jsonObject['creation_date']
#        self.last_accessed = jsonObject['last_accessed']
#        self.exploit_info = BHExploitInfo(jsonObject['exploit_info'])
#        self.vulnerability_info = BHVulnerabilityInfo(jsonObject['vulnerability_info'])
        #
        if "machines" in jsonObject and len(jsonObject['machines'])>0:
            self.POVMachines = self.getPOVObjsFromDict(jsonObject['machines'])
            self.victimMachines = self.getVictimObjsFromDict(jsonObject['machines'])
#        self.network_settings = BHNetworkSettings(jsonObject['network_settings'])

    #returns a JSON string representation of this object
    def toJSON(self):
        completeJSON = copy.deepcopy(self.scenarioJSON)

        # Add machines
        for victim in self.getVictimMachines:
            completeJSON["machines"][victim.getName()] = victim.toJSON()
        for pov in self.getPOVMachines:
            completeJSON["machines"][pov.getName()] = pov.toJSON()

        return completeJSON

    #receives a list of machine dictionaries and returns a list of objects with the POV machines
    def getPOVObjsFromDict(self, machineJSONArray):

        POVObjectsArray = []
        # Iterate over the dictionary looking for POVs and instantiate BHMachine for each
        print(machineJSONArray["attacker"])
        for machineName in machineJSONArray:
            if machineJSONArray[machineName]['is_attacker'] == True:

                newPOVMachine = BHMachine()
                newPOVMachine.fromJSON(machineJSONArray[machineName])
                POVObjectsArray.append(newPOVMachine)

        return POVObjectsArray

    #receives a list of machine dictionaries and returns a list of objects with the victim machines
    def getVictimObjsFromDict(self, machineJSONArray):
        victimObjectsArray = []
        # Iterate over the dictionary looking for victims and instantiate BHMachine for each
        for machineName in machineJSONArray:
            if machineJSONArray[machineName]['is_attacker'] == False:

                newVictimMachine = BHMachine()
                newVictimMachine.fromJSON(machineJSONArray[machineName])
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
