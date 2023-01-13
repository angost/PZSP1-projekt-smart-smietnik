# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 680)
        self.actionAdd_trasmitter = QAction(MainWindow)
        self.actionAdd_trasmitter.setObjectName(u"actionAdd_trasmitter")
        self.actionRemove_trasmitter = QAction(MainWindow)
        self.actionRemove_trasmitter.setObjectName(u"actionRemove_trasmitter")
        self.actionAdd_location = QAction(MainWindow)
        self.actionAdd_location.setObjectName(u"actionAdd_location")
        self.actionRemove_location = QAction(MainWindow)
        self.actionRemove_location.setObjectName(u"actionRemove_location")
        self.actionAdd_waste_type = QAction(MainWindow)
        self.actionAdd_waste_type.setObjectName(u"actionAdd_waste_type")
        self.actionRemove_waste_type = QAction(MainWindow)
        self.actionRemove_waste_type.setObjectName(u"actionRemove_waste_type")
        self.actionBy_location = QAction(MainWindow)
        self.actionBy_location.setObjectName(u"actionBy_location")
        self.actionBy_waste_type = QAction(MainWindow)
        self.actionBy_waste_type.setObjectName(u"actionBy_waste_type")
        self.actionShow_all_locations = QAction(MainWindow)
        self.actionShow_all_locations.setObjectName(u"actionShow_all_locations")
        self.actionShow_all_waste_types = QAction(MainWindow)
        self.actionShow_all_waste_types.setObjectName(u"actionShow_all_waste_types")
        self.actionShow_all_transmitters = QAction(MainWindow)
        self.actionShow_all_transmitters.setObjectName(u"actionShow_all_transmitters")
        self.actionBy_filling_level = QAction(MainWindow)
        self.actionBy_filling_level.setObjectName(u"actionBy_filling_level")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.horizontalLayout.addWidget(self.listWidget_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 24))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuLocation = QMenu(self.menubar)
        self.menuLocation.setObjectName(u"menuLocation")
        self.menuWaste_type = QMenu(self.menubar)
        self.menuWaste_type.setObjectName(u"menuWaste_type")
        self.menuFilter = QMenu(self.menubar)
        self.menuFilter.setObjectName(u"menuFilter")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_trasmitter.setText(QCoreApplication.translate("MainWindow", u"Add transmitter", None))
        self.actionRemove_trasmitter.setText(QCoreApplication.translate("MainWindow", u"Remove transmitter", None))
        self.actionAdd_location.setText(QCoreApplication.translate("MainWindow", u"Add location", None))
        self.actionRemove_location.setText(QCoreApplication.translate("MainWindow", u"Remove location", None))
        self.actionAdd_waste_type.setText(QCoreApplication.translate("MainWindow", u"Add waste type", None))
        self.actionRemove_waste_type.setText(QCoreApplication.translate("MainWindow", u"Remove waste type", None))
        self.actionBy_location.setText(QCoreApplication.translate("MainWindow", u"By location", None))
        self.actionBy_waste_type.setText(QCoreApplication.translate("MainWindow", u"By waste type", None))
        self.actionShow_all_locations.setText(QCoreApplication.translate("MainWindow", u"Show all locations", None))
        self.actionShow_all_waste_types.setText(QCoreApplication.translate("MainWindow", u"Show all waste types", None))
        self.actionShow_all_transmitters.setText(QCoreApplication.translate("MainWindow", u"Show all transmitters", None))
        self.actionBy_filling_level.setText(QCoreApplication.translate("MainWindow", u"By filling level", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Transmitter", None))
        self.menuLocation.setTitle(QCoreApplication.translate("MainWindow", u"Location", None))
        self.menuWaste_type.setTitle(QCoreApplication.translate("MainWindow", u"Waste type", None))
        self.menuFilter.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
    # retranslateUi

