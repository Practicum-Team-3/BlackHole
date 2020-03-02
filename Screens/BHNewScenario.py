# This Python file uses the following encoding: utf-8
import sys
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Signal
from PySide2.QtWidgets import QDialog
from Screens.Interfaces.ui_newScenario import Ui_NewScenario

class BHNewScenario(QDialog):

    # == Declare signals here ==
    # They are the events that another class can subscribe to be notified of something
    # To actually trigger the event, call .emit()
    scenarioCreatedAction = Signal()
    scenarioCanceled = Signal()
    scenarioSaved = Signal()

    exploitAdded = Signal()
    exploitDeleted = Signal()
    vulProgAdded = Signal()
    vulProgDeleted = Signal()

    def __init__(self, scenario):
       super(BHNewScenario, self).__init__()

       self.ui = Ui_NewScenario()
       self.ui.setupUi(self)
       # self.ui.openScreenButton.clicked.connect(self.openSampleScreen)

       # == Fill in the fields with the values of the BHScenario passed (scenario) ==
       self.ui.scenarioName.setPlainText("SampleScenario")

       # == Connect the button actions to listeners ==
       self.ui.buttons.accepted.connect(self.acceptButtonPressed)
       self.ui.buttons.rejected.connect(self.rejectButtonPressed)
       #self.ui.buttons.accepted.connect(self.savedButtonPressed)
       #self.ui.addExploit.accepted.connect(self.addExploitButtonPressed)
       #self.ui.addVulProg.accepted.connect(self.addVulProgButtonPressed)
       #self.ui.delExploit.accepted.connect(self.delExploitButtonPressed)
       #self.ui.delVulProg.accepted.connect(self.delVulProgButtonPressed)


    @Slot()
    def acceptButtonPressed(self):
        # Do something, like emit a signal
        self.scenarioCreatedAction.emit()

    @Slot()
    def rejectButtonPressed():
        # Do something
        self.scenarioCanceled.emit()

    #@Slot()
    #def savedButtonPressed(self):
     #   self.scenarioSaved.emit()

#    @Slot()
 #   def addExploitButtonPressed(self):
  #      self.exploitAdded.emit()

   # @Slot()
    #def addVulProgButtonPressed(self):
     #    self.vulProgAdded.emit()

    #@Slot()
    #def delExploit(self):
     #    self.exploitDeleted.edmit()

    #@Slot()
    #def delVulProg(self):
    #    self.vulProgDeleted.edmit()
