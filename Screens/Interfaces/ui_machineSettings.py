# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'machineSettings.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MachineSettings(object):
    def setupUi(self, MachineSettings):
        if MachineSettings.objectName():
            MachineSettings.setObjectName(u"MachineSettings")
        MachineSettings.resize(400, 604)
        MachineSettings.setModal(True)
        self.gridLayout_2 = QGridLayout(MachineSettings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_Processor = QGroupBox(MachineSettings)
        self.groupBox_Processor.setObjectName(u"groupBox_Processor")
        self.gridLayout_3 = QGridLayout(self.groupBox_Processor)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.groupBox_Processor)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.spinBox_processors = QSpinBox(self.groupBox_Processor)
        self.spinBox_processors.setObjectName(u"spinBox_processors")
        self.spinBox_processors.setMinimum(1)
        self.spinBox_processors.setMaximum(4)

        self.gridLayout_3.addWidget(self.spinBox_processors, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_Processor)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.spinBox_executionCap = QSpinBox(self.groupBox_Processor)
        self.spinBox_executionCap.setObjectName(u"spinBox_executionCap")
        self.spinBox_executionCap.setMinimum(1)
        self.spinBox_executionCap.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_executionCap, 1, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_Processor)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 1, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_Processor)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.checkBox_enablePAEnx = QCheckBox(self.groupBox_Processor)
        self.checkBox_enablePAEnx.setObjectName(u"checkBox_enablePAEnx")

        self.gridLayout_3.addWidget(self.checkBox_enablePAEnx, 2, 1, 1, 2)

        self.label_13 = QLabel(self.groupBox_Processor)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_Processor, 1, 0, 1, 1)

        self.groupBox_Acceleration = QGroupBox(MachineSettings)
        self.groupBox_Acceleration.setObjectName(u"groupBox_Acceleration")
        self.gridLayout_4 = QGridLayout(self.groupBox_Acceleration)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_9 = QLabel(self.groupBox_Acceleration)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.comboBox_paravirtInterface = QComboBox(self.groupBox_Acceleration)
        self.comboBox_paravirtInterface.addItem("")
        self.comboBox_paravirtInterface.addItem("")
        self.comboBox_paravirtInterface.addItem("")
        self.comboBox_paravirtInterface.addItem("")
        self.comboBox_paravirtInterface.addItem("")
        self.comboBox_paravirtInterface.addItem("")
        self.comboBox_paravirtInterface.setObjectName(u"comboBox_paravirtInterface")

        self.gridLayout_4.addWidget(self.comboBox_paravirtInterface, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_Acceleration)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)

        self.checkBox_enableVTxAMDV = QCheckBox(self.groupBox_Acceleration)
        self.checkBox_enableVTxAMDV.setObjectName(u"checkBox_enableVTxAMDV")

        self.gridLayout_4.addWidget(self.checkBox_enableVTxAMDV, 1, 1, 1, 1)

        self.checkBox_enableNestedPaging = QCheckBox(self.groupBox_Acceleration)
        self.checkBox_enableNestedPaging.setObjectName(u"checkBox_enableNestedPaging")

        self.gridLayout_4.addWidget(self.checkBox_enableNestedPaging, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_Acceleration, 2, 0, 1, 1)

        self.OverlayButtonBox = QDialogButtonBox(MachineSettings)
        self.OverlayButtonBox.setObjectName(u"OverlayButtonBox")
        self.OverlayButtonBox.setOrientation(Qt.Horizontal)
        self.OverlayButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.OverlayButtonBox, 3, 0, 1, 1)

        self.groupBox_Motherboard = QGroupBox(MachineSettings)
        self.groupBox_Motherboard.setObjectName(u"groupBox_Motherboard")
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_Motherboard.setFont(font)
        self.groupBox_Motherboard.setFlat(False)
        self.groupBox_Motherboard.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox_Motherboard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.extFeatCheckBox_enableEFI = QCheckBox(self.groupBox_Motherboard)
        self.extFeatCheckBox_enableEFI.setObjectName(u"extFeatCheckBox_enableEFI")

        self.gridLayout.addWidget(self.extFeatCheckBox_enableEFI, 9, 1, 1, 2)

        self.label_2 = QLabel(self.groupBox_Motherboard)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox_Motherboard)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_Motherboard)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.comboBox_chipset = QComboBox(self.groupBox_Motherboard)
        self.comboBox_chipset.addItem("")
        self.comboBox_chipset.addItem("")
        self.comboBox_chipset.setObjectName(u"comboBox_chipset")

        self.gridLayout.addWidget(self.comboBox_chipset, 6, 1, 1, 2)

        self.label_11 = QLabel(self.groupBox_Motherboard)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 1)

        self.extFeatCheckbox_enableIO = QCheckBox(self.groupBox_Motherboard)
        self.extFeatCheckbox_enableIO.setObjectName(u"extFeatCheckbox_enableIO")

        self.gridLayout.addWidget(self.extFeatCheckbox_enableIO, 8, 1, 1, 2)

        self.label_5 = QLabel(self.groupBox_Motherboard)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.comboBox_pointingDevice = QComboBox(self.groupBox_Motherboard)
        self.comboBox_pointingDevice.addItem("")
        self.comboBox_pointingDevice.addItem("")
        self.comboBox_pointingDevice.addItem("")
        self.comboBox_pointingDevice.setObjectName(u"comboBox_pointingDevice")

        self.gridLayout.addWidget(self.comboBox_pointingDevice, 7, 1, 1, 2)

        self.bootOrderCheckbox_network = QCheckBox(self.groupBox_Motherboard)
        self.bootOrderCheckbox_network.setObjectName(u"bootOrderCheckbox_network")

        self.gridLayout.addWidget(self.bootOrderCheckbox_network, 5, 1, 1, 2)

        self.bootOrderCheckbox_optical = QCheckBox(self.groupBox_Motherboard)
        self.bootOrderCheckbox_optical.setObjectName(u"bootOrderCheckbox_optical")

        self.gridLayout.addWidget(self.bootOrderCheckbox_optical, 2, 1, 1, 2)

        self.spinbox_baseMemory = QSpinBox(self.groupBox_Motherboard)
        self.spinbox_baseMemory.setObjectName(u"spinbox_baseMemory")
        self.spinbox_baseMemory.setProperty("showGroupSeparator", True)
        self.spinbox_baseMemory.setMinimum(4)
        self.spinbox_baseMemory.setMaximum(8192)

        self.gridLayout.addWidget(self.spinbox_baseMemory, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_Motherboard)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.extFeatCheckbox_hwClockUTCtime = QCheckBox(self.groupBox_Motherboard)
        self.extFeatCheckbox_hwClockUTCtime.setObjectName(u"extFeatCheckbox_hwClockUTCtime")

        self.gridLayout.addWidget(self.extFeatCheckbox_hwClockUTCtime, 10, 1, 1, 2)

        self.bootOrderCheckBox_floppy = QCheckBox(self.groupBox_Motherboard)
        self.bootOrderCheckBox_floppy.setObjectName(u"bootOrderCheckBox_floppy")

        self.gridLayout.addWidget(self.bootOrderCheckBox_floppy, 4, 1, 1, 1)

        self.bootOrderCheckbox_hardDisk = QCheckBox(self.groupBox_Motherboard)
        self.bootOrderCheckbox_hardDisk.setObjectName(u"bootOrderCheckbox_hardDisk")

        self.gridLayout.addWidget(self.bootOrderCheckbox_hardDisk, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_Motherboard, 0, 0, 1, 1)


        self.retranslateUi(MachineSettings)
        self.OverlayButtonBox.accepted.connect(MachineSettings.accept)
        self.OverlayButtonBox.rejected.connect(MachineSettings.reject)

        QMetaObject.connectSlotsByName(MachineSettings)
    # setupUi

    def retranslateUi(self, MachineSettings):
        MachineSettings.setWindowTitle(QCoreApplication.translate("MachineSettings", u"Machine Settings", None))
        self.groupBox_Processor.setTitle(QCoreApplication.translate("MachineSettings", u"Processor", None))
        self.label_6.setText(QCoreApplication.translate("MachineSettings", u"Processor(s):", None))
        self.label_7.setText(QCoreApplication.translate("MachineSettings", u"Execution Cap:", None))
        self.label_12.setText(QCoreApplication.translate("MachineSettings", u"(1% - 100%)", None))
        self.label_8.setText(QCoreApplication.translate("MachineSettings", u"Extended Features:", None))
        self.checkBox_enablePAEnx.setText(QCoreApplication.translate("MachineSettings", u"Enable PAE/NX", None))
        self.label_13.setText(QCoreApplication.translate("MachineSettings", u"(1 CPU - 4 CPUs)", None))
        self.groupBox_Acceleration.setTitle(QCoreApplication.translate("MachineSettings", u"Acceleration", None))
        self.label_9.setText(QCoreApplication.translate("MachineSettings", u"Paravirtualization Interface:", None))
        self.comboBox_paravirtInterface.setItemText(0, QCoreApplication.translate("MachineSettings", u"None", None))
        self.comboBox_paravirtInterface.setItemText(1, QCoreApplication.translate("MachineSettings", u"Default", None))
        self.comboBox_paravirtInterface.setItemText(2, QCoreApplication.translate("MachineSettings", u"Legacy", None))
        self.comboBox_paravirtInterface.setItemText(3, QCoreApplication.translate("MachineSettings", u"Minimal", None))
        self.comboBox_paravirtInterface.setItemText(4, QCoreApplication.translate("MachineSettings", u"Hyper-V", None))
        self.comboBox_paravirtInterface.setItemText(5, QCoreApplication.translate("MachineSettings", u"KVM", None))

        self.label_10.setText(QCoreApplication.translate("MachineSettings", u"Hardware Virtualization:", None))
        self.checkBox_enableVTxAMDV.setText(QCoreApplication.translate("MachineSettings", u"Enable VT-x/AMD-V", None))
        self.checkBox_enableNestedPaging.setText(QCoreApplication.translate("MachineSettings", u"Enable Nested Paging", None))
        self.groupBox_Motherboard.setTitle(QCoreApplication.translate("MachineSettings", u"Motherboard", None))
        self.extFeatCheckBox_enableEFI.setText(QCoreApplication.translate("MachineSettings", u"Enable EFI (special OSes only)", None))
        self.label_2.setText(QCoreApplication.translate("MachineSettings", u"Boot Order", None))
        self.label.setText(QCoreApplication.translate("MachineSettings", u"Base Memory", None))
        self.label_4.setText(QCoreApplication.translate("MachineSettings", u"Pointing Device", None))
        self.comboBox_chipset.setItemText(0, QCoreApplication.translate("MachineSettings", u"PIIX3", None))
        self.comboBox_chipset.setItemText(1, QCoreApplication.translate("MachineSettings", u"ICH9", None))

        self.label_11.setText(QCoreApplication.translate("MachineSettings", u"(4MB - 8192 MB)", None))
        self.extFeatCheckbox_enableIO.setText(QCoreApplication.translate("MachineSettings", u"Enable I/O APIC", None))
        self.label_5.setText(QCoreApplication.translate("MachineSettings", u"Extended Features", None))
        self.comboBox_pointingDevice.setItemText(0, QCoreApplication.translate("MachineSettings", u"PS/2 Mouse", None))
        self.comboBox_pointingDevice.setItemText(1, QCoreApplication.translate("MachineSettings", u"USB Tablet", None))
        self.comboBox_pointingDevice.setItemText(2, QCoreApplication.translate("MachineSettings", u"USB Multi-Touch Tablet", None))

        self.bootOrderCheckbox_network.setText(QCoreApplication.translate("MachineSettings", u"Network", None))
        self.bootOrderCheckbox_optical.setText(QCoreApplication.translate("MachineSettings", u"Optical", None))
        self.label_3.setText(QCoreApplication.translate("MachineSettings", u"Chipset", None))
        self.extFeatCheckbox_hwClockUTCtime.setText(QCoreApplication.translate("MachineSettings", u"Hardware Clock in UTC Time", None))
        self.bootOrderCheckBox_floppy.setText(QCoreApplication.translate("MachineSettings", u"Floppy", None))
        self.bootOrderCheckbox_hardDisk.setText(QCoreApplication.translate("MachineSettings", u"Hard Disk", None))
    # retranslateUi

