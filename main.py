#python -m PyQt5.uic.pyuic -x interface/mainwindow.ui -o interface/design.py
from PyQt5 import QtGui, QtWidgets, QtCore, uic
from server import flask_server
import sys
import requests
from interface.mainwindow import Ui_mainWindow
import pyqtgraph as pg

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
        self.actionReadTemperature.triggered.connect(self.updateTemperature)

    def configurePlot(self):
        color = self.palette().color(QtGui.QPalette.Base)
        self.graphWidget.setBackground(color)
        pen = pg.mkPen(color=(255, 0, 0), width=2)
        self.graphWidget.plot([0,1,2,3,4,5,6,7,], [1,1,0,0,1,1,0,0], pen=pen)

    def updateTemperature(self):
        self.temperatureDisplay.setText(flask_server.readTemp())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.flask_thread.start(QtCore.QThread.HighPriority)
    app.exec()
    window.flask_thread.quit()
    sys.exit()
