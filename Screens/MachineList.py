import sys, os
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea, 
QFormLayout, QGroupBox, QLabel, QPushButton, QHBoxLayout, QLayoutItem, QAction, QDialog)
from PySide2.QtCore import (QFile, QDate, Signal, Slot, QObject)
from PySide2.QtGui import (QPixmap, QFont)
from Interfaces.ui_machineList import Ui_MachineList
from DataHandler.BHScenario import BHScenario #getPOVMachines()  ,  getVictimMachines()
from DataHandler.BHMachine import BHMachine
#from MachineEdit import MachineEdit
import json

logoPaths = {"windows":"Media\OSLogos\windows-logo.png", "debian":"Media\OSLogos\debian-logo.png"}

genericMachine = {
    "os": "windows",
    "name": "attacker",
    "shared_folders": [
        "./attackerfiles",
        "/sharedfolder"
    ],
    "network_settings": {
        "ip_address": "192.168.50.5",
        "network_type" : "type", 
        "network_name" : "Name", 
        "auto_config" : "True"
    },
    "provisions": [
        {
        "name": "installE0",
        "commands": [
        [
            "shell",
            "./../../sharedfolder/e0.sh"
        ]
        ]
    }]
}

#VM Quick View Widget
class QuickView(QWidget):
    def __init__(self, BHMachine, indexOnList):
        super(QuickView, self).__init__()
        self.setFixedSize(300, 150)
        self.machine = BHMachine
        self.listIndex = indexOnList
        self.mainHorizontalLayout = QHBoxLayout()
        self.VMInfoAndOptionsVerticalLayout = QVBoxLayout()

        self.setLogo(BHMachine.getOS())

        #Decide which values will be displayed
        self.setFields(BHMachine.getFieldsToShow())

        self.signalObject = QObject()
        self.signalObject.editButtonClickedSignal = Signal(BHMachine)
        self.signalObject.deleteButtonClickedSignal = Signal(bool, int)

        #set buttons
        self.setButtons()

        #add to main layout
        self.mainHorizontalLayout.addLayout(self.VMInfoAndOptionsVerticalLayout)
        self.setLayout(self.mainHorizontalLayout)


    def setLogo(self, osName):
        #Add VM image to right pane
        logoPath = logoPaths[str(osName).lower()]
        VMLogo = QPixmap(logoPath)
        VMLogo = VMLogo.scaledToHeight(100)
        VMLogo = VMLogo.scaledToWidth(100)
        sampleLabel = QLabel()
        sampleLabel.setPixmap(VMLogo)
        sampleLabel.setMinimumSize(100, 100)
        sampleLabel.setMaximumSize(100, 100)

        self.mainHorizontalLayout.addWidget(sampleLabel)


    def setButtons(self):
        #Create edit-delete buttons
        editAndDeleteButtonsHorizLayout = QHBoxLayout()
        editVMButton = QPushButton("Edit")
        editVMButton.setMaximumWidth(50)
        editVMButton.clicked.connect(self.editVMButtonClicked)#(self.machine.isVictim(), self.listIndex)

        deleteVMButton = QPushButton("Delete")
        deleteVMButton.setMaximumWidth(50)
        deleteVMButton.clicked.connect(self.deleteVMButtonClicked)#(self.machine.isVictim(), self.listIndex)

        editAndDeleteButtonsHorizLayout.addWidget(editVMButton)
        editAndDeleteButtonsHorizLayout.addWidget(deleteVMButton)

        #Add to left pane
        self.VMInfoAndOptionsVerticalLayout.addLayout(editAndDeleteButtonsHorizLayout)


    def setFields(self, fieldsList):
        #Create VM info
        VMFields = QFormLayout()
        for key, val in fieldsList.items():
            label = QLabel(f"{str(key).capitalize()}:")
            font = QFont()
            font.setBold(True)
            font.setPointSize(8)
            label.setFont(font)
            value = QLabel(str(val))

            VMFields.addRow(label, value)

        self.VMInfoAndOptionsVerticalLayout.addLayout(VMFields)


    def editVMButtonClicked(self):
        self.signalObject.emit(self.machine)

    def deleteVMButtonClicked(self):
        self.signalObject.emit(self.machine.isVictim(), self.machine.getMachineID())


