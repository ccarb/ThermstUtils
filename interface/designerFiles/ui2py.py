# This Python file uses the following encoding: utf-8

from PyQt5 import uic
def makePyFromUi():
    uifile="interface/designerFiles/mainWindow.ui"
    pyfileName="interface/designerFiles/mainwindowqtd.py"
    pyfile=open(pyfileName,"w")
    print("Translating UI file: "+uifile+" to python module: "+pyfileName+" ...")
    uic.compileUi(uifile,pyfile)
    print("Done")
    uifile="interface/designerFiles/connectionDialog.ui"
    pyfileName="interface/designerFiles/connectiondialogqtd.py"
    pyfile=open(pyfileName,"w")
    print("Translating UI file: "+uifile+" to python module: "+pyfileName+" ...")
    uic.compileUi(uifile,pyfile)
    print("Done")
    uifile="interface/designerFiles/errorDialog.ui"
    pyfileName="interface/designerFiles/errordialogqtd.py"
    pyfile=open(pyfileName,"w")
    print("Translating UI file: "+uifile+" to python module: "+pyfileName+" ...")
    uic.compileUi(uifile,pyfile)
    print("Done")

if __name__ == "__main__":
    makePyFromUi()
