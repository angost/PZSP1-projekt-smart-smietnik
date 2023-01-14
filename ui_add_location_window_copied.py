from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1072, 593)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1071, 591))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.add_location_label = QLabel(self.layoutWidget)
        self.add_location_label.setObjectName(u"add_location_label")
        self.add_location_label.setAlignment(Qt.AlignCenter)
        self.add_location_label.setMargin(15)

        self.verticalLayout_4.addWidget(self.add_location_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.country_label = QLabel(self.layoutWidget)
        self.country_label.setObjectName(u"country_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.country_label.sizePolicy().hasHeightForWidth())
        self.country_label.setSizePolicy(sizePolicy)
        self.country_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.country_label)

        self.enter_country = QLineEdit(self.layoutWidget)
        self.enter_country.setObjectName(u"enter_country")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enter_country.sizePolicy().hasHeightForWidth())
        self.enter_country.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.enter_country)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.city_label = QLabel(self.layoutWidget)
        self.city_label.setObjectName(u"city_label")
        sizePolicy.setHeightForWidth(self.city_label.sizePolicy().hasHeightForWidth())
        self.city_label.setSizePolicy(sizePolicy)
        self.city_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.city_label)

        self.enter_city = QLineEdit(self.layoutWidget)
        self.enter_city.setObjectName(u"enter_city")
        sizePolicy1.setHeightForWidth(self.enter_city.sizePolicy().hasHeightForWidth())
        self.enter_city.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.enter_city)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.street_label = QLabel(self.layoutWidget)
        self.street_label.setObjectName(u"street_label")
        sizePolicy.setHeightForWidth(self.street_label.sizePolicy().hasHeightForWidth())
        self.street_label.setSizePolicy(sizePolicy)
        self.street_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.street_label)

        self.enter_street = QLineEdit(self.layoutWidget)
        self.enter_street.setObjectName(u"enter_street")
        sizePolicy1.setHeightForWidth(self.enter_street.sizePolicy().hasHeightForWidth())
        self.enter_street.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.enter_street)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.number_label = QLabel(self.layoutWidget)
        self.number_label.setObjectName(u"number_label")
        sizePolicy.setHeightForWidth(self.number_label.sizePolicy().hasHeightForWidth())
        self.number_label.setSizePolicy(sizePolicy)
        self.number_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.number_label)

        self.enter_number = QLineEdit(self.layoutWidget)
        self.enter_number.setObjectName(u"enter_number")
        sizePolicy1.setHeightForWidth(self.enter_number.sizePolicy().hasHeightForWidth())
        self.enter_number.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.enter_number)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.notes_label = QLabel(self.layoutWidget)
        self.notes_label.setObjectName(u"notes_label")
        sizePolicy.setHeightForWidth(self.notes_label.sizePolicy().hasHeightForWidth())
        self.notes_label.setSizePolicy(sizePolicy)
        self.notes_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.notes_label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.enter_notes = QLineEdit(self.layoutWidget)
        self.enter_notes.setObjectName(u"enter_notes")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.enter_notes.sizePolicy().hasHeightForWidth())
        self.enter_notes.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.enter_notes)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

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
        self.add_location_label.setText(QCoreApplication.translate("Form", u"Enter new location info:", None))
        self.country_label.setText(QCoreApplication.translate("Form", u"Country", None))
        self.city_label.setText(QCoreApplication.translate("Form", u"City", None))
        self.street_label.setText(QCoreApplication.translate("Form", u"Street", None))
        self.number_label.setText(QCoreApplication.translate("Form", u"Number", None))
        self.notes_label.setText(QCoreApplication.translate("Form", u"Notes", None))
    # retranslateUi