class MachineListDialog(QDialog):
    def __init__(self, BHScenario):
        super(MachineListDialog, self).__init__()
        self.ui = Ui_MachineList()
        self.ui.setupUi(self)
        self.scenario = BHScenario
        self.placeholderMachine = None

        #Get JSON from String
        self.setLabels()

        #setup QuickViews
        self.updatePOVs(self.scenario)
        self.updateVictims(self.scenario)

        #create buttons
        createVMButton = QPushButton("Create VM")
        #connect buttons to actions
        createVMButton.clicked.connect(self.onCreateVMButtonClicked)
        #add buttons to layout
        self.ui.horizontalLayout_3.addWidget(createVMButton)

        #set up save and cancel buttons
        # self.ui.buttonBox.accepted.connect(self.onSaveClicked)
        # self.ui.buttonBox.rejected.connect(self.onCancelClicked)

    def updatePOVs(self, BHScenario):
        self.attackersLayout = QVBoxLayout()
        self.attackersScroll = self.getScrollArea()
        self.attackersScroll.setWidget(self.getQuickViewList(BHScenario.getPOVMachines()))
        self.attackersLayout.addWidget(self.attackersScroll)
        self.ui.horizontalLayout.addLayout(self.attackersLayout)


    def updateVictims(self, BHScenario):
        self.victimsLayout = QVBoxLayout()
        self.victimsScroll = self.getScrollArea()
        self.victimsScroll.setWidget(self.getQuickViewList(BHScenario.getVictimMachines()))
        self.victimsLayout.addWidget(self.victimsScroll)
        self.ui.horizontalLayout.addLayout(self.victimsLayout)

    def setLabels(self):
        PoCLabel = QLabel("PoCs")
        victimLabel = QLabel("Victims")
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)
        PoCLabel.setFont(font)
        victimLabel.setFont(font)
        self.ui.horizontalLayout_2.addWidget(PoCLabel)
        self.ui.horizontalLayout_2.addWidget(victimLabel)

    def getScrollArea(self):
        #setup PoC quickviews
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setFixedHeight(291)
        return scrollArea


    def getQuickViewList(self, BHMachinesList):
        verticalLayout = QVBoxLayout()
        groupBox = QGroupBox()
        for i in range(len(BHMachinesList) - 1, -1, -1):
            quickView = QuickView(BHMachinesList[i], i)
            verticalLayout.addWidget(quickView)
        groupBox.setLayout(verticalLayout)
        return groupBox


    def onCreateVMButtonClicked(self):
        self.placeholderMachine = BHMachine()
        #TODO
        # machineEditWindow = MachineEdit(self.placeholderMachine)
        # machineEditWindow.onOKAction.connect(self.createVM)
        print(f"create machine clicked")


    @Slot(bool, int)
    def onDeleteVM(self, isVictim, machineID):
        if isVictim:
            self.scenario.deleteVictimMachine(machineID)
            self.updateVictims(self.scenario)
        else:
            self.scenario.deletePOVMachine(machineID)
            self.updatePOVs(self.scenario)
        print(f"delete clicked from {isVictim} machine {machineID}")
    
    @Slot(BHMachine)
    def onEditVMButtonClicked(self, BHMachine):
        self.placeholderMachine = BHMachine
        #TODO
        # machineEditWindow = MachineEdit(self.placeholderMachine)
        # machineEditWindow.onOKAction.connect(self.replaceMachine)
        print(f"edit clicked from machine {BHMachine.getMachineID()}")

    @Slot()
    def replaceMachine(self):
        self.scenario.replaceMachine(self.placeholderMachine.getMachineID(), self.placeholderMachine, self.placeholderMachine.isVictim())
        if self.placeholderMachine.isVictim():
            self.updateVictims(self.scenario)
        else:
            self.updatePOVs(self.scenario)


    @Slot()
    def createVM(self):
        self.scenario.addMachine(self.placeholderMachine)
        if self.placeholderMachine.isVictim():
            self.updateVictims(self.scenario)
        else:
            self.updatePOVs(self.scenario)


    def onSaveClicked(self):
        print("returned modified JSON")

    def onCancelClicked(self):
        print("return original JSON")



if __name__ == "__main__":

    sample_scenario = '''{
    "scenario_name" : "name", 
    "id" : 123, 
    "creation_date" : "string", 
    "last_accessed" : "string", 
    "exploit_info": {
            "name": "Name", 
            "download_link": "link", 
            "type": "type"
        }, 
    "vulnerability_info": {
            "name": "Name", 
            "cve_link": "url", 
            "download_link": "link", 
            "type": "type"
        }, 
    "machines": [
        {
            "os": "windows",
            "name": "attacker1",
            "id": 123,
            "type": "pov",
            "shared_folders": [],
            "network_settings": [],
            "provisions": []
        },
        {
            "os": "debian",
            "name": "victim1",
            "id": 124,
            "type": "victim",
            "shared_folders": [],
            "network_settings": [],
            "provisions": []
        }
    ],
    "network_settings" : {
            "network_type" : "type", 
            "network_name" : "Name", 
            "auto_config" : "True"
        }
    }'''

    testScenario = BHScenario()
    JSONScenario = json.loads(sample_scenario)
    testScenario.fromJSON(JSONScenario)
    
    app = QApplication(sys.argv)
    window = MachineListDialog(testScenario)
    window.show()
    sys.exit(app.exec_())