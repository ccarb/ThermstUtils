import os

def makePyFromQrt():
    print("Building resources module")
    os.system('python -m PyQt5.pyrcc_main -o ./"resources_rc.py" resources/resources.qrc')
    print("Done")

if __name__ == "__main__":
    makePyFromQrt()