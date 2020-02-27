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


if __name__ == "__main__":
    # Main setup
    app = QApplication([])

    # Instantiate and show main window
    window = BHMainWindow()
    window.show()

    # Execute Qt
    sys.exit(app.exec_())
