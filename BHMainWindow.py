import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QFrame, QWidget, QGridLayout
from PySide2.QtCore import Slot
from Screens.Interfaces.ui_mainWindow import Ui_MainWindow

from Screens.Interfaces.networkWindowInternals.ui_networkPanel import Ui_NetworkPanel
from Screens.Interfaces.networkWindowInternals.ui_machineInfo import Ui_MachineInfo
from Screens.Interfaces.networkWindowInternals.NetworkConfig.Graphics import NetworkGraph

from Screens.DataHandler.BHScenarios import *
from Screens.DataHandler.BHScenario import *

# BHMainWindow
class BHMainWindow(QMainWindow):
    def __init__(self):
        super(BHMainWindow, self).__init__()

        # Keep references to scenarios in tuples of scenario, tab, layout
        self.openScenarios = []

        # Draw top window UI (includes tab support and empty views)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # TODO: Call update


    def openScenario(self, scenario):
        self.createNewTabForScenario(scenario)

    def createNewTabForScenario(self, scenario):
        # create tab
        newTab = QWidget()
        # add layout to tab
        tabLayout = QGridLayout(newTab)
        tabLayout.setContentsMargins(0, 0, 0, 0)
        # add tab to window
        newTabIndex = self.ui.tabWidget.addTab(newTab, "")

        # set tab name
        self.ui.tabWidget.setTabText(newTabIndex, scenario.getName())
        # add network panel
        networkPanel = BHNetworkPanel(scenario)
        tabLayout.addWidget(networkPanel, 0, 0, 1, 1)

        self.ui.tabWidget.setCurrentIndex(newTabIndex)

        # Keep track of the open scenarios
        self.openScenarios.append(scenario)

    # Call to notify of external changes to data
    def generateTab(self):
        # === Create tabs with scenarios and pass BHScenario objects to the network panels created ===
        # TODO: Implement programatic tab and panel creation

        # Get a scenario from scenarios
        # TODO: update getScenario function to the official implementation and traverse through available scenarios
        singleScenario = self.scenarios.getScenario()

        # Fill a default tab view with the newtork panel and pass a single scenario for handling



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
#        self.selectedMachine = scenario.getPOVMachines()[0]
        self.populateMachineInfo()
        self.machineInfo.ui.editButton.clicked.connect(self.editClicked)
        self.ui.machineInfoArea.addWidget(self.machineInfo, 0, 0, 1, 1)

        # /= Network View
        self.networkGraph = NetworkGraph()
        self.ui.graphArea.addWidget(self.networkGraph, 0, 0, 1, 1)

        # /= Component view

    # Call to populate the fields of the machine Info section with the info of the selected machine
    def populateMachineInfo(self):
#        self.machineInfo.ui.name.setText(self.selectedMachine.getFieldsToShow()["name"])
#        self.machineInfo.ui.os.setText(self.selectedMachine.getFieldsToShow()["os"])
        pass

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

