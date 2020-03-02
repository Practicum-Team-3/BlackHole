import sys, os
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea, 
QFormLayout, QGroupBox, QLabel, QPushButton, QHBoxLayout, QLayoutItem, QAction, QDialog, QLayout)
from PySide2.QtCore import (QFile, QDate, Slot, QObject, Signal)
from PySide2.QtGui import (QPixmap, QFont)
from Screens.Interfaces.ui_machineList import Ui_MachineList
from Screens.DataHandler.BHScenario import BHScenario #getPOVMachines()  ,  getVictimMachines()
from Screens.DataHandler.BHMachine import BHMachine

from Screens.MachineSettings import MachineSettings
from Screens.BHMachineEditDialog import BHMachineEditDialog

#from MachineEdit import MachineEdit
import json

logoPaths = {"windows":"Screens/Media/OSLogos/windows-logo.png", "debian":"Screens/Media/OSLogos/debian-logo.png"}

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

# #VM Quick View Widget
# class QuickView(QWidget):
#     # class EditSignalObject(QObject):
#     #     editButtonClickedSignal = Signal(BHMachine)

#     # class DeleteSignalObject(QObject):
#     #     deleteButtonClickedSignal = Signal(bool, int)

#     def __init__(self, BHMachine, indexOnList):
#         super(QuickView, self).__init__()
#         self.setFixedSize(300, 150)
#         self.machine = BHMachine
#         self.listIndex = indexOnList
#         self.mainHorizontalLayout = QHBoxLayout()
#         self.VMInfoAndOptionsVerticalLayout = QVBoxLayout()

#         self.setLogo(BHMachine.getOS())

#         #Decide which values will be displayed
#         self.setFields(BHMachine.getFieldsToShow())

#         #instantiate signal object
#         # self.editSignalObject = self.EditSignalObject()
#         # self.deleteSignalObject = self.DeleteSignalObject()

#         #set buttons
#         self.setButtons()

#         #add to main layout
#         self.mainHorizontalLayout.addLayout(self.VMInfoAndOptionsVerticalLayout)
#         self.setLayout(self.mainHorizontalLayout)


#     def setLogo(self, osName):
#         #Add VM image to right pane
#         logoPath = logoPaths[str(osName).lower()]
#         VMLogo = QPixmap(logoPath)
#         VMLogo = VMLogo.scaledToHeight(100)
#         VMLogo = VMLogo.scaledToWidth(100)
#         sampleLabel = QLabel()
#         sampleLabel.setPixmap(VMLogo)
#         sampleLabel.setMinimumSize(100, 100)
#         sampleLabel.setMaximumSize(100, 100)

#         self.mainHorizontalLayout.addWidget(sampleLabel)


#     def setButtons(self):
#         #Create edit-delete buttons
#         editAndDeleteButtonsHorizLayout = QHBoxLayout()
#         editVMButton = QPushButton("Edit")
#         editVMButton.setMaximumWidth(50)
#         editVMButton.clicked.connect(self.editVMButtonClicked)#(self.machine.isVictim(), self.listIndex)

#         deleteVMButton = QPushButton("Delete")
#         deleteVMButton.setMaximumWidth(50)
#         deleteVMButton.clicked.connect(self.deleteVMButtonClicked)#(self.machine.isVictim(), self.listIndex)

#         editAndDeleteButtonsHorizLayout.addWidget(editVMButton)
#         editAndDeleteButtonsHorizLayout.addWidget(deleteVMButton)

#         #Add to left pane
#         self.VMInfoAndOptionsVerticalLayout.addLayout(editAndDeleteButtonsHorizLayout)


#     def setFields(self, fieldsList):
#         #Create VM info
#         VMFields = QFormLayout()
#         for key, val in fieldsList.items():
#             label = QLabel(f"{str(key).capitalize()}:")
#             font = QFont()
#             font.setBold(True)
#             font.setPointSize(8)
#             label.setFont(font)
#             value = QLabel(str(val))

#             VMFields.addRow(label, value)

#         self.VMInfoAndOptionsVerticalLayout.addLayout(VMFields)


#     def editVMButtonClicked(self):
#         self.editSignalObject.editButtonClickedSignal.emit(self.machine)

#     def deleteVMButtonClicked(self):
#         self.deleteSignalObject.deleteButtonClickedSignal.emit(self.machine.isVictim(), self.machine.getMachineID())


