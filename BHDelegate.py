# This is the file that contains the top control code for the program

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtCore import Slot
from Screens.DataHandler.BHScenarios import BHScenarios
from Screens.DataHandler.BHScenario import BHScenario
from Screens.DataHandler.BHMachine import BHMachine
from BHMainWindow import BHMainWindow
from Screens.MachineList import MachineListDialog
from Screens.BHWelcomeScreen import BHWelcomeScreen
from Screens.BHNewScenario import BHNewScenario
# BHDelegate
# Responsible for main control logic
class BHDelegate(QMainWindow):
    def __init__(self):
        super(BHDelegate, self).__init__()
        # Main setu

        # 1 
        self.scenarios = BHScenarios("http://127.0.0.1:5000")
        self.scenarios.loadScenarioList()
        self.scenarios.loadAllScenarios()

        # Instantiate main window
        self.window = BHMainWindow()
        self.welcomeScreen = None
        self.newScenarioWindow = None
        self.machineListWindow = None
        #self.createEditVMWindow = None
        #self.VMSettingWindow = None


        #2 Bring up up and show Welcome WindoW

        # self.welcomeWindow = WelcomeWindow(testScenarios)
        # self.welcomeWindow.createScenarioAction.connect(self.createNewScenario)
        # self.welcomeWindow.show()

        self.welcomeScreen = BHWelcomeScreen(self.scenarios)
        self.welcomeScreen.newScenarioRequested.connect(self.createNewScenario)
        self.welcomeScreen.openScenarioRequested.connect(self.openScenarioByName)
        self.welcomeScreen.show()



#CALLBACKS
    @Slot()
    def createNewScenario(self):

        self.welcomeScreen.hide()

        self.newScenario = BHScenario()


        # move to function called when 
        # self.BHScenarios.addScenario(newScenarioObject)
        
        self.newScenarioWindow = BHNewScenario(self.newScenario)
        self.newScenarioWindow.scenarioCreatedAction.connect(self.showMachineList)

        self.newScenarioWindow.show()

    @Slot()
    def openScenarioByName(self, scenarioName):

        self.window.openScenario(self.scenarios.getScenarioByName(scenarioName))
        self.window.show()


    @Slot()
    def showMachineList(self):

        self.scenarios.addScenario(self.newScenario)

        self.machineListWindow = MachineListDialog(self.newScenario)
        #machine list will call create/edit window
        #self.machineListWindow.onCreateVM.connect(createVM)
        self.machineListWindow.ui.buttonBox.accepted.connect(self.finalizeScenarioCreation)

        self.machineListWindow.show()

    @Slot()
    def finalizeScenarioCreation(self):
        # Finally add the new scenario
        self.scenarios.addScenario(self.newScenario)

        # Save to backend
        if self.scenarios.saveScenarioDeclaration(self.newScenario):
            self.scenarios.saveScenario(self.newScenario)

            self.machineListWindow.hide()
            self.window.openScenario(self.newScenario)
            self.window.show()



if __name__ == "__main__":
    app = QApplication()
    BHDelegate = BHDelegate()

    # Execute Qt
    sys.exit(app.exec_())
