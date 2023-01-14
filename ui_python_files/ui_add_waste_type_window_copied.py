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

        self.add_waste_type_label = QLabel(self.layoutWidget)
        self.add_waste_type_label.setObjectName(u"add_waste_type_label")
        self.add_waste_type_label.setAlignment(Qt.AlignCenter)
        self.add_waste_type_label.setMargin(15)

        self.verticalLayout_4.addWidget(self.add_waste_type_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.waste_type_name_label = QLabel(self.layoutWidget)
        self.waste_type_name_label.setObjectName(u"waste_type_name_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waste_type_name_label.sizePolicy().hasHeightForWidth())
        self.waste_type_name_label.setSizePolicy(sizePolicy)
        self.waste_type_name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.waste_type_name_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.enter_waste_type_name = QLineEdit(self.layoutWidget)
        self.enter_waste_type_name.setObjectName(u"enter_waste_type_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enter_waste_type_name.sizePolicy().hasHeightForWidth())
        self.enter_waste_type_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.enter_waste_type_name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

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
        self.add_waste_type_label.setText(QCoreApplication.translate("Form", u"Enter new waste type info:", None))
        self.waste_type_name_label.setText(QCoreApplication.translate("Form", u"Waste type name", None))
    # retranslateUi