# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'networkPanel.ui'
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


class Ui_NetworkPanel(object):
    def setupUi(self, NetworkPanel):
        if NetworkPanel.objectName():
            NetworkPanel.setObjectName(u"NetworkPanel")
        NetworkPanel.resize(800, 600)
        self.horizontalLayout = QHBoxLayout(NetworkPanel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.networkItemsScroll = QScrollArea(NetworkPanel)
        self.networkItemsScroll.setObjectName(u"networkItemsScroll")
        self.networkItemsScroll.setMaximumSize(QSize(150, 16777215))
        self.networkItemsScroll.setFrameShape(QFrame.NoFrame)
        self.networkItemsScroll.setWidgetResizable(True)
        self.networkItemsScroll.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.networkItems = QWidget()
        self.networkItems.setObjectName(u"networkItems")
        self.networkItems.setGeometry(QRect(0, 0, 150, 600))
        self.networkItemsList = QVBoxLayout(self.networkItems)
        self.networkItemsList.setObjectName(u"networkItemsList")
        self.networkItemsList.setSizeConstraint(QLayout.SetMaximumSize)
        self.networkItemsScroll.setWidget(self.networkItems)

        self.horizontalLayout.addWidget(self.networkItemsScroll)

        self.graphFrame = QFrame(NetworkPanel)
        self.graphFrame.setObjectName(u"graphFrame")
        self.graphFrame.setMinimumSize(QSize(300, 0))
        self.graphFrame.setFrameShape(QFrame.NoFrame)
        self.graphFrame.setFrameShadow(QFrame.Raised)
        self.graphArea = QGridLayout(self.graphFrame)
#ifndef Q_OS_MAC
        self.graphArea.setSpacing(-1)
#endif
        self.graphArea.setObjectName(u"graphArea")
        self.graphArea.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.graphFrame)

        self.machineInfoScroll = QScrollArea(NetworkPanel)
        self.machineInfoScroll.setObjectName(u"machineInfoScroll")
        self.machineInfoScroll.setMinimumSize(QSize(200, 0))
        self.machineInfoScroll.setMaximumSize(QSize(300, 16777215))
        self.machineInfoScroll.setFrameShape(QFrame.NoFrame)
        self.machineInfoScroll.setFrameShadow(QFrame.Raised)
        self.machineInfoScroll.setLineWidth(1)
        self.machineInfoScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.machineInfoScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 300, 600))
        self.machineInfoArea = QGridLayout(self.scrollAreaWidgetContents)
        self.machineInfoArea.setObjectName(u"machineInfoArea")
        self.machineInfoArea.setContentsMargins(0, 0, 0, 0)
        self.machineInfoScroll.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.machineInfoScroll)


        self.retranslateUi(NetworkPanel)

        QMetaObject.connectSlotsByName(NetworkPanel)
    # setupUi

    def retranslateUi(self, NetworkPanel):
        NetworkPanel.setWindowTitle(QCoreApplication.translate("NetworkPanel", u"Frame", None))
    # retranslateUi

