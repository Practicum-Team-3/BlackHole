# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'machineEdit.ui'
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


class Ui_MachineEdit(object):
    def setupUi(self, MachineEdit):
        if MachineEdit.objectName():
            MachineEdit.setObjectName(u"MachineEdit")
        MachineEdit.resize(400, 470)
        self.label = QLabel(MachineEdit)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-160, 230, 47, 13))
        self.browse1 = QPushButton(MachineEdit)
        self.browse1.setObjectName(u"browse1")
        self.browse1.setGeometry(QRect(320, 130, 75, 23))
        self.mname = QLabel(MachineEdit)
        self.mname.setObjectName(u"mname")
        self.mname.setGeometry(QRect(10, 10, 81, 16))
        self.lineEdit = QLineEdit(MachineEdit)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 10, 291, 20))
        self.type = QLabel(MachineEdit)
        self.type.setObjectName(u"type")
        self.type.setGeometry(QRect(10, 50, 47, 13))
        self.poventry = QComboBox(MachineEdit)
        self.poventry.addItem("")
        self.poventry.setObjectName(u"poventry")
        self.poventry.setGeometry(QRect(40, 50, 81, 22))
        self.cfevm = QLabel(MachineEdit)
        self.cfevm.setObjectName(u"cfevm")
        self.cfevm.setGeometry(QRect(140, 50, 131, 16))
        self.b1 = QPushButton(MachineEdit)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(270, 50, 81, 23))
        self.vmos = QLabel(MachineEdit)
        self.vmos.setObjectName(u"vmos")
        self.vmos.setGeometry(QRect(10, 90, 47, 13))
        self.cb2 = QComboBox(MachineEdit)
        self.cb2.addItem("")
        self.cb2.setObjectName(u"cb2")
        self.cb2.setGeometry(QRect(70, 90, 291, 22))
        self.malwarebinary = QLabel(MachineEdit)
        self.malwarebinary.setObjectName(u"malwarebinary")
        self.malwarebinary.setGeometry(QRect(10, 130, 81, 16))
        self.input1 = QLineEdit(MachineEdit)
        self.input1.setObjectName(u"input1")
        self.input1.setGeometry(QRect(90, 130, 211, 20))
        self.msmodule = QLabel(MachineEdit)
        self.msmodule.setObjectName(u"msmodule")
        self.msmodule.setGeometry(QRect(10, 170, 91, 16))
        self.input2 = QLineEdit(MachineEdit)
        self.input2.setObjectName(u"input2")
        self.input2.setGeometry(QRect(110, 170, 191, 20))
        self.browse2 = QPushButton(MachineEdit)
        self.browse2.setObjectName(u"browse2")
        self.browse2.setGeometry(QRect(320, 170, 75, 23))
        self.script = QLabel(MachineEdit)
        self.script.setObjectName(u"script")
        self.script.setGeometry(QRect(10, 210, 47, 13))
        self.input3 = QLineEdit(MachineEdit)
        self.input3.setObjectName(u"input3")
        self.input3.setGeometry(QRect(50, 210, 251, 20))
        self.browse3 = QPushButton(MachineEdit)
        self.browse3.setObjectName(u"browse3")
        self.browse3.setGeometry(QRect(320, 210, 75, 23))
        self.software = QLabel(MachineEdit)
        self.software.setObjectName(u"software")
        self.software.setGeometry(QRect(10, 270, 47, 13))
        self.list1 = QListWidget(MachineEdit)
        QListWidgetItem(self.list1)
        self.list1.setObjectName(u"list1")
        self.list1.setGeometry(QRect(60, 250, 241, 61))
        self.add = QPushButton(MachineEdit)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(320, 270, 75, 23))
        self.line = QFrame(MachineEdit)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 310, 401, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.syssets = QPushButton(MachineEdit)
        self.syssets.setObjectName(u"syssets")
        self.syssets.setGeometry(QRect(140, 350, 121, 23))
        self.line_2 = QFrame(MachineEdit)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 390, 401, 21))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.save = QPushButton(MachineEdit)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(30, 420, 75, 23))
        self.discard = QPushButton(MachineEdit)
        self.discard.setObjectName(u"discard")
        self.discard.setGeometry(QRect(250, 420, 75, 23))

        self.retranslateUi(MachineEdit)

        QMetaObject.connectSlotsByName(MachineEdit)
    # setupUi

    def retranslateUi(self, MachineEdit):
        MachineEdit.setWindowTitle(QCoreApplication.translate("MachineEdit", u"Edit", None))
        self.label.setText(QCoreApplication.translate("MachineEdit", u"TextLabel", None))
        self.browse1.setText(QCoreApplication.translate("MachineEdit", u"Browse", None))
        self.mname.setText(QCoreApplication.translate("MachineEdit", u"Machine Name:", None))
        self.type.setText(QCoreApplication.translate("MachineEdit", u"Type:", None))
        self.poventry.setItemText(0, QCoreApplication.translate("MachineEdit", u"POV Entry", None))

        self.cfevm.setText(QCoreApplication.translate("MachineEdit", u"Create From Existing VM:", None))
        self.b1.setText(QCoreApplication.translate("MachineEdit", u"Open Existing", None))
        self.vmos.setText(QCoreApplication.translate("MachineEdit", u"VM OS:", None))
        self.cb2.setItemText(0, QCoreApplication.translate("MachineEdit", u"Kali Linux", None))

        self.malwarebinary.setText(QCoreApplication.translate("MachineEdit", u"Malware/Binary:", None))
        self.input1.setText(QCoreApplication.translate("MachineEdit", u"None", None))
        self.msmodule.setText(QCoreApplication.translate("MachineEdit", u"MetaSploit Module:", None))
        self.input2.setText(QCoreApplication.translate("MachineEdit", u"None", None))
        self.browse2.setText(QCoreApplication.translate("MachineEdit", u"Browse", None))
        self.script.setText(QCoreApplication.translate("MachineEdit", u"Script:", None))
        self.input3.setText(QCoreApplication.translate("MachineEdit", u"script.sh", None))
        self.browse3.setText(QCoreApplication.translate("MachineEdit", u"Browse", None))
        self.software.setText(QCoreApplication.translate("MachineEdit", u"Sftware:", None))

        __sortingEnabled = self.list1.isSortingEnabled()
        self.list1.setSortingEnabled(False)
        ___qlistwidgetitem = self.list1.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MachineEdit", u"All", None));
        self.list1.setSortingEnabled(__sortingEnabled)

        self.add.setText(QCoreApplication.translate("MachineEdit", u"Add", None))
        self.syssets.setText(QCoreApplication.translate("MachineEdit", u"System Settings", None))
        self.save.setText(QCoreApplication.translate("MachineEdit", u"Save", None))
        self.discard.setText(QCoreApplication.translate("MachineEdit", u"Discard", None))
    # retranslateUi

