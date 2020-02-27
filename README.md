# BlackHole
Front-end of the automated malware and exploit data collection tool

UI Designer files are located in Screens/Interfaces
  These are the files where drag and drop can be used to build the interfaces
  
  Current UI Designer files and their assignments are as follows:
  
  welcomeScreen.ui  - Freddye
  
  newScenario.ui    - Laura
  
  machineList.ui    - Daniel
  
  machineEdit.ui    - Manali
  
  machineSettings.ui - Aaron
  
  mainWindow.ui     - Jose
  
  
  
IMPORTANT:
  Every screen's UI is to be developed in a .ui designer file.
  Python code can be generated from these files using the command:
      pyside2-uic sampleName.ui > ui_sampleName.py
  
  The generated code is to get called from a BHSampleNameDialog class inside a corresponding .py file
  
Tip:
  Screens can make use of multiple .ui designer files to generate the interface
  (useful when the interface requires multiple instances of a similar group of items),
  code will be required on the corresponding BHSampleNameDialog class to preform the generation calls.
