# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_waste_types.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_wasteTypeWidget(object):
    def setupUi(self, wasteTypeWidget):
        if not wasteTypeWidget.objectName():
            wasteTypeWidget.setObjectName(u"wasteTypeWidget")
        wasteTypeWidget.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(wasteTypeWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.wasteTypes = QLabel(wasteTypeWidget)
        self.wasteTypes.setObjectName(u"wasteTypes")

        self.verticalLayout.addWidget(self.wasteTypes)

        self.wasteTypeTable = QTableWidget(wasteTypeWidget)
        self.wasteTypeTable.setObjectName(u"wasteTypeTable")

        self.verticalLayout.addWidget(self.wasteTypeTable)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(wasteTypeWidget)

        QMetaObject.connectSlotsByName(wasteTypeWidget)
    # setupUi

    def retranslateUi(self, wasteTypeWidget):
        wasteTypeWidget.setWindowTitle(QCoreApplication.translate("wasteTypeWidget", u"Form", None))
        self.wasteTypes.setText(QCoreApplication.translate("wasteTypeWidget", u"Current waste types:", None))
    # retranslateUi

