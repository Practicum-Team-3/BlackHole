import sys
import json
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtCore import QFile
from Screens.Interfaces.ui_machineSettings import Ui_MachineSettings
from Screens.DataHandler.BHMachine import BHMachine

# will take a BHMachine instance
class MachineSettings(QDialog):
    def __init__(self, BHMachine):
        super(MachineSettings, self).__init__()
        self.machineObject = BHMachine
        self.ui = Ui_MachineSettings()
        self.ui.setupUi(self)

        # set machine state
        self.setState()

        self.ui.OverlayButtonBox.accepted.connect(self.okPressed)
        self.ui.OverlayButtonBox.rejected.connect(self.cancelPressed)
    
    # set the state of the machine when user first enters window
    def setState(self):
        self.ui.spinbox_baseMemory.setValue(self.machineObject.getBaseMemory())
        
        if (self.machineObject.getBootOrder_hardDisk() == "True"): # was in json as str
            self.ui.bootOrderCheckbox_hardDisk.setChecked(True)
        else:
            self.ui.bootOrderCheckbox_hardDisk.setChecked(False)

        if (self.machineObject.getBootOrder_optical() == "True"): # was in json as str
            self.ui.bootOrderCheckbox_optical.setChecked(True)
        else:
            self.ui.bootOrderCheckbox_optical.setChecked(False)
        
        if (self.machineObject.getBootOrder_floppy() == "True"): # was in json as str
            self.ui.bootOrderCheckBox_floppy.setChecked(True)
        else:
            self.ui.bootOrderCheckBox_floppy.setChecked(False)
        
        if (self.machineObject.getBootOrder_network() == "True"): # was in json as str
            self.ui.bootOrderCheckbox_network.setChecked(True)
        else:
            self.ui.bootOrderCheckbox_network.setChecked(False)
        

        self.ui.comboBox_chipset.setCurrentText(self.machineObject.getChipset())
        self.ui.comboBox_pointingDevice.setCurrentText(self.machineObject.getPointingDevice())

        if (self.machineObject.getExtFeat_enableIO() == "True"): # was in json as str
            self.ui.extFeatCheckbox_enableIO.setChecked(True)
        else:
            self.ui.extFeatCheckbox_enableIO.setChecked(False)
        
        if (self.machineObject.getExtFeat_enableEFI_network() == "True"): # was in json as str
            self.ui.extFeatCheckBox_enableEFI.setChecked(True)
        else:
            self.ui.extFeatCheckBox_enableEFI.setChecked(False)

        if (self.machineObject.getExtFeat_hwClockUTCtime() == "True"): # was in json as str
            self.ui.extFeatCheckbox_hwClockUTCtime.setChecked(True)
        else:
            self.ui.extFeatCheckbox_hwClockUTCtime.setChecked(False)

        self.ui.spinBox_processors.setValue(self.machineObject.getProcessors())
        self.ui.spinBox_executionCap.setValue(self.machineObject.getExeCap())

        if (self.machineObject.getExtFeat_enablePAE_NX() == "True"): # was in json as str
            self.ui.checkBox_enablePAEnx.setChecked(True)
        else:
            self.ui.checkBox_enablePAEnx.setChecked(False)

        self.ui.comboBox_paravirtInterface.setCurrentText(self.machineObject.getParavirtInterface())

        if (self.machineObject.getHdVirt_enableVTx() == "True"): # was in json as str
            self.ui.checkBox_enableVTxAMDV.setChecked(True)
        else:
            self.ui.checkBox_enableVTxAMDV.setChecked(False)

        if (self.machineObject.getHdVirt_enableNestedPaging() == "True"): # was in json as str
            self.ui.checkBox_enableNestedPaging.setChecked(True)
        else:
            self.ui.checkBox_enableNestedPaging.setChecked(False)

    # Save the state of machine settings back into machine object when ok is pressed
    def okPressed(self):       
        self.machineObject.setBaseMemory(self.ui.spinbox_baseMemory.value())

        if (self.ui.bootOrderCheckbox_hardDisk.isChecked() == True): # have to store back as string
            self.machineObject.setBootOrder_hardDisk("True")
        else:
            self.machineObject.setBootOrder_hardDisk("False")

        if (self.ui.bootOrderCheckbox_optical.isChecked() == True): # have to store back as string
            self.machineObject.setBootOrder_optical("True")
        else:
            self.machineObject.setBootOrder_optical("False")

        if (self.ui.bootOrderCheckBox_floppy.isChecked() == True): # have to store back as string
            self.machineObject.setBootOrder_floppy("True")
        else:
            self.machineObject.setBootOrder_floppy("False")

        if (self.ui.bootOrderCheckbox_network.isChecked() == True): # have to store back as string
            self.machineObject.setBootOrder_network("True")
        else:
            self.machineObject.setBootOrder_network("False")

        self.machineObject.setChipset(self.ui.comboBox_chipset.currentText())
        self.machineObject.setPointingDevice(self.ui.comboBox_pointingDevice.currentText())

        if (self.ui.extFeatCheckbox_enableIO.isChecked() == True): # have to store back as string
            self.machineObject.setExtFeat_enableIO("True")
        else:
            self.machineObject.setExtFeat_enableIO("False")

        if (self.ui.extFeatCheckBox_enableEFI.isChecked() == True): # have to store back as string
            self.machineObject.setExtFeat_enableEFI("True")
        else:
            self.machineObject.setExtFeat_enableEFI("False")

        if (self.ui.extFeatCheckbox_hwClockUTCtime.isChecked() == True): # have to store back as string
            self.machineObject.setExtFeat_hwClockUTCtime("True")
        else:
            self.machineObject.setExtFeat_hwClockUTCtime("False")

        self.machineObject.setProcessors(self.ui.spinBox_processors.value())
        self.machineObject.setExeCap(self.ui.spinBox_executionCap.value())

        if (self.ui.checkBox_enablePAEnx.isChecked() == True): # have to store back as string
            self.machineObject.setExtFeat_enablePAE_NX("True")
        else:
            self.machineObject.setExtFeat_enablePAE_NX("False")

        self.machineObject.setParavirtInterface(self.ui.comboBox_paravirtInterface.currentText())

        if (self.ui.checkBox_enableVTxAMDV.isChecked() == True): # have to store back as string
            self.machineObject.setHdVirt_enableVTx("True")
        else:
            self.machineObject.setHdVirt_enableVTx("False")

        if (self.ui.checkBox_enableNestedPaging.isChecked() == True): # have to store back as string
            self.machineObject.setHdVirt_enableNestedPaging("True")
        else:
            self.machineObject.setHdVirt_enableNestedPaging("False")

        print("OK pressed, exiting \"Machine Settings\" window.")
        

    # if cancel is pressed, do not change the machine state
    def cancelPressed(self):
        print("Cancel pressed, exiting \"Machine Settings\" window.")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     test = '''{
#             "os": "windows",
#             "name": "attacker1",
#             "id": 122,
#             "type": "pov",
#             "shared_folders": [],
#             "network_settings": [],
#             "provisions": [],
#             "baseMemory": 5,
#             "bootOrder_floppy": "False",
#             "bootOrder_optical": "False",
#             "bootOrder_hardDisk": "False",
#             "bootOrder_network": "False",
#             "chipset": "PIIX3",
#             "pointingDevice": "PS/2 Mouse",
#             "extFeat_enableIO": "False",
#             "extFeat_enableEFI": "False",
#             "extFeat_hwClockUTCtime": "False",
#             "processors": 3,
#             "exeCap": 99,
#             "extFeat_EnablePAE_NX": "False",
#             "paravirtInterface": "Default",
#             "hdVirt_enableVTx": "False",
#             "hdVirt_enableNestedPaging": "False"
#         }'''
#     jsonObject = json.loads(test)
#     testMachine = BHMachine()
#     testMachine.fromJSON(jsonObject)
#     window = MachineSettings(testMachine)
#     window.show()

#     sys.exit(app.exec_())