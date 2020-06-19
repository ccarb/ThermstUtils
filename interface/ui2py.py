# This Python file uses the following encoding: utf-8

from PyQt5 import uic

if __name__ == "__main__":
    uifile="mainwindow.ui"
    pyfileName="mainwindow.py"
    pyfile=open(pyfileName,"w")
    print("Translating UI file: "+uifile+" to python module: "+pyfileName+" ...")
    uic.compileUi(uifile,pyfile)
    print("Done")
