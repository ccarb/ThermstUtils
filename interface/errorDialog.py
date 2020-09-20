from PyQt5 import QtCore, QtWidgets
from interface.designerFiles.errordialogqtd import Ui_errorDiag
from server import flask_server

class ErrorDialog(QtWidgets.QDialog,Ui_errorDiag):
    def __init__(self, *args, **kwargs):
        super(ErrorDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
