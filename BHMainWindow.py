import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QFrame
from PySide2.QtCore import Slot
from Screens.Interfaces.ui_mainWindow import Ui_MainWindow

from Screens.Interfaces.networkWindowInternals.ui_networkPanel import Ui_NetworkPanel
from Screens.Interfaces.networkWindowInternals.ui_machineInfo import Ui_MachineInfo
from Screens.Interfaces.networkWindowInternals.NetworkConfig.Graphics import NetworkGraph

from Screens.DataHandler.BHScenarios import *
from Screens.DataHandler.BHScenario import *

# BHMainWindow
class BHMainWindow(QMainWindow):
    def __init__(self, scenarios):
        super(BHMainWindow, self).__init__()

        # Keep reference to scenarios
        self.scenarios = scenarios

        # Draw top window UI (includes tab support and empty views)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # TODO: Call update
        
    # Call to notify of external changes to data
    def update(self):
        # === Create tabs with scenarios and pass BHScenario objects to the network panels created ===
        # TODO: Implement programatic tab and panel creation

        # Get a scenario from scenarios
        # TODO: update getScenario function to the official implementation and traverse through available scenarios
        singleScenario = self.scenarios.getScenario()

        # Fill a default tab view with the newtork panel and pass a single scenario for handling
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.defaultTab), singleScenario.scenario_name)
        self.defaultNetworkPanel = BHNetworkPanel(singleScenario)
        self.ui.gridLayoutTab.addWidget(self.defaultNetworkPanel, 0, 0, 1, 1)


# === Single Tab (the network panel) ===
# Handles a single BHScenario instance
class BHNetworkPanel(QFrame):
    def __init__(self, scenario):
        super(BHNetworkPanel, self).__init__()

        # Keep reference to the scenario
        self.scenario = scenario

        # Draw main network panel ui (with the empty frames sections)
        self.ui = Ui_NetworkPanel()
        self.ui.setupUi(self)

        # === Add the parts to the section frames ===

        # /= Machine info
        self.machineInfo = BHMachineInfo()
        # Preselect a machine
        # TODO: Make the preselection process safer
        self.selectedMachine = scenario.getPOVMachines()[0]
        self.populateMachineInfo()
        self.machineInfo.ui.editButton.clicked.connect(self.editClicked)
        self.ui.machineInfoArea.addWidget(self.machineInfo, 0, 0, 1, 1)

        # /= Network View
        self.networkGraph = NetworkGraph()
        self.ui.graphArea.addWidget(self.networkGraph, 0, 0, 1, 1)

        # /= Component view

    # Call to populate the fields of the machine Info section with the info of the selected machine
    def populateMachineInfo(self):
        self.machineInfo.ui.name.setText(self.selectedMachine.getFieldsToShow()["name"])
        self.machineInfo.ui.os.setText(self.selectedMachine.getFieldsToShow()["os"])


    @Slot()
    def editClicked(self):
        # STUB: init machine edit, subscribe to events, and show
        pass

# View that displays basic information from a machine
class BHMachineInfo(QFrame):
    def __init__(self):
        super(BHMachineInfo, self).__init__()

        self.ui = Ui_MachineInfo()
        self.ui.setupUi(self)

