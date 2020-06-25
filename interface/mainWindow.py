from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg

import interface.flaskRequests as flaskRequests
from interface.designerFiles.mainwindowqtd import Ui_mainWindow
from server import flask_server
from interface.connectionDialog import ConnectionDialog

class Flask_server_thread(QtCore.QThread):
    port = int(flask_server.os.environ.get("PORT", 5000))
    @QtCore.pyqtSlot()
    def run(self):
        flask_server.app.run(debug=False,host='0.0.0.0',port=self.port)
    @QtCore.pyqtSlot()
    def quit(self):
        flaskRequests.shutdownServer()

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.flask_thread = Flask_server_thread()
        self.configurePlot()

        self.measurementTimer=QtCore.QTimer(self)
        self.measurementTimer.start(1000)
        self.measurementTimer.timeout.connect(self.actionReadTemperature.trigger)

        self.freqMeasurementInputBox.valueChanged['int'].connect(self.measurementTimer.start)

        self.actionReadTemperature.triggered.connect(self.updateTemperature)

        self.connDialog=ConnectionDialog()
        self.device={}
        self.actionConnectDevice.triggered.connect(self.runConnectionDialog)

    def configurePlot(self):
        color = self.palette().color(QtGui.QPalette.Base)
        self.graphWidget.setBackground(color)
        pen = pg.mkPen(color=(255, 0, 0), width=2)
        self.graphWidget.plot([0,1,2,3,4,5,6,7,], [1,1,0,0,1,1,0,0], pen=pen)

    def updateTemperature(self):
        self.temperatureDisplay.setText(flask_server.readTemp())
    
    def runConnectionDialog(self):
        self.connDialog.devicesList.clear()
        self.connDialog.devicesList.addItems(self.getDeviceList())
        if self.connDialog.exec_():
            if self.device!={}:
                flaskRequests.closeDevice(self.device)
            if self.connDialog.devicesList.currentText():
                self.device={"device" : self.connDialog.devicesList.currentText()}
                flaskRequests.openDevice(self.device)
            if self.connDialog.paradigmModeButton.isChecked():
                self.settingsBox.setEnabled(False)
            else:
                self.settingsBox.setEnabled(True)
    
    def getDeviceList(self):
        devices=flaskRequests.getDevices()
        return [x["port"] for x in devices]
