from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg
import requests

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
        requests.get("http://localhost:5000/shutdown")

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.flask_thread = Flask_server_thread()
        self.configurePlot()

        measurementTimer=QtCore.QTimer(self)
        measurementTimer.start(1000)
        measurementTimer.timeout.connect(self.actionReadTemperature.trigger)

        self.freqMeasurementInputBox.valueChanged['int'].connect(measurementTimer.start)

        self.actionReadTemperature.triggered.connect(self.updateTemperature)

        self.connDialog=ConnectionDialog()

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
        self.getDeviceList()
        if self.connDialog.exec_():
            if self.connDialog.devicesList.currentText():
            	requests.post("http://localhost:5000/open_connection",{"device": self.connDialog.devicesList.currentText()})
            if self.connDialog.paradigmModeButton.isChecked():
                self.settingsBox.setEnabled(False)
            else:
                self.settingsBox.setEnabled(True)
    
    def getDeviceList(self):
        r=requests.get("http://localhost:5000/list_devices")
        devices=r.json()
        return [x["port"] for x in devices]
