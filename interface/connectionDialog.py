from PyQt5 import QtCore, QtWidgets
from interface.designerFiles.connectiondialogqtd import Ui_connectionDialog
from server import flask_server

class ConnectionDialog(QtWidgets.QDialog,Ui_connectionDialog):
    def __init__(self, *args, **kwargs):
        super(ConnectionDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        #TODO set deviceList items

    def getDeviceList(self):
        #TODO define this method
        pass