# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_locations.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_locationsWidget(object):
    def setupUi(self, locationsWidget):
        if not locationsWidget.objectName():
            locationsWidget.setObjectName(u"locationsWidget")
        locationsWidget.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(locationsWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.locations = QLabel(locationsWidget)
        self.locations.setObjectName(u"locations")

        self.verticalLayout.addWidget(self.locations)

        self.locationsTable = QTableWidget(locationsWidget)
        self.locationsTable.setObjectName(u"locationsTable")

        self.verticalLayout.addWidget(self.locationsTable)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(locationsWidget)

        QMetaObject.connectSlotsByName(locationsWidget)
    # setupUi

    def retranslateUi(self, locationsWidget):
        locationsWidget.setWindowTitle(QCoreApplication.translate("locationsWidget", u"Form", None))
        self.locations.setText(QCoreApplication.translate("locationsWidget", u"Current locations: ", None))
    # retranslateUi

