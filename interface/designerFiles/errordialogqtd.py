# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/designerFiles/errorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_errorDiag(object):
    def setupUi(self, errorDiag):
        errorDiag.setObjectName("errorDiag")
        errorDiag.resize(260, 83)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(errorDiag.sizePolicy().hasHeightForWidth())
        errorDiag.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(errorDiag)
        self.verticalLayout.setObjectName("verticalLayout")
        self.errorDiagInfoLabel = QtWidgets.QLabel(errorDiag)
        self.errorDiagInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorDiagInfoLabel.setObjectName("errorDiagInfoLabel")
        self.verticalLayout.addWidget(self.errorDiagInfoLabel)
        self.errorDiagAcceptButton = QtWidgets.QDialogButtonBox(errorDiag)
        self.errorDiagAcceptButton.setOrientation(QtCore.Qt.Horizontal)
        self.errorDiagAcceptButton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.errorDiagAcceptButton.setCenterButtons(True)
        self.errorDiagAcceptButton.setObjectName("errorDiagAcceptButton")
        self.verticalLayout.addWidget(self.errorDiagAcceptButton)

        self.retranslateUi(errorDiag)
        self.errorDiagAcceptButton.accepted.connect(errorDiag.accept)
        QtCore.QMetaObject.connectSlotsByName(errorDiag)

    def retranslateUi(self, errorDiag):
        _translate = QtCore.QCoreApplication.translate
        errorDiag.setWindowTitle(_translate("errorDiag", "Error"))
        self.errorDiagInfoLabel.setText(_translate("errorDiag", "Device not found at selected port."))

