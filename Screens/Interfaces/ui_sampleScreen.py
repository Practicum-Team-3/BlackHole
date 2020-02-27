# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sampleScreen.ui'
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


class Ui_SampleScreen(object):
    def setupUi(self, SampleScreen):
        if SampleScreen.objectName():
            SampleScreen.setObjectName(u"SampleScreen")
        SampleScreen.resize(378, 480)
        self.verticalLayout = QVBoxLayout(SampleScreen)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(SampleScreen)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nameField = QLineEdit(self.frame_2)
        self.nameField.setObjectName(u"nameField")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameField)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.nicknameField = QLineEdit(self.frame_2)
        self.nicknameField.setObjectName(u"nicknameField")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nicknameField)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.slider = QSlider(self.frame_2)
        self.slider.setObjectName(u"slider")
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.slider)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dateEdit)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBox)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(SampleScreen)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progress = QProgressBar(self.frame)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(24)

        self.horizontalLayout.addWidget(self.progress)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(SampleScreen)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Abort|QDialogButtonBox.Cancel|QDialogButtonBox.Discard)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SampleScreen)
        self.buttonBox.accepted.connect(SampleScreen.accept)
        self.buttonBox.rejected.connect(SampleScreen.reject)

        QMetaObject.connectSlotsByName(SampleScreen)
    # setupUi

    def retranslateUi(self, SampleScreen):
        SampleScreen.setWindowTitle(QCoreApplication.translate("SampleScreen", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SampleScreen", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("SampleScreen", u"Nickname", None))
        self.label_3.setText(QCoreApplication.translate("SampleScreen", u"Level", None))
        self.label_4.setText(QCoreApplication.translate("SampleScreen", u"Date", None))
        self.label_5.setText(QCoreApplication.translate("SampleScreen", u"Option", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("SampleScreen", u"First Option", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("SampleScreen", u"Second Option", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("SampleScreen", u"Third Option", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("SampleScreen", u"Pick something, will ya?", None))

    # retranslateUi

