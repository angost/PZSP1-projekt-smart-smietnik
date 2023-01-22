# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TurnWaste(object):
    def setupUi(self, TurnWaste):
        if not TurnWaste.objectName():
            TurnWaste.setObjectName(u"TurnWaste")
        TurnWaste.resize(1072, 593)
        self.actionAdd_trasmitter = QAction(TurnWaste)
        self.actionAdd_trasmitter.setObjectName(u"actionAdd_trasmitter")
        self.actionRemove_trasmitter = QAction(TurnWaste)
        self.actionRemove_trasmitter.setObjectName(u"actionRemove_trasmitter")
        self.actionAdd_location = QAction(TurnWaste)
        self.actionAdd_location.setObjectName(u"actionAdd_location")
        self.actionRemove_location = QAction(TurnWaste)
        self.actionRemove_location.setObjectName(u"actionRemove_location")
        self.actionAdd_waste_type = QAction(TurnWaste)
        self.actionAdd_waste_type.setObjectName(u"actionAdd_waste_type")
        self.actionRemove_waste_type = QAction(TurnWaste)
        self.actionRemove_waste_type.setObjectName(u"actionRemove_waste_type")
        self.actionBy_location = QAction(TurnWaste)
        self.actionBy_location.setObjectName(u"actionBy_location")
        self.actionBy_waste_type = QAction(TurnWaste)
        self.actionBy_waste_type.setObjectName(u"actionBy_waste_type")
        self.actionShow_all_locations = QAction(TurnWaste)
        self.actionShow_all_locations.setObjectName(u"actionShow_all_locations")
        self.actionShow_all_waste_types = QAction(TurnWaste)
        self.actionShow_all_waste_types.setObjectName(u"actionShow_all_waste_types")
        self.actionShow_all_transmitters = QAction(TurnWaste)
        self.actionShow_all_transmitters.setObjectName(u"actionShow_all_transmitters")
        self.actionBy_filling_level = QAction(TurnWaste)
        self.actionBy_filling_level.setObjectName(u"actionBy_filling_level")
        self.centralwidget = QWidget(TurnWaste)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.transmittersTable = QTableWidget(self.centralwidget)
        self.transmittersTable.setObjectName(u"transmittersTable")

        self.verticalLayout.addWidget(self.transmittersTable)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.numberOfFull = QLabel(self.centralwidget)
        self.numberOfFull.setObjectName(u"numberOfFull")

        self.horizontalLayout.addWidget(self.numberOfFull)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setValue(90)
        self.progressBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        TurnWaste.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TurnWaste)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1072, 24))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuLocation = QMenu(self.menubar)
        self.menuLocation.setObjectName(u"menuLocation")
        self.menuWaste_type = QMenu(self.menubar)
        self.menuWaste_type.setObjectName(u"menuWaste_type")
        self.menuFilter = QMenu(self.menubar)
        self.menuFilter.setObjectName(u"menuFilter")
        TurnWaste.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TurnWaste)
        self.statusbar.setObjectName(u"statusbar")
        TurnWaste.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuLocation.menuAction())
        self.menubar.addAction(self.menuWaste_type.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menuOptions.addAction(self.actionShow_all_transmitters)
        self.menuOptions.addAction(self.actionAdd_trasmitter)
        self.menuOptions.addAction(self.actionRemove_trasmitter)
        self.menuLocation.addAction(self.actionShow_all_locations)
        self.menuLocation.addAction(self.actionAdd_location)
        self.menuLocation.addAction(self.actionRemove_location)
        self.menuWaste_type.addAction(self.actionShow_all_waste_types)
        self.menuWaste_type.addAction(self.actionAdd_waste_type)
        self.menuWaste_type.addAction(self.actionRemove_waste_type)
        self.menuFilter.addAction(self.actionBy_location)
        self.menuFilter.addAction(self.actionBy_waste_type)
        self.menuFilter.addAction(self.actionBy_filling_level)

        self.retranslateUi(TurnWaste)

        QMetaObject.connectSlotsByName(TurnWaste)
    # setupUi

    def retranslateUi(self, TurnWaste):
        TurnWaste.setWindowTitle(QCoreApplication.translate("TurnWaste", u"MainWindow", None))
        self.actionAdd_trasmitter.setText(QCoreApplication.translate("TurnWaste", u"Add transmitter", None))
        self.actionRemove_trasmitter.setText(QCoreApplication.translate("TurnWaste", u"Remove transmitter", None))
        self.actionAdd_location.setText(QCoreApplication.translate("TurnWaste", u"Add location", None))
        self.actionRemove_location.setText(QCoreApplication.translate("TurnWaste", u"Remove location", None))
        self.actionAdd_waste_type.setText(QCoreApplication.translate("TurnWaste", u"Add waste type", None))
        self.actionRemove_waste_type.setText(QCoreApplication.translate("TurnWaste", u"Remove waste type", None))
        self.actionBy_location.setText(QCoreApplication.translate("TurnWaste", u"By location", None))
        self.actionBy_waste_type.setText(QCoreApplication.translate("TurnWaste", u"By waste type", None))
        self.actionShow_all_locations.setText(QCoreApplication.translate("TurnWaste", u"Show all locations", None))
        self.actionShow_all_waste_types.setText(QCoreApplication.translate("TurnWaste", u"Show all waste types", None))
        self.actionShow_all_transmitters.setText(QCoreApplication.translate("TurnWaste", u"Show all transmitters", None))
        self.actionBy_filling_level.setText(QCoreApplication.translate("TurnWaste", u"By filling level", None))
        self.numberOfFull.setText(QCoreApplication.translate("TurnWaste", u"a", None))
        self.menuOptions.setTitle(QCoreApplication.translate("TurnWaste", u"Transmitter", None))
        self.menuLocation.setTitle(QCoreApplication.translate("TurnWaste", u"Location", None))
        self.menuWaste_type.setTitle(QCoreApplication.translate("TurnWaste", u"Waste type", None))
        self.menuFilter.setTitle(QCoreApplication.translate("TurnWaste", u"Filter", None))
    # retranslateUi

