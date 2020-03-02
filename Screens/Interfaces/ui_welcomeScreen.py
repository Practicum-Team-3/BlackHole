# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcomeScreen.ui'
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


class Ui_WelcomeScreen(object):
    def setupUi(self, WelcomeScreen):
        if WelcomeScreen.objectName():
            WelcomeScreen.setObjectName(u"WelcomeScreen")
        WelcomeScreen.resize(969, 616)
        self.groupBox = QGroupBox(WelcomeScreen)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 130, 281, 431))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.lstScenarios = QListWidget(self.groupBox)
        QListWidgetItem(self.lstScenarios)
        QListWidgetItem(self.lstScenarios)
        QListWidgetItem(self.lstScenarios)
        QListWidgetItem(self.lstScenarios)
        QListWidgetItem(self.lstScenarios)
        QListWidgetItem(self.lstScenarios)
        QListWidgetItem(self.lstScenarios)
        QListWidgetItem(self.lstScenarios)
        QListWidgetItem(self.lstScenarios)
        self.lstScenarios.setObjectName(u"lstScenarios")
        self.lstScenarios.setGeometry(QRect(15, 20, 250, 401))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.lstScenarios.setFont(font1)
        self.btnNew = QPushButton(WelcomeScreen)
        self.btnNew.setObjectName(u"btnNew")
        self.btnNew.setGeometry(QRect(210, 570, 93, 28))
        self.groupBox_2 = QGroupBox(WelcomeScreen)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(313, 130, 641, 431))
        self.groupBox_2.setFont(font)
        self.txtDesc = QTextBrowser(self.groupBox_2)
        self.txtDesc.setObjectName(u"txtDesc")
        self.txtDesc.setGeometry(QRect(9, 20, 621, 401))
        self.txtDesc.setFont(font1)
        self.btnOpen = QPushButton(WelcomeScreen)
        self.btnOpen.setObjectName(u"btnOpen")
        self.btnOpen.setGeometry(QRect(860, 570, 93, 28))
        self.label = QLabel(WelcomeScreen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 10, 131, 111))
        self.label.setAutoFillBackground(False)
        self.label.setPixmap(QPixmap(u"../../../../../../Downloads/hacker-hack-crime-cyber_2-512.png"))
        self.label.setScaledContents(True)
        self.btnEdit = QPushButton(WelcomeScreen)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setGeometry(QRect(760, 570, 93, 28))
        self.btnRemove = QPushButton(WelcomeScreen)
        self.btnRemove.setObjectName(u"btnRemove")
        self.btnRemove.setGeometry(QRect(660, 570, 93, 28))

        self.retranslateUi(WelcomeScreen)

        QMetaObject.connectSlotsByName(WelcomeScreen)
    # setupUi

    def retranslateUi(self, WelcomeScreen):
        WelcomeScreen.setWindowTitle(QCoreApplication.translate("WelcomeScreen", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("WelcomeScreen", u"Scenarios", None))

        __sortingEnabled = self.lstScenarios.isSortingEnabled()
        self.lstScenarios.setSortingEnabled(False)
        ___qlistwidgetitem = self.lstScenarios.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("WelcomeScreen", u"Scenario 0001", None));
        ___qlistwidgetitem1 = self.lstScenarios.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("WelcomeScreen", u"Scenario 0002", None));
        ___qlistwidgetitem2 = self.lstScenarios.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("WelcomeScreen", u"Scenario 0003", None));
        ___qlistwidgetitem3 = self.lstScenarios.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("WelcomeScreen", u"Scenario 0004", None));
        ___qlistwidgetitem4 = self.lstScenarios.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("WelcomeScreen", u"Scenario 0005", None));
        ___qlistwidgetitem5 = self.lstScenarios.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("WelcomeScreen", u"Scenario 0006", None));
        ___qlistwidgetitem6 = self.lstScenarios.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("WelcomeScreen", u"Scenario 0007", None));
        ___qlistwidgetitem7 = self.lstScenarios.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("WelcomeScreen", u"Scenario 0008", None));
        ___qlistwidgetitem8 = self.lstScenarios.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("WelcomeScreen", u"Scenario 0009", None));
        self.lstScenarios.setSortingEnabled(__sortingEnabled)

        self.btnNew.setText(QCoreApplication.translate("WelcomeScreen", u"New Scenario", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("WelcomeScreen", u"Scenario Description", None))
        self.btnOpen.setText(QCoreApplication.translate("WelcomeScreen", u"Open", None))
        self.label.setText("")
        self.btnEdit.setText(QCoreApplication.translate("WelcomeScreen", u"Edit", None))
        self.btnRemove.setText(QCoreApplication.translate("WelcomeScreen", u"Remove", None))
    # retranslateUi

