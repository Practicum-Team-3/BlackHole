# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'machineInfo.ui'
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


class Ui_MachineInfo(object):
    def setupUi(self, MachineInfo):
        if MachineInfo.objectName():
            MachineInfo.setObjectName(u"MachineInfo")
        MachineInfo.setWindowModality(Qt.NonModal)
        MachineInfo.resize(209, 579)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MachineInfo.sizePolicy().hasHeightForWidth())
        MachineInfo.setSizePolicy(sizePolicy)
        MachineInfo.setAcceptDrops(False)
        MachineInfo.setAutoFillBackground(False)
        MachineInfo.setFrameShadow(QFrame.Plain)
        MachineInfo.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(MachineInfo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.infoFrame = QFrame(MachineInfo)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setMinimumSize(QSize(0, 200))
        self.infoFrame.setFrameShape(QFrame.NoFrame)
        self.infoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.infoFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.icon = QLabel(self.infoFrame)
        self.icon.setObjectName(u"icon")
        self.icon.setAutoFillBackground(False)
        self.icon.setStyleSheet(u"image: url(resources/imac.png) 0 0 0 0 stretch stretch;")
        self.icon.setFrameShape(QFrame.NoFrame)
        self.icon.setMargin(20)

        self.verticalLayout_3.addWidget(self.icon)

        self.frame = QFrame(self.infoFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_5)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_7)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_9)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_11)

        self.editButton = QPushButton(self.frame)
        self.editButton.setObjectName(u"editButton")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.editButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        palette = QPalette()
        brush = QBrush(QColor(169, 8, 4, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(148, 148, 148, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        self.pushButton_2.setPalette(palette)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(False)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.pushButton_2)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.infoFrame)

        self.collectorBox = QGroupBox(MachineInfo)
        self.collectorBox.setObjectName(u"collectorBox")
        sizePolicy1.setHeightForWidth(self.collectorBox.sizePolicy().hasHeightForWidth())
        self.collectorBox.setSizePolicy(sizePolicy1)
        self.collectorBox.setFlat(False)
        self.collectorBox.setCheckable(False)
        self.formLayout = QFormLayout(self.collectorBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.collectorBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.collectorBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_3 = QLabel(self.collectorBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_2 = QLineEdit(self.collectorBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)


        self.verticalLayout.addWidget(self.collectorBox)

        self.networkBox = QGroupBox(MachineInfo)
        self.networkBox.setObjectName(u"networkBox")
        sizePolicy1.setHeightForWidth(self.networkBox.sizePolicy().hasHeightForWidth())
        self.networkBox.setSizePolicy(sizePolicy1)
        self.networkBox.setFlat(False)
        self.networkBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.networkBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(self.networkBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.checkBox_3 = QCheckBox(self.networkBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.networkBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.networkBox)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.label = QLabel(self.networkBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.comboBox_2 = QComboBox(self.networkBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_2.addWidget(self.comboBox_2)

        self.label_12 = QLabel(self.networkBox)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.comboBox_3 = QComboBox(self.networkBox)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_2.addWidget(self.comboBox_3)


        self.verticalLayout.addWidget(self.networkBox)


        self.retranslateUi(MachineInfo)

        self.pushButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(MachineInfo)
    # setupUi

    def retranslateUi(self, MachineInfo):
        MachineInfo.setWindowTitle(QCoreApplication.translate("MachineInfo", u"Frame", None))
        self.icon.setText("")
        self.label_4.setText(QCoreApplication.translate("MachineInfo", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("MachineInfo", u"VM-B1", None))
        self.label_6.setText(QCoreApplication.translate("MachineInfo", u"OS", None))
        self.label_7.setText(QCoreApplication.translate("MachineInfo", u"Windows 10", None))
        self.label_8.setText(QCoreApplication.translate("MachineInfo", u"Vulnerability", None))
        self.label_9.setText(QCoreApplication.translate("MachineInfo", u"p0", None))
        self.label_10.setText(QCoreApplication.translate("MachineInfo", u"Collector", None))
        self.label_11.setText(QCoreApplication.translate("MachineInfo", u"ECELd", None))
        self.editButton.setText(QCoreApplication.translate("MachineInfo", u"Edit", None))
        self.pushButton_2.setText(QCoreApplication.translate("MachineInfo", u"Delete", None))
        self.collectorBox.setTitle(QCoreApplication.translate("MachineInfo", u"Network", None))
        self.label_2.setText(QCoreApplication.translate("MachineInfo", u"IP Address", None))
        self.label_3.setText(QCoreApplication.translate("MachineInfo", u"Port", None))
        self.networkBox.setTitle(QCoreApplication.translate("MachineInfo", u"Collector", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MachineInfo", u"ECELd", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MachineInfo", u"Garbage Collector", None))

        self.checkBox_3.setText(QCoreApplication.translate("MachineInfo", u"API Calls", None))
        self.checkBox_2.setText(QCoreApplication.translate("MachineInfo", u"System Logs", None))
        self.checkBox.setText(QCoreApplication.translate("MachineInfo", u"Network Traffic", None))
        self.label.setText(QCoreApplication.translate("MachineInfo", u"Start Condition", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MachineInfo", u"Total Eclipse", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MachineInfo", u"Eclipse Starts", None))

        self.label_12.setText(QCoreApplication.translate("MachineInfo", u"Stop Condition", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MachineInfo", u"Eclipse Ends", None))

    # retranslateUi

