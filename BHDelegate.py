# This is the file that contains the top control code for the program

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtCore import Slot
from BHMainWindow import BHMainWindow

# BHDelegate
# Responsible for main control logic
class BHDelegate(QMainWindow):
    def __init__(self):
        super(BHDelegate, self).__init__()
        # Main setup
        app = QApplication()

        # Instantiate main window
        self.window = BHMainWindow()
        self.welcomeWindow = None
        self.newScenarioWindow = None
        self.machineListWindow = None
        self.createEditVMWindow = None
        self.VMSettingWindow = None


        #1 try to load local list of scenarios, meanwhile contact backend and request list of existing scenarios, update accordingly
        self.scenariosObject = BHScenariosObject()
            #populate object with either local info or backend reply

        #2 Bring up up and show Welcome WindoW

        self.welcomeWindow = WelcomeWindow(self.BHScenarios)
        self.welcomeWindow.createScenarioAction.connect(createNewScenario)
        self.welcomeWindow.show()

         



#CALLBACKS
    @Slot()
    def createNewScenario(self):
        newScenarioObject = BHScenario()
        #3 User clicks createscenario,
        self.BHScenarios.addScenario(newScenarioObject)
        
        self.newScenarioWindow = NewScenarioWindow(newScenarioObject)

        self.newScenarioWindow.onNextAction.connect(showMachineList)



    @Slot()
    def showMachineList(self, BHScenario):
        self.machineListWindow = MachineList(BHScenario)
        #machine list will call create/edit window
        #self.machineListWindow.onCreateVM.connect(createVM)
        self.machineListWindow.onSaveEvent.connect(showMainWindow)

    @Slot()
    def showMainWindow(self, BHScenario):
        self.window.show()
        pass


if __name__ == "__main__":
    BHDelegate = BHDelegate()
        





    # Execute Qt
    sys.exit(app.exec_())
