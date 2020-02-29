import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea, 
QFormLayout, QGroupBox, QLabel, QPushButton, QHBoxLayout, QLayoutItem, QAction, QDialog)
from PySide2.QtCore import (QFile, QDate)
from PySide2.QtGui import (QPixmap, QFont)
from Interfaces.ui_machineList import Ui_MachineList
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
    def __init__(self, machineJSON, index):
        super(QuickView, self).__init__()
        self.setFixedSize(300, 150)
        self.machineIndex = index

        self.mainHorizontalLayout = QHBoxLayout()
        self.VMInfoAndOptionsVerticalLayout = QVBoxLayout()

        self.setLogo(machineJSON["os"])

        #Decide which values will be displayed
        fieldsList = ["name", "os"]
        self.setFields(machineJSON, fieldsList)

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
        editVMButton.clicked.connect(self.editClicked)


        deleteVMButton = QPushButton("Delete")
        deleteVMButton.setMaximumWidth(50)
        deleteVMButton.clicked.connect(self.deleteClicked)

        editAndDeleteButtonsHorizLayout.addWidget(editVMButton)
        editAndDeleteButtonsHorizLayout.addWidget(deleteVMButton)

        #Add to left pane
        self.VMInfoAndOptionsVerticalLayout.addLayout(editAndDeleteButtonsHorizLayout)


    def setFields(self, machineJSON, fieldsList):
        #Create VM info
        VMFields = QFormLayout()
        for key in fieldsList:
            label = QLabel(f"{str(key).capitalize()}:")
            font = QFont()
            font.setBold(True)
            font.setPointSize(8)
            label.setFont(font)
            value = QLabel(str(machineJSON[key]))

            VMFields.addRow(label, value)

        self.VMInfoAndOptionsVerticalLayout.addLayout(VMFields) 

    def editClicked(self):
        print("edit clicked") 

    def deleteClicked(self):
        print("delete clicked") 


class MachineListDialog(QDialog):
    def __init__(self, JSON_Scenario):
        super(MachineListDialog, self).__init__()
        self.ui = Ui_MachineList()
        self.ui.setupUi(self)
        self.JSON_Scenario = json.loads(JSON_Scenario)

        #Get JSON from String
        self.setLabels()

        #setup QuickViews
        self.attackersLayout = QVBoxLayout()
        self.attackersScroll = self.getScrollArea()
        self.attackersScroll.setWidget(self.getQuickViewList(self.JSON_Scenario["machines"]))
        self.attackersLayout.addWidget(self.attackersScroll)


        self.victimsLayout = QVBoxLayout()
        self.victimsScroll = self.getScrollArea()
        self.victimsScroll.setWidget(self.getQuickViewList(self.JSON_Scenario["machines"]))
        self.victimsLayout.addWidget(self.victimsScroll)

        self.ui.horizontalLayout.addLayout(self.attackersLayout)
        self.ui.horizontalLayout.addLayout(self.victimsLayout)

        #setup buttons
        self.setButtons()

        # #set up save and cancel buttons
        self.ui.buttonBox.accepted.connect(self.onSaveClicked)
        self.ui.buttonBox.rejected.connect(self.onCancelClicked)

    
    def onSaveClicked(self):
        print("returned modified JSON")

    def onCancelClicked(self):
        print("return original JSON")


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


    def getQuickViewList(self, machines):
        verticalLayout = QVBoxLayout()
        groupBox = QGroupBox()

        for i in range(len(machines) - 1, -1, -1):
            verticalLayout.addWidget(QuickView(machines[i], i))#TODO pass callbacks 

        groupBox.setLayout(verticalLayout)
        return groupBox


    def setButtons(self):
        
        #create buttons
        addPOCButton = QPushButton("Add PoC VM")
        addVictimButton = QPushButton("Add Victim VM")

        #connect buttons to actions
        addPOCButton.clicked.connect(self.onAddPOC)
        addVictimButton.clicked.connect(self.onAddVictim)

        #add buttons to layout
        self.ui.horizontalLayout_3.addWidget(addPOCButton)
        self.ui.horizontalLayout_3.addWidget(addVictimButton)


    def onAddPOC(self):
        print("add POC clicked!!!")
        self.JSON_Scenario["machines"].append(genericMachine)
        self.attackersScroll.setWidget(self.getQuickViewList(self.JSON_Scenario["machines"]))

    def onAddVictim(self):
        print("add victim clicked!!!")
        self.JSON_Scenario["machines"].append(genericMachine)
        self.victimsScroll.setWidget(self.getQuickViewList(self.JSON_Scenario["machines"]))



if __name__ == "__main__":

    sample_scenario = '''{
    "scenario_name" : "name", 
    "id" : 123456789, 
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
        },
        {
        "os": "debian",
        "name": "victim",
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
    ],
    "network_settings" : {
            "network_type" : "type", 
            "network_name" : "Name", 
            "auto_config" : "True"
        }
    }'''

    app = QApplication(sys.argv)
    window = MachineListDialog(sample_scenario)
    window.show()
    sys.exit(app.exec_())