import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QFrame
from PySide2.QtCore import Slot
from Screens.Interfaces.ui_mainWindow import Ui_MainWindow

from Screens.Interfaces.networkWindowInternals.ui_networkPanel import Ui_NetworkPanel
from Screens.Interfaces.networkWindowInternals.ui_machineInfo import Ui_MachineInfo
from Screens.Interfaces.networkWindowInternals.NetworkConfig.Graphics import NetworkGraph

# BHMainWindow
class BHMainWindow(QMainWindow):
    def __init__(self):
        super(BHMainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.defaultNetworkPanel = BHNetworkPanel()

        self.ui.gridLayoutTab.addWidget(self.defaultNetworkPanel, 0, 0, 1, 1)

# Single Tab
class BHNetworkPanel(QFrame):
    def __init__(self):
        super(BHNetworkPanel, self).__init__()

        self.ui = Ui_NetworkPanel()
        self.ui.setupUi(self)

        # === Add the parts to the sections ===

        # Machine info
        self.machineInfo = BHMachineInfo()
        self.ui.machineInfoArea.addWidget(self.machineInfo, 0, 0, 1, 1)

        # Network View
        self.networkGraph = NetworkGraph()
        self.ui.graphArea.addWidget(self.networkGraph, 0, 0, 1, 1)

        # Component view


# View that displays basic information from a machine
class BHMachineInfo(QFrame):
    def __init__(self):
        super(BHMachineInfo, self).__init__()

        self.ui = Ui_MachineInfo()
        self.ui.setupUi(self)

