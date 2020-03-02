# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setBaseSize(QSize(0, 0))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"qdarkstyle")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName(u"actionFile")
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionWhatIsThis = QAction(MainWindow)
        self.actionWhatIsThis.setObjectName(u"actionWhatIsThis")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutFull = QGridLayout(self.centralwidget)
        self.gridLayoutFull.setObjectName(u"gridLayoutFull")
        self.gridLayoutFull.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.defaultTab = QWidget()
        self.defaultTab.setObjectName(u"defaultTab")
        self.gridLayoutTab = QGridLayout(self.defaultTab)
        self.gridLayoutTab.setObjectName(u"gridLayoutTab")
        self.gridLayoutTab.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.defaultTab, "")

        self.gridLayoutFull.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuWoko = QMenu(self.menubar)
        self.menuWoko.setObjectName(u"menuWoko")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setFloatable(True)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuWoko.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuWoko.addAction(self.actionFile)
        self.menuWoko.addAction(self.actionImport)
        self.menuWoko.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionWhatIsThis)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoBug", None))
        self.actionFile.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionWhatIsThis.setText(QCoreApplication.translate("MainWindow", u"What Is This?", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.defaultTab), QCoreApplication.translate("MainWindow", u"Default", None))
        self.menuWoko.setTitle(QCoreApplication.translate("MainWindow", u"Scenario", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

