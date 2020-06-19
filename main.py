#python -m PyQt5.uic.pyuic -x interface/mainwindow.ui -o interface/design.py
from PyQt5 import QtGui, QtWidgets, QtCore, uic
from server import flask_server
import sys
import requests
from interface.design import Ui_ThermstUtil

class Flask_server_thread(QtCore.QThread):
    port = int(flask_server.os.environ.get("PORT", 5000))
    @QtCore.pyqtSlot()
    def run(self):
        flask_server.app.run(debug=False,host='0.0.0.0',port=self.port)
    @QtCore.pyqtSlot()
    def quit(self):
        requests.get("http://localhost:5000/shutdown")

class MainWindow(QtWidgets.QMainWindow, Ui_ThermstUtil):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.flask_thread = Flask_server_thread()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.flask_thread.start(QtCore.QThread.HighPriority)
    app.exec()
    window.flask_thread.quit()
    sys.exit()
