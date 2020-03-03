from Screens.DataHandler.BHScenario import BHScenario
from PySide2.QtCore import Slot, QDate, Signal
from PySide2.QtCore import Slot, Signal
import requests
import json

class BHScenarios(object):


    def __init__(self, widowAddress):

        self.widowAddress = widowAddress

        # List of scenario names
        self.scenarioNamesList = []
        # Dictionary of BHScenario objects indexed by name
        self.scenarios = {}


    # Set backend address
    def setWidowAddress(self, address):
        self.widowAddress = address

# ============
# Load
# ============

    # Load scenarios from a specific address
    def loadScenarioList(self):
        try:
            req = requests.get(self.widowAddress+"/scenarios/all")
            if req.status_code==requests.codes.ok:
                self.scenarioNamesList = req.json()["scenarios"]
        except:
            print("oops1")


    # Load single scenario from Widow by it's name
    def loadScenarioByName(self, name):
        try:
            req = requests.get(self.widowAddress+"/scenarios/"+name)
            if req.status_code==requests.codes.ok:
                self.addScenario(BHScenario(req.json()))
        except:
            print("oops2")

    # Load all scenarios into memory
    def loadAllScenarios(self):
        self.scenarios = {}
        for scenarioName in self.scenarioNamesList:
            self.loadScenarioByName(scenarioName)
    

    def addScenario(self, scenario):
        self.scenarios[scenario.getName()] = scenario

# ============
# Save
# ============

    # Save scenario name on widow
    def saveScenarioDeclaration(self, scenario):
        try:
            req = requests.get(self.widowAddress+"/scenarios/new/"+scenario.getName())
            if req.status_code==requests.codes.ok:
                return True
        except:
            return False

    # Call to trigger a save to Widow
    def saveScenario(self, scenario):
        try:
            post = requests.post(self.widowAddress+"/scenarios/edit/"+scenario.getName(), scenario.toJSON())
        except:
            print("saveNewScenarioFailed")


# ============
# Get multiple scenarios / scenario names
# ============

    # Returns list of scenario ids
    def getScenarioIdList(self):
        scenarioIds = []

        for scenarioName in self.scenarioNamesList:
            scenarioIds.append(self.scenarios[scenarioName].getName())

        return scenarioIds

    def getScenarioNamesList(self):
        return self.scenarioNamesList

# ============
# Get single scenario
# ============

    # Returns a BHScenario instance from id
    def getScenarioById(self, id):
        testScenarioObject = BHScenario()

        scenarioJSONObject = json.loads(self.testScenario)
        testScenarioObject.fromJSON(scenarioJSONObject)

        testScenarioObject.setId(id)
        testScenarioObject.setName(self.scenarios[id])
        testScenarioObject.setDescription("default description")

        return testScenarioObject

    # Returns a BHScenario instance from the name
    def getScenarioByName(self, name):
        return self.scenarios[name]

    # Returns list of BHScenario objects
    def getScenarios(self):
        scenariosComp = []

        for scenarioName in self.scenarios:
            scenariosComp.append(self.getScenarioByName(scenarioName))
        return scenariosComp

    # Remove a scenario
    def removeScenarioById(self, id):
        self.scenarioList.remove(id)
        self.scenarios.pop(id)

    # == Deprecated ==
    def getScenario(self):
        testScenarioObject = BHScenario()
        scenarioJSONObject = json.loads(self.testScenario)
        testScenarioObject.fromJSON(scenarioJSONObject)
        return testScenarioObject

