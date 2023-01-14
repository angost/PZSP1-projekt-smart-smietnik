from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1069, 592)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(200, 90, 711, 441))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.add_transmitter_label = QLabel(self.layoutWidget)
        self.add_transmitter_label.setObjectName(u"add_transmitter_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_transmitter_label.sizePolicy().hasHeightForWidth())
        self.add_transmitter_label.setSizePolicy(sizePolicy)
        self.add_transmitter_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.add_transmitter_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.select_waste_type_label = QLabel(self.layoutWidget)
        self.select_waste_type_label.setObjectName(u"select_waste_type_label")
        self.select_waste_type_label.setMargin(15)

        self.verticalLayout_3.addWidget(self.select_waste_type_label)

        self.select_waste_type_dropdown = QComboBox(self.layoutWidget)
        self.select_waste_type_dropdown.setObjectName(u"select_waste_type_dropdown")

        self.verticalLayout_3.addWidget(self.select_waste_type_dropdown)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.select_location_label = QLabel(self.layoutWidget)
        self.select_location_label.setObjectName(u"select_location_label")
        self.select_location_label.setMargin(15)

        self.verticalLayout_2.addWidget(self.select_location_label)

        self.select_location_dropdown = QComboBox(self.layoutWidget)
        self.select_location_dropdown.setObjectName(u"select_location_dropdown")

        self.verticalLayout_2.addWidget(self.select_location_dropdown)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.window_control = QDialogButtonBox(self.layoutWidget)
        self.window_control.setObjectName(u"window_control")
        self.window_control.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.window_control.setCenterButtons(False)

        self.verticalLayout_4.addWidget(self.window_control)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.add_transmitter_label.setText(QCoreApplication.translate("Form", u"Enter new transmitter info:", None))
        self.select_waste_type_label.setText(QCoreApplication.translate("Form", u"Select waste type", None))
        self.select_location_label.setText(QCoreApplication.translate("Form", u"Select location", None))
    # retranslateUi