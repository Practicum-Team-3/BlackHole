# This class makes use of the code generated by PySide2 to generate it's interface.
# Once the interface is drawn, additional code can be written to fill fields in,
# adjust default values, or connect signals (events) to slots (listeners)

from PySide2 import QtWidgets
from PySide2.QtCore import Slot, QDate
from PySide2.QtWidgets import QDialog
from Screens.Interfaces.ui_machineEdit import Ui_MachineEdit

class BHMachineEditDialog(QDialog):
    def __init__(self):
        super(BHMachineEditDialog, self).__init__()

        # Instantiate the ui design class generated by pyside2-uic
        # pyside2-uic sampleScreen.ui > ui_sampleScreen.py
        # remember to re-run the command on the shell after making changes to the .ui file
        self.ui = Ui_MachineEdit()

        # Call setupUi to generate interface
        self.ui.setupUi(self)
