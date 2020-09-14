# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/designerFiles/connectionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_connectionDialog(object):
    def setupUi(self, connectionDialog):
        connectionDialog.setObjectName("connectionDialog")
        connectionDialog.resize(372, 113)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(connectionDialog.sizePolicy().hasHeightForWidth())
        connectionDialog.setSizePolicy(sizePolicy)
        connectionDialog.setSizeGripEnabled(False)
        connectionDialog.setModal(False)
        self.formLayout = QtWidgets.QFormLayout(connectionDialog)
        self.formLayout.setObjectName("formLayout")
        self.devicesListLabel = QtWidgets.QLabel(connectionDialog)
        self.devicesListLabel.setObjectName("devicesListLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.devicesListLabel)
        self.devicesList = QtWidgets.QComboBox(connectionDialog)
        self.devicesList.setMinimumContentsLength(0)
        self.devicesList.setObjectName("devicesList")
        self.devicesList.addItem("")
        self.devicesList.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.devicesList)
        self.modeSelectorLabel = QtWidgets.QLabel(connectionDialog)
        self.modeSelectorLabel.setObjectName("modeSelectorLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.modeSelectorLabel)
        self.paradigmModeButton = QtWidgets.QRadioButton(connectionDialog)
        self.paradigmModeButton.setChecked(True)
        self.paradigmModeButton.setObjectName("paradigmModeButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.paradigmModeButton)
        self.maintenanceModeButton = QtWidgets.QRadioButton(connectionDialog)
        self.maintenanceModeButton.setObjectName("maintenanceModeButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.maintenanceModeButton)
        self.connectionDialogButtons = QtWidgets.QDialogButtonBox(connectionDialog)
        self.connectionDialogButtons.setOrientation(QtCore.Qt.Horizontal)
        self.connectionDialogButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.connectionDialogButtons.setObjectName("connectionDialogButtons")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.connectionDialogButtons)

        self.retranslateUi(connectionDialog)
        self.devicesList.setCurrentIndex(0)
        self.connectionDialogButtons.accepted.connect(connectionDialog.accept)
        self.connectionDialogButtons.rejected.connect(connectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(connectionDialog)
        connectionDialog.setTabOrder(self.devicesList, self.maintenanceModeButton)
        connectionDialog.setTabOrder(self.maintenanceModeButton, self.paradigmModeButton)

    def retranslateUi(self, connectionDialog):
        _translate = QtCore.QCoreApplication.translate
        connectionDialog.setWindowTitle(_translate("connectionDialog", "Connection Settings"))
        self.devicesListLabel.setToolTip(_translate("connectionDialog", "Choose the port in which the device is connected"))
        self.devicesListLabel.setText(_translate("connectionDialog", "Devices:"))
        self.devicesList.setCurrentText(_translate("connectionDialog", "test item 1"))
        self.devicesList.setItemText(0, _translate("connectionDialog", "test item 1"))
        self.devicesList.setItemText(1, _translate("connectionDialog", "test item 2"))
        self.modeSelectorLabel.setToolTip(_translate("connectionDialog", "Select the mode of operation"))
        self.modeSelectorLabel.setText(_translate("connectionDialog", "Mode:"))
        self.paradigmModeButton.setToolTip(_translate("connectionDialog", "Paradigm: the program has no interaction with the device"))
        self.paradigmModeButton.setText(_translate("connectionDialog", "Paradigm"))
        self.maintenanceModeButton.setToolTip(_translate("connectionDialog", "Maintenance: Program has full control of the device"))
        self.maintenanceModeButton.setText(_translate("connectionDialog", "Maintenance/Diagnostics"))
import resources_rc
