import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtCore import Slot
from Screens.Interfaces.ui_mainWindow import Ui_MainWindow

# Import for the screen to open upon the button press
from Screens.BHSampleScreenDialog import BHSampleScreenDialog

# BHMainWindow
class BHMainWindow(QMainWindow):
    def __init__(self):
        super(BHMainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Connect clicked event to the listener function
        self.ui.openScreenButton.clicked.connect(self.openSampleScreen)

    @Slot()
    def openSampleScreen(self):

        # Change class so the "Open Screen" button opens different one
        # don't forget to also adjust the imports
        self.screenToShow = BHSampleScreenDialog()
        self.screenToShow.show()
