from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RemoveWasteType(object):
    def setupUi(self, RemoveWasteType):
        if not RemoveWasteType.objectName():
            RemoveWasteType.setObjectName(u"RemoveWasteType")
        RemoveWasteType.resize(659, 438)
        self.horizontalLayout = QHBoxLayout(RemoveWasteType)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(RemoveWasteType)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(9)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.dropdownlist = QComboBox(RemoveWasteType)
        self.dropdownlist.setObjectName(u"dropdownlist")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dropdownlist.sizePolicy().hasHeightForWidth())
        self.dropdownlist.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.dropdownlist)

        self.buttonBox = QDialogButtonBox(RemoveWasteType)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(RemoveWasteType)

        QMetaObject.connectSlotsByName(RemoveWasteType)
    # setupUi

    def retranslateUi(self, RemoveWasteType):
        RemoveWasteType.setWindowTitle(QCoreApplication.translate("RemoveWasteType", u"RemoveWasteType", None))
        self.label.setText(QCoreApplication.translate("RemoveWasteType", u"Choose which type of waste you would like to remove:", None))
    # retranslateUi
    