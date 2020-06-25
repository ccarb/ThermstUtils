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
        self.measurementTimer.timeout.connect(self.actionReadTemperature.trigger)

        self.actionReadTemperature.triggered.connect(self.updateTemperature)

        self.connDialog=ConnectionDialog()
        self.device={}
        self.actionConnectDevice.triggered.connect(self.runConnectionDialog)

        self.temperature=25

        self.actionStart.triggered.connect(self.startDevice)
        self.graphData={'x':[],'y':[]}

    def configurePlot(self):
        color = self.palette().color(QtGui.QPalette.Base)
        self.graphWidget.setBackground(color)
        self.graphWidget.setLabel('bottom', 'Time [s]')
        self.graphWidget.setLabel('left', 'Temperature [ºC]')
        self.graphWidget.setYRange(-10,50)
        pen = pg.mkPen(color=(255, 0, 0), width=2)
        self.plotLine=self.graphWidget.plot([0],[0],pen=pen)

    def updateTemperature(self):
        newTemp=flaskRequests.readTemperature()
        self.temperatureDisplay.setText(newTemp+'ºC')
        self.updateGraph(float(newTemp))

    def updateGraph(self,temperature: float):
        maximumTimeInterval=30
        timeIncrement=self.freqMeasurementInputBox.value()/1000
        if self.graphData["x"]==[]:
            time=0
        else:
            time=self.graphData["x"][-1]+timeIncrement
            if (self.graphData["x"][-1]-self.graphData["x"][0])>maximumTimeInterval:
                self.graphData["x"]=self.graphData["x"][1:]
                self.graphData["y"]=self.graphData["y"][1:]
        self.graphData["x"].append(time)
        self.graphData["y"].append(temperature)
        self.plotLine.setData(self.graphData["x"],self.graphData["y"])
    
    def runConnectionDialog(self):
        self.connDialog.devicesList.clear()
        self.connDialog.devicesList.addItems(self.getDeviceList())
        if self.connDialog.exec_():
            if self.device!={}:
                flaskRequests.closeDevice(self.device)
            if self.connDialog.devicesList.currentText():
                self.device={"device" : self.connDialog.devicesList.currentText()}
                flaskRequests.openDevice(self.device)
                self.measurementTimer.start(self.freqMeasurementInputBox.value())
                self.freqMeasurementInputBox.valueChanged['int'].connect(self.measurementTimer.start)
            if self.connDialog.paradigmModeButton.isChecked():
                self.settingsBox.setEnabled(False)
            else:
                self.settingsBox.setEnabled(True)
    
    def getDeviceList(self):
        devices=flaskRequests.getDevices()
        return [x["port"] for x in devices]

    def startDevice(self):
        if self.modeSelectorColdButton.isChecked:
            settings={ "temperature": str(self.coldTemperatureInputBox.value())}
        if self.modeSelectorHotButton.isChecked:
            settings={ "temperature": str(self.hotTemperatureInputBox.value())}
        flaskRequests.startDevice(settings)
        
        