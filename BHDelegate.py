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
        self.testScenarios = BHScenarios()

        # Instantiate main window
        self.window = BHMainWindow(self.testScenarios)
        self.welcomeScreen = None
        self.newScenarioWindow = None
        self.machineListWindow = None
        #self.createEditVMWindow = None
        #self.VMSettingWindow = None


        #2 Bring up up and show Welcome WindoW

        # self.welcomeWindow = WelcomeWindow(testScenarios)
        # self.welcomeWindow.createScenarioAction.connect(self.createNewScenario)
        # self.welcomeWindow.show()

        self.welcomeScreen = BHWelcomeScreen(self.testScenarios)
        self.welcomeScreen.newScenarioRequested.connect(self.createNewScenario)
        self.welcomeScreen.show()



#CALLBACKS
    @Slot()
    def createNewScenario(self):

        self.welcomeScreen.hide()

        # TODO: Change to a new instance of BHScenarios
        self.newScenario = self.testScenarios.getScenario()


        # move to function called when 
        # self.BHScenarios.addScenario(newScenarioObject)
        
        self.newScenarioWindow = BHNewScenario(self.newScenario)
        self.newScenarioWindow.scenarioCreatedAction.connect(self.showMachineList)

        self.newScenarioWindow.show()



    @Slot()
    def showMachineList(self):

        self.testScenarios.addScenario(self.newScenario)

        self.machineListWindow = MachineListDialog(self.newScenario)
        #machine list will call create/edit window
        #self.machineListWindow.onCreateVM.connect(createVM)
        self.machineListWindow.ui.buttonBox.accepted.connect(self.showMainWindow)

        self.machineListWindow.show()

    @Slot()
    def showMainWindow(self):

        self.machineListWindow.hide()

        self.window.update()
        self.window.show()


if __name__ == "__main__":
    app = QApplication()
    BHDelegate = BHDelegate()

    # Execute Qt
    sys.exit(app.exec_())