class MachineListDialog(QDialog):
    def __init__(self, BHScenario):
        super(MachineListDialog, self).__init__()
        self.ui = Ui_MachineList()
        self.ui.setupUi(self)
        self.scenario = BHScenario
        self.placeholderMachine = None

        self.buttonGroupList = []

        #Get JSON from String
        self.setLabels()

        #setup QuickViews
        self.attackersLayout = QVBoxLayout()
        self.attackersScroll = self.getScrollArea()
        self.updatePOVs()
        self.attackersLayout.addWidget(self.attackersScroll)
        self.ui.horizontalLayout.addLayout(self.attackersLayout)


        self.victimsLayout = QVBoxLayout()
        self.victimsScroll = self.getScrollArea()
        self.updateVictims()
        self.victimsLayout.addWidget(self.victimsScroll)
        self.ui.horizontalLayout.addLayout(self.victimsLayout)

        #create buttons
        createVMButton = QPushButton("Create VM")
        #connect buttons to actions
        createVMButton.clicked.connect(self.onCreateVMButtonClicked)
        #add buttons to layout
        self.ui.horizontalLayout_3.addWidget(createVMButton)

        #set save and cancel buttons
        # self.ui.buttonBox.accepted.connect(self.onSaveClicked)
        # self.ui.buttonBox.rejected.connect(self.onCancelClicked)

    def updatePOVs(self):
        self.attackersScroll.setWidget(self.getQuickViewList(self.scenario.getPOVMachines()))


    def updateVictims(self):
        self.victimsScroll.setWidget(self.getQuickViewList(self.scenario.getVictimMachines()))


    def setLabels(self):
        PoCLabel = QLabel("PoVs")
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
            quickViewWidget = self.addQuickView(BHMachinesList[i], i)
            verticalLayout.addWidget(quickViewWidget)
        groupBox.setLayout(verticalLayout)
        return groupBox


    def onCreateVMButtonClicked(self):
        self.placeholderMachine = BHMachine()
        #TODO
        machineEditWindow = BHMachineEditDialog(self.placeholderMachine)
        machineEditWindow.saveSignal.connect(self.createVM)
        

    @Slot()
    def createVM(self):
        self.scenario.addMachine(self.placeholderMachine)
        if self.placeholderMachine.isVictim():
            self.updateVictims()
        else:
            self.updatePOVs()

    @Slot()
    def replaceMachine(self):
        self.scenario.replaceMachine(self.placeholderMachine.getMachineID(), self.placeholderMachine, self.placeholderMachine.isVictim())
        if self.placeholderMachine.isVictim():
            self.updateVictims()
        else:
            self.updatePOVs()


    def onSaveClicked(self):
        print("Start Jose's window...")
        self.accept()

    def onCancelClicked(self):
        print("Go back to Freddye's window...")
        self.reject()



    #QUICKVIEW functions
    def addQuickView(self, BHMachine, MachineID):
        mainHorizontalLayout = QHBoxLayout()
        widget = QWidget()
        widget.setFixedSize(300, 150)
        VMInfoAndOptionsVerticalLayout = QVBoxLayout()
        mainHorizontalLayout.addWidget(self.getLogo(BHMachine.getOS()))
        VMInfoAndOptionsVerticalLayout.addLayout(self.getMachineFields(BHMachine.getFieldsToShow()))

        editAndDeleteButtonsHorizLayout = QHBoxLayout()

        #Create edit-delete buttons
        editVMButton = QPushButton("Edit")
        editVMButton.setMaximumWidth(50)

        deleteVMButton = QPushButton("Delete")
        deleteVMButton.setMaximumWidth(50)

        buttonGroup = self.ButtonGroup(self, len(self.buttonGroupList),BHMachine)

        deleteVMButton.clicked.connect(buttonGroup.onDeleteVM)
        editVMButton.clicked.connect(buttonGroup.onEditVMButtonClicked)

        self.buttonGroupList.append(buttonGroup)

        editAndDeleteButtonsHorizLayout.addWidget(editVMButton)
        editAndDeleteButtonsHorizLayout.addWidget(deleteVMButton)

        #Add to left pane
        VMInfoAndOptionsVerticalLayout.addLayout(editAndDeleteButtonsHorizLayout)
        mainHorizontalLayout.addLayout(VMInfoAndOptionsVerticalLayout)
        widget.setLayout(mainHorizontalLayout)
        return widget


    def getLogo(self, osName):
        #Add VM image to right pane
        logoPath = logoPaths[str(osName).lower()]
        VMLogo = QPixmap(logoPath)
        VMLogo = VMLogo.scaledToHeight(100)
        VMLogo = VMLogo.scaledToWidth(100)
        sampleLabel = QLabel()
        sampleLabel.setPixmap(VMLogo)
        sampleLabel.setMinimumSize(100, 100)
        sampleLabel.setMaximumSize(100, 100)
        return sampleLabel


    def getMachineFields(self, fieldsList):
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

        return VMFields

    
    class ButtonGroup():
        def __init__(self, parent, index, BHMachine):
            self.parent = parent
            self.machine = BHMachine
            self.index = index

        @Slot()
        def onDeleteVM(self):
            if self.machine.isVictim():
                self.parent.scenario.deleteVictimMachine(self.machine.getMachineID())
                self.parent.updateVictims()
            else:
                self.parent.scenario.deletePOVMachine(self.machine.getMachineID())
                self.parent.updatePOVs()
            self.parent.buttonGroupList.pop(self.index)
            print("Deleted")
        
        @Slot()
        def onEditVMButtonClicked(self):
            self.parent.placeholderMachine = self.machine
            #TODO
            self.machineEditWindow = BHMachineEditDialog(self.parent.placeholderMachine)
            self.machineEditWindow.saveSignal.connect(self.parent.replaceMachine)
            print("Manali?")
            self.machineEditWindow.show()



# if __name__ == "__main__":

#     sample_scenario = '''{
#     "scenario_name" : "name", 
#     "id" : 123, 
#     "creation_date" : "string", 
#     "last_accessed" : "string", 
#     "exploit_info": {
#             "name": "Name", 
#             "download_link": "link", 
#             "type": "type"
#         }, 
#     "vulnerability_info": {
#             "name": "Name", 
#             "cve_link": "url", 
#             "download_link": "link", 
#             "type": "type"
#         }, 
#     "machines": [],
#     "network_settings" : {
#             "network_type" : "type", 
#             "network_name" : "Name", 
#             "auto_config" : "True"
#         }
#     }'''

#     testScenario = BHScenario()
#     JSONScenario = json.loads(sample_scenario)
#     testScenario.fromJSON(JSONScenario)
    
#     app = QApplication(sys.argv)
#     window = MachineListDialog(testScenario)
#     window.show()
#     sys.exit(app.exec_())
