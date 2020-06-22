#python -m PyQt5.uic.pyuic -x interface/mainwindow.ui -o interface/design.py
from PyQt5 import QtCore, QtWidgets
import sys
import interface.flaskRequests as flaskRequests
from interface.mainWindow import MainWindow
from interface.connectionDialog import ConnectionDialog

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.flask_thread.start(QtCore.QThread.HighPriority)
    app.exec()
    if window.device!={}:
        flaskRequests.closeDevice(window.device)
    window.flask_thread.quit()
    sys.exit()
