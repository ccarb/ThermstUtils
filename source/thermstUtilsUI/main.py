# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_ThermstUtil(QtWidgets.QMainWindow):

    def setupUi(self, ThermstUtil):
        ThermstUtil.setObjectName("ThermstUtil")
        ThermstUtil.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(ThermstUtil)
        self.centralWidget.setObjectName("centralWidget")
        # Display tabs set up
        self.displayTabs = QtWidgets.QTabWidget(self.centralWidget)
        self.displayTabs.setGeometry(QtCore.QRect(320, 30, 471, 521))
        self.displayTabs.setAutoFillBackground(True)
        self.displayTabs.setTabPosition(QtWidgets.QTabWidget.South)
        self.displayTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.displayTabs.setElideMode(QtCore.Qt.ElideNone)
        self.displayTabs.setObjectName("displayTabs")
        self.logTab = QtWidgets.QWidget()
        self.logTab.setObjectName("logTab")
        self.logDisplayBox = QtWidgets.QTextBrowser(self.logTab)
        self.logDisplayBox.setGeometry(QtCore.QRect(0, 0, 465, 496))
        self.logDisplayBox.setObjectName("logDisplayBox")
        self.displayTabs.addTab(self.logTab, "")
        self.graphTab = QtWidgets.QWidget()
        self.graphTab.setObjectName("graphTab")
        self.displayTabs.addTab(self.graphTab, "")
        # Dock set up
        self.settingsButton = QtWidgets.QPushButton(self.centralWidget)
        self.settingsButton.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.settingsButton.setObjectName("settingsButton")
        self.settingsDock = QtWidgets.QDockWidget(self.centralWidget)
        self.settingsDock.setGeometry(QtCore.QRect(10, 10, 300, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsDock.sizePolicy().hasHeightForWidth())
        self.settingsDock.setSizePolicy(sizePolicy)
        self.settingsDock.setMinimumSize(QtCore.QSize(300, 38))
        self.settingsDock.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)
        self.settingsDock.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.LeftDockWidgetArea)
        self.settingsDock.setObjectName("settingsDock")
        self.settingsDockContents = QtWidgets.QWidget()
        self.settingsDockContents.setObjectName("settingsDockContents")
        self.stopButton = QtWidgets.QPushButton(self.settingsDockContents)
        self.stopButton.setGeometry(QtCore.QRect(0, 490, 301, 23))
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.settingsDockContents)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 0, 301, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.modeSelectorLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.modeSelectorLayout.setContentsMargins(0, 0, 0, 0)
        self.modeSelectorLayout.setObjectName("modeSelectorLayout")
        self.modeSelectorLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.modeSelectorLabel.setObjectName("modeSelectorLabel")
        self.modeSelectorLayout.addWidget(self.modeSelectorLabel)
        self.modeSelectorHotButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.modeSelectorHotButton.setObjectName("modeSelectorHotButton")
        self.modeSelectorLayout.addWidget(self.modeSelectorHotButton)
        self.modeSelectorColdButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.modeSelectorColdButton.setChecked(True)
        self.modeSelectorColdButton.setObjectName("modeSelectorColdButton")
        self.modeSelectorLayout.addWidget(self.modeSelectorColdButton)
        self.coldTemperatureLabel = QtWidgets.QLabel(self.settingsDockContents)
        self.coldTemperatureLabel.setGeometry(QtCore.QRect(0, 60, 101, 21))
        self.coldTemperatureLabel.setObjectName("coldTemperatureLabel")
        self.hotTemperatureLabel = QtWidgets.QLabel(self.settingsDockContents)
        self.hotTemperatureLabel.setGeometry(QtCore.QRect(0, 30, 91, 21))
        self.hotTemperatureLabel.setObjectName("hotTemperatureLabel")
        self.startButton = QtWidgets.QPushButton(self.settingsDockContents)
        self.startButton.setGeometry(QtCore.QRect(0, 460, 301, 23))
        self.startButton.setObjectName("startButton")
        self.restorePresetsButton = QtWidgets.QPushButton(self.settingsDockContents)
        self.restorePresetsButton.setGeometry(QtCore.QRect(0, 90, 301, 23))
        self.restorePresetsButton.setObjectName("restorePresetsButton")
        self.hotTemperatureInputBox = QtWidgets.QSpinBox(self.settingsDockContents)
        self.hotTemperatureInputBox.setGeometry(QtCore.QRect(110, 30, 51, 22))
        self.hotTemperatureInputBox.setMinimum(-10)
        self.hotTemperatureInputBox.setMaximum(50)
        self.hotTemperatureInputBox.setValue(35)
        self.hotTemperatureInputBox.setObjectName("hotTemperatureInputBox")
        self.coldTemperatureInputBox = QtWidgets.QSpinBox(self.settingsDockContents)
        self.coldTemperatureInputBox.setGeometry(QtCore.QRect(110, 60, 51, 22))
        self.coldTemperatureInputBox.setMinimum(-10)
        self.coldTemperatureInputBox.setMaximum(50)
        self.coldTemperatureInputBox.setValue(10)
        self.coldTemperatureInputBox.setObjectName("coldTemperatureInputBox")
        self.hotTempCelsiusLabel = QtWidgets.QLabel(self.settingsDockContents)
        self.hotTempCelsiusLabel.setGeometry(QtCore.QRect(170, 30, 31, 21))
        self.hotTempCelsiusLabel.setObjectName("hotTempCelsiusLabel")
        self.coldTempCelsiusLabel = QtWidgets.QLabel(self.settingsDockContents)
        self.coldTempCelsiusLabel.setGeometry(QtCore.QRect(170, 60, 31, 21))
        self.coldTempCelsiusLabel.setObjectName("coldTempCelsiusLabel")
        self.settingsDock.setWidget(self.settingsDockContents)
        # Central widget set up
        ThermstUtil.setCentralWidget(self.centralWidget)
        # Menu set up
        self.menuBar = QtWidgets.QMenuBar(ThermstUtil)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        ThermstUtil.setMenuBar(self.menuBar)
        # Status bar set up
        self.statusbar = QtWidgets.QStatusBar(ThermstUtil)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        ThermstUtil.setStatusBar(self.statusbar)
        # Actions definition
        self.actionSettings = QtWidgets.QAction(ThermstUtil)
        self.actionSettings.setObjectName("actionSettings")
        self.actionGraph = QtWidgets.QAction(ThermstUtil)
        self.actionGraph.setObjectName("actionGraph")
        self.actionLog = QtWidgets.QAction(ThermstUtil)
        self.actionLog.setObjectName("actionLog")
        self.actionStart = QtWidgets.QAction(ThermstUtil)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(ThermstUtil)
        self.actionStop.setObjectName("actionStop")
        self.actionSetHotMode = QtWidgets.QAction(ThermstUtil)
        self.actionSetHotMode.setObjectName("actionSetHotMode")
        self.actionSetColdMode = QtWidgets.QAction(ThermstUtil)
        self.actionSetColdMode.setObjectName("actionSetColdMode")
        self.actionSetHotTemperature = QtWidgets.QAction(ThermstUtil)
        self.actionSetHotTemperature.setObjectName("actionSetHotTemperature")
        self.actionSetColdTemperature = QtWidgets.QAction(ThermstUtil)
        self.actionSetColdTemperature.setObjectName("actionSetColdTemperature")
        self.actionRestorePresets = QtWidgets.QAction(ThermstUtil)
        self.actionRestorePresets.setObjectName("actionRestorePresets")
        self.actionUserManual = QtWidgets.QAction(ThermstUtil)
        self.actionUserManual.setObjectName("actionUserManual")
        self.actionAboutThermstUtil = QtWidgets.QAction(ThermstUtil)
        self.actionAboutThermstUtil.setObjectName("actionAboutThermstUtil")

        # Adition of actions to menu
        self.menuView.addAction(self.actionSettings)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionGraph)
        self.menuView.addAction(self.actionLog)
        self.menuHelp.addAction(self.actionUserManual)
        self.menuHelp.addAction(self.actionAboutThermstUtil)
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        # Adding language strings
        self.retranslateUi(ThermstUtil)
        # Selecting predifined startup tab
        self.displayTabs.setCurrentIndex(0)
        # Conection of signals to slots
        self.settingsButton.clicked.connect(self.settingsDock.show)
        self.startButton.clicked.connect(self.actionStart.trigger)
        self.stopButton.clicked.connect(self.actionStop.trigger)
        self.modeSelectorColdButton.clicked.connect(self.actionSetColdMode.trigger)
        self.modeSelectorHotButton.clicked.connect(self.actionSetHotMode.trigger)
        self.restorePresetsButton.clicked.connect(self.actionRestorePresets.trigger)
        self.hotTemperatureInputBox.valueChanged['int'].connect(self.actionSetHotTemperature.trigger)
        self.coldTemperatureInputBox.valueChanged['int'].connect(self.actionSetColdTemperature.trigger)
        self.settingsDock.visibilityChanged.connect(self.resizeDisplayTabWindow)
        self.actionLog.triggered.connect(self.showLogTab)
        self.actionGraph.triggered.connect(self.showGraphTab)
        self.actionSettings.triggered.connect(self.toggleSettingsDockVisibility)
        self.actionRestorePresets.triggered.connect(self.restorePresets)
        QtCore.QMetaObject.connectSlotsByName(ThermstUtil)

    def showLogTab(self):
        self.displayTabs.setCurrentIndex(0)

    def showGraphTab(self):
        self.displayTabs.setCurrentIndex(1)

    def toggleSettingsDockVisibility(self):
        if self.settingsDock.isVisible():
            self.settingsDock.hide()
        else:
            self.settingsDock.show()

    def restorePresets(self):
        self.modeSelectorColdButton.toggle()
        self.hotTemperatureInputBox.setValue(35)
        self.coldTemperatureInputBox.setValue(10)

    def resizeDisplayTabWindow(self):
        if self.settingsDock.isVisible():
            self.displayTabs.setGeometry(QtCore.QRect(320, 30, 471, 521))
            self.logDisplayBox.setGeometry(QtCore.QRect(0, 0, 465, 496))
        else:
            self.displayTabs.setGeometry(QtCore.QRect(10, 30, 781, 521))
            self.logDisplayBox.setGeometry(QtCore.QRect(0, 0, 775, 496))

    def retranslateUi(self, ThermstUtil):
        _translate = QtCore.QCoreApplication.translate
        ThermstUtil.setWindowTitle(_translate("ThermstUtil", "MainWindow"))
        self.logDisplayBox.setHtml(_translate("ThermstUtil", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">connected successfuly</span></p></body></html>"))
        self.displayTabs.setTabText(self.displayTabs.indexOf(self.logTab), _translate("ThermstUtil", "Log"))
        self.displayTabs.setTabText(self.displayTabs.indexOf(self.graphTab), _translate("ThermstUtil", "Graph"))
        self.settingsButton.setText(_translate("ThermstUtil", "Settings"))
        self.settingsDock.setWindowTitle(_translate("ThermstUtil", "Settings"))
        self.stopButton.setText(_translate("ThermstUtil", "Stop"))
        self.modeSelectorLabel.setText(_translate("ThermstUtil", "Mode:"))
        self.modeSelectorHotButton.setText(_translate("ThermstUtil", "Hot"))
        self.modeSelectorColdButton.setText(_translate("ThermstUtil", "Cold"))
        self.coldTemperatureLabel.setText(_translate("ThermstUtil", "Cold Temperature:"))
        self.hotTemperatureLabel.setText(_translate("ThermstUtil", "Hot Temperature:"))
        self.startButton.setText(_translate("ThermstUtil", "Start"))
        self.restorePresetsButton.setText(_translate("ThermstUtil", "Restore presets"))
        self.hotTempCelsiusLabel.setText(_translate("ThermstUtil", "ºC"))
        self.coldTempCelsiusLabel.setText(_translate("ThermstUtil", "ºC"))
        self.menuView.setTitle(_translate("ThermstUtil", "View"))
        self.menuHelp.setTitle(_translate("ThermstUtil", "Help"))
        self.actionSettings.setText(_translate("ThermstUtil", "Show/Hide Settings"))
        self.actionGraph.setText(_translate("ThermstUtil", "Graph"))
        self.actionLog.setText(_translate("ThermstUtil", "Log"))
        self.actionStart.setText(_translate("ThermstUtil", "Start"))
        self.actionStop.setText(_translate("ThermstUtil", "Stop"))
        self.actionSetHotMode.setText(_translate("ThermstUtil", "Set Hot Mode"))
        self.actionSetHotMode.setToolTip(_translate("ThermstUtil", "Set Hot Mode"))
        self.actionSetColdMode.setText(_translate("ThermstUtil", "Set Cold Mode"))
        self.actionSetColdMode.setToolTip(_translate("ThermstUtil", "Set Cold Mode"))
        self.actionSetHotTemperature.setText(_translate("ThermstUtil", "Set Hot Temperature"))
        self.actionSetHotTemperature.setToolTip(_translate("ThermstUtil", "Set Hot Temperature"))
        self.actionSetColdTemperature.setText(_translate("ThermstUtil", "Set Cold Temperature"))
        self.actionRestorePresets.setText(_translate("ThermstUtil", "Restore Presets"))
        self.actionRestorePresets.setToolTip(_translate("ThermstUtil", "Restore Presets"))
        self.actionUserManual.setText(_translate("ThermstUtil", "User Manual"))
        self.actionAboutThermstUtil.setText(_translate("ThermstUtil", "About ThermstUtil"))



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_ThermstUtil()
    window.setupUi(window)
    window.show()
    sys.exit(app.exec_())
