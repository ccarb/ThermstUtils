from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg
import os

from config import *
import interface.flaskRequests as flaskRequests
from interface.designerFiles.mainwindowqtd import Ui_mainWindow
from server import flask_server
from interface.connectionDialog import ConnectionDialog
from interface.errorDialog import ErrorDialog

class Flask_server_thread(QtCore.QThread):
    port = int(flask_server.os.environ.get("PORT", 5000))
    @QtCore.pyqtSlot()
    def run(self):
        flask_server.app.run(debug=False,host='0.0.0.0',port=self.port, threaded=False)
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
        self.actionDisconnect_Device.triggered.connect(self.disconnectDevice)

        self.errDialog=ErrorDialog()

        self.temperature=25

        self.actionStart.triggered.connect(self.startDevice)
        self.actionStop.triggered.connect(self.stopDevice)
        self.actionUserManual.triggered.connect(self.openUserManual)
        self.actionExamples.triggered.connect(self.openExamples)

        self.graphData={'x':[],'y':[]}

    def configurePlot(self):
        color = self.palette().color(QtGui.QPalette.Base)
        self.graphWidget.setBackground(color)
        self.graphWidget.setLabel('bottom', 'Time [s]')
        self.graphWidget.setLabel('left', 'Temperature [ºC]')
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setYRange(0,60)
        self.graphWidget.setMouseEnabled(x=False, y=False)
        self.graphWidget.setMenuEnabled(False)
        pen = pg.mkPen(color=(255, 0, 0), width=2)
        self.plotDesiredTemp = self.graphWidget.plot([0],[0], pen=pg.mkPen(color=(0, 0, 255), width=2, style=QtCore.Qt.DashLine))
        self.plotLine=self.graphWidget.plot([0],[0],pen=pen)
        ticks = range(0, 65, 5)
        ticks = [list(zip(ticks, ticks))]
        self.graphWidget.getPlotItem().getAxis('left').setTicks(ticks)
        
    def updateTemperature(self):
        response = flaskRequests.readTemperature()
        if response.get("error") == "ServerError": return self.communicationError()
        newTemp = float(response["temperature"])
        target_temp = response.get("status", {}).get("target_temperature")
        target_temp = float(target_temp) if not target_temp == None else -99
        self.updateGraph(newTemp, target_temp)
        newTemp = "{T:.1f}".format(T=newTemp)
        self.temperatureDisplay.setText(newTemp + 'ºC')
        self.updateStatus(response["status"])
    
    def updateStatus(self, status):
        device = status.get("device")
        if device == None:
            self.SerialIndicatorIcon.setPixmap(QtGui.QPixmap(":/icons/serial_off.png"))
        else:
            self.SerialIndicatorIcon.setPixmap(QtGui.QPixmap(":/icons/serial_on.png"))

        mode = status.get("operation_mode", None)
        if mode == None:
            self.OperationModeIcon.setPixmap(QtGui.QPixmap(":/icons/off.png"))
        elif mode == "hot":
            self.OperationModeIcon.setPixmap(QtGui.QPixmap(":/icons/danger.png"))
        else:
            self.OperationModeIcon.setPixmap(QtGui.QPixmap(":/icons/cold.png"))
        
        status_description = status.get("status_descriptions", {}).get("status")
        if status_description == None:
            self.StatusText.setText("Off")
        else:
            self.StatusText.setText(status_description)
        
        status_error = status.get("status_codes", {}).get("error")
        if not status_error == 0:
            self.StatusIcon.setPixmap(QtGui.QPixmap(":/icons/danger.png"))
            self.measurementTimer.stop()
            self.errDialog.errorDiagInfoLabel.setText(self.parse_error_descriptions(status))
            self.errDialog.exec_()
            flaskRequests.closeDevice(self.device)
            self.close()

    def parse_error_descriptions(self, status):
        errors = status.get("status_descriptions", {}).get("error")
        return '\n'.join(errors)

    def updateGraph(self,temperature: float, target_temp=25.0):
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
        self.plotDesiredTemp.setData(self.graphData["x"], [target_temp]*len(self.graphData["x"]))
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
                status = flaskRequests.apiStatus()
                if status.get("status_codes", {}).get("error") == 0:
                    self.measurementTimer.start(self.freqMeasurementInputBox.value())
                    self.freqMeasurementInputBox.valueChanged['int'].connect(self.measurementTimer.start)
                    if self.connDialog.paradigmModeButton.isChecked():
                        self.settingsBox.setEnabled(False)
                    else:
                        self.settingsBox.setEnabled(True)
                else:
                    flaskRequests.closeDevice(self.device)
                    self.device = {}
                    self.errDialog.errorDiagInfoLabel.setText("Device not found at selected port.")
                    self.errDialog.exec_()

    
    def disconnectDevice(self):
        if self.device == {}: return False
        flaskRequests.closeDevice(self.device)
        self.freqMeasurementInputBox.valueChanged['int'].disconnect(self.measurementTimer.start)
        self.measurementTimer.stop()
        self.SerialIndicatorIcon.setPixmap(QtGui.QPixmap(":/icons/serial_off.png"))
        self.OperationModeIcon.setPixmap(QtGui.QPixmap(":/icons/off.png"))
        self.StatusText.setText("Off")
        self.device == {}
        return True
    
    def getDeviceList(self):
        devices=flaskRequests.getDevices()
        return [x["port"] for x in devices]
        

    def startDevice(self):
        temperature=self.temperatureInputBox.value()
        settings={ "objective_temperature": str(temperature)}
        if self.modeSelectorHotButton.isChecked():
            flaskRequests.hot(settings)
        else:
            flaskRequests.cold(settings)
    
    def stopDevice(self):
        flaskRequests.stopTemp()
    
    def communicationError(self):
        pass

    def openUserManual(self):
        path = os.path.abspath("docs/Manual.pdf")
        os.startfile(path, 'open')
    
    def openExamples(self):
        path = os.path.abspath("examples/exampleParadigm.m")
        os.startfile(path, 'open')
