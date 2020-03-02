# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newScenario.ui'
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


class Ui_NewScenario(object):
    def setupUi(self, NewScenario):
        if NewScenario.objectName():
            NewScenario.setObjectName(u"NewScenario")
        NewScenario.resize(484, 476)
        self.buttons = QDialogButtonBox(NewScenario)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setGeometry(QRect(90, 430, 341, 32))
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.Save)
        self.tableWidget = QTableWidget(NewScenario)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setCheckState(Qt.Unchecked);
        __qtablewidgetitem7.setTextAlignment(Qt.AlignHCenter|Qt.AlignTop);
        __qtablewidgetitem7.setFlags(Qt.NoItemFlags);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFlags(Qt.ItemIsEnabled);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setCheckState(Qt.Unchecked);
        __qtablewidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFlags(Qt.ItemIsEnabled);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setCheckState(Qt.Unchecked);
        __qtablewidgetitem11.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFlags(Qt.ItemIsEnabled);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setCheckState(Qt.Unchecked);
        __qtablewidgetitem13.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(3, 1, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 130, 301, 101))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(15)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(15)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.label = QLabel(NewScenario)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 0, 121, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(NewScenario)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 91, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.scenarioName = QPlainTextEdit(NewScenario)
        self.scenarioName.setObjectName(u"scenarioName")
        self.scenarioName.setGeometry(QRect(30, 80, 279, 24))
        self.tableWidget_2 = QTableWidget(NewScenario)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        if (self.tableWidget_2.rowCount() < 4):
            self.tableWidget_2.setRowCount(4)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFlags(Qt.NoItemFlags);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setCheckState(Qt.Unchecked);
        __qtablewidgetitem21.setFlags(Qt.NoItemFlags);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFlags(Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setCheckState(Qt.Unchecked);
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFlags(Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setCheckState(Qt.Unchecked);
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setCheckState(Qt.Unchecked);
        self.tableWidget_2.setItem(3, 1, __qtablewidgetitem26)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(70, 290, 301, 101))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy1)
        self.tableWidget_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.setWordWrap(False)
        self.tableWidget_2.setRowCount(4)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(15)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget_2.verticalHeader().setVisible(True)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(15)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)
        self.addExploit = QPushButton(NewScenario)
        self.addExploit.setObjectName(u"addExploit")
        self.addExploit.setGeometry(QRect(390, 160, 41, 31))
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        font2.setWeight(75)
        self.addExploit.setFont(font2)
        self.delExploit = QPushButton(NewScenario)
        self.delExploit.setObjectName(u"delExploit")
        self.delExploit.setGeometry(QRect(270, 130, 61, 23))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.delExploit.setFont(font3)
        self.addVulProg = QPushButton(NewScenario)
        self.addVulProg.setObjectName(u"addVulProg")
        self.addVulProg.setGeometry(QRect(390, 320, 41, 31))
        self.addVulProg.setFont(font2)
        self.delVulProg = QPushButton(NewScenario)
        self.delVulProg.setObjectName(u"delVulProg")
        self.delVulProg.setGeometry(QRect(280, 290, 61, 23))
        self.delVulProg.setFont(font3)
        self.tableWidget.raise_()
        self.buttons.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.scenarioName.raise_()
        self.tableWidget_2.raise_()
        self.addExploit.raise_()
        self.delExploit.raise_()
        self.addVulProg.raise_()
        self.delVulProg.raise_()

        self.retranslateUi(NewScenario)
        self.buttons.accepted.connect(NewScenario.accept)
        self.buttons.rejected.connect(NewScenario.reject)

        QMetaObject.connectSlotsByName(NewScenario)
    # setupUi

    def retranslateUi(self, NewScenario):
        NewScenario.setWindowTitle(QCoreApplication.translate("NewScenario", u"New Scenario", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("NewScenario", u"Path", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("NewScenario", u"Delete", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("NewScenario", u"Exploits                   ", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("NewScenario", u"e0", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("NewScenario", u"e1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("NewScenario", u"e2", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(whatsthis)
        self.tableWidget.setWhatsThis(QCoreApplication.translate("NewScenario", u"<html><head/><body><p>Exploit</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("NewScenario", u"New Scenario", None))
        self.label_2.setText(QCoreApplication.translate("NewScenario", u"Scenario Name", None))
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("NewScenario", u"Path", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("NewScenario", u"Delete", None));
        ___qtablewidgetitem8 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("NewScenario", u"Vulnerable Programs", None));
        ___qtablewidgetitem9 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("NewScenario", u"p0", None));
        ___qtablewidgetitem10 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("NewScenario", u"p1", None));
        ___qtablewidgetitem11 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("NewScenario", u"p2", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(whatsthis)
        self.tableWidget_2.setWhatsThis(QCoreApplication.translate("NewScenario", u"<html><head/><body><p>Exploit</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.addExploit.setText(QCoreApplication.translate("NewScenario", u"+", None))
        self.delExploit.setText(QCoreApplication.translate("NewScenario", u"Delete", None))
        self.addVulProg.setText(QCoreApplication.translate("NewScenario", u"+", None))
        self.delVulProg.setText(QCoreApplication.translate("NewScenario", u"Delete", None))
    # retranslateUi

