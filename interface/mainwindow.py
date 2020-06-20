# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\Ceci\Documents\Facu\ThermstUtils\interface\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settingsBox = QtWidgets.QGroupBox(self.centralWidget)
        self.settingsBox.setMinimumSize(QtCore.QSize(300, 0))
        self.settingsBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.settingsBox.setLocale(QtCore.QLocale(QtCore.QLocale.Slovak, QtCore.QLocale.Slovakia))
        self.settingsBox.setObjectName("settingsBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.settingsBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.modeSelectorLayout = QtWidgets.QHBoxLayout()
        self.modeSelectorLayout.setObjectName("modeSelectorLayout")
        self.modeSelectorLabel = QtWidgets.QLabel(self.settingsBox)
        self.modeSelectorLabel.setObjectName("modeSelectorLabel")
        self.modeSelectorLayout.addWidget(self.modeSelectorLabel)
        self.modeSelectorHotButton = QtWidgets.QRadioButton(self.settingsBox)
        self.modeSelectorHotButton.setObjectName("modeSelectorHotButton")
        self.modeSelectorLayout.addWidget(self.modeSelectorHotButton)
        self.modeSelectorColdButton = QtWidgets.QRadioButton(self.settingsBox)
        self.modeSelectorColdButton.setChecked(True)
        self.modeSelectorColdButton.setObjectName("modeSelectorColdButton")
        self.modeSelectorLayout.addWidget(self.modeSelectorColdButton)
        self.verticalLayout.addLayout(self.modeSelectorLayout)
        self.setHotTemperatureLayout = QtWidgets.QHBoxLayout()
        self.setHotTemperatureLayout.setObjectName("setHotTemperatureLayout")
        self.hotTemperatureLabel = QtWidgets.QLabel(self.settingsBox)
        self.hotTemperatureLabel.setObjectName("hotTemperatureLabel")
        self.setHotTemperatureLayout.addWidget(self.hotTemperatureLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.setHotTemperatureLayout.addItem(spacerItem)
        self.hotTemperatureInputBox = QtWidgets.QSpinBox(self.settingsBox)
        self.hotTemperatureInputBox.setMinimum(-10)
        self.hotTemperatureInputBox.setMaximum(50)
        self.hotTemperatureInputBox.setObjectName("hotTemperatureInputBox")
        self.setHotTemperatureLayout.addWidget(self.hotTemperatureInputBox)
        self.hotTempCelsiusLabel = QtWidgets.QLabel(self.settingsBox)
        self.hotTempCelsiusLabel.setObjectName("hotTempCelsiusLabel")
        self.setHotTemperatureLayout.addWidget(self.hotTempCelsiusLabel)
        self.verticalLayout.addLayout(self.setHotTemperatureLayout)
        self.setColdTemperatureLayout = QtWidgets.QHBoxLayout()
        self.setColdTemperatureLayout.setObjectName("setColdTemperatureLayout")
        self.coldTemperatureLabel = QtWidgets.QLabel(self.settingsBox)
        self.coldTemperatureLabel.setObjectName("coldTemperatureLabel")
        self.setColdTemperatureLayout.addWidget(self.coldTemperatureLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.setColdTemperatureLayout.addItem(spacerItem1)
        self.coldTemperatureInputBox = QtWidgets.QSpinBox(self.settingsBox)
        self.coldTemperatureInputBox.setMinimum(-10)
        self.coldTemperatureInputBox.setMaximum(50)
        self.coldTemperatureInputBox.setObjectName("coldTemperatureInputBox")
        self.setColdTemperatureLayout.addWidget(self.coldTemperatureInputBox)
        self.coldTempCelsiusLabel = QtWidgets.QLabel(self.settingsBox)
        self.coldTempCelsiusLabel.setObjectName("coldTempCelsiusLabel")
        self.setColdTemperatureLayout.addWidget(self.coldTempCelsiusLabel)
        self.verticalLayout.addLayout(self.setColdTemperatureLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.settingsBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.spinBox = QtWidgets.QSpinBox(self.settingsBox)
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.label_2 = QtWidgets.QLabel(self.settingsBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.restorePresetsButton = QtWidgets.QPushButton(self.settingsBox)
        self.restorePresetsButton.setObjectName("restorePresetsButton")
        self.verticalLayout.addWidget(self.restorePresetsButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.settingsBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.temperatureDisplay = QtWidgets.QLabel(self.settingsBox)
        self.temperatureDisplay.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperatureDisplay.sizePolicy().hasHeightForWidth())
        self.temperatureDisplay.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 191, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 159, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 63, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 84, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 63, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 191, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 159, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 63, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 84, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 63, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 63, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 191, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 159, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 63, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 84, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 63, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 63, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.temperatureDisplay.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.temperatureDisplay.setFont(font)
        self.temperatureDisplay.setMouseTracking(True)
        self.temperatureDisplay.setAutoFillBackground(True)
        self.temperatureDisplay.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.temperatureDisplay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temperatureDisplay.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temperatureDisplay.setText("28ºC")
        self.temperatureDisplay.setTextFormat(QtCore.Qt.PlainText)
        self.temperatureDisplay.setScaledContents(False)
        self.temperatureDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatureDisplay.setObjectName("temperatureDisplay")
        self.verticalLayout.addWidget(self.temperatureDisplay, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.startButton = QtWidgets.QPushButton(self.settingsBox)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.settingsBox)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout.addWidget(self.stopButton)
        self.horizontalLayout.addWidget(self.settingsBox)
        self.displayTabs = QtWidgets.QTabWidget(self.centralWidget)
        self.displayTabs.setAutoFillBackground(True)
        self.displayTabs.setTabPosition(QtWidgets.QTabWidget.South)
        self.displayTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.displayTabs.setElideMode(QtCore.Qt.ElideNone)
        self.displayTabs.setObjectName("displayTabs")
        self.logTab = QtWidgets.QWidget()
        self.logTab.setObjectName("logTab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.logTab)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logDisplayBox = QtWidgets.QTextBrowser(self.logTab)
        self.logDisplayBox.setAutoFillBackground(True)
        self.logDisplayBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logDisplayBox.setObjectName("logDisplayBox")
        self.horizontalLayout_3.addWidget(self.logDisplayBox)
        self.displayTabs.addTab(self.logTab, "")
        self.graphTab = QtWidgets.QWidget()
        self.graphTab.setObjectName("graphTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.graphTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphWidget = PlotWidget(self.graphTab)
        self.graphWidget.setAutoFillBackground(False)
        self.graphWidget.setObjectName("graphWidget")
        self.horizontalLayout_2.addWidget(self.graphWidget)
        self.displayTabs.addTab(self.graphTab, "")
        self.horizontalLayout.addWidget(self.displayTabs)
        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuConnect_Device = QtWidgets.QMenu(self.menuBar)
        self.menuConnect_Device.setObjectName("menuConnect_Device")
        mainWindow.setMenuBar(self.menuBar)
        self.actionStart = QtWidgets.QAction(mainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(mainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionSetHotMode = QtWidgets.QAction(mainWindow)
        self.actionSetHotMode.setObjectName("actionSetHotMode")
        self.actionSetColdMode = QtWidgets.QAction(mainWindow)
        self.actionSetColdMode.setObjectName("actionSetColdMode")
        self.actionSetHotTemperature = QtWidgets.QAction(mainWindow)
        self.actionSetHotTemperature.setObjectName("actionSetHotTemperature")
        self.actionSetColdTemperature = QtWidgets.QAction(mainWindow)
        self.actionSetColdTemperature.setObjectName("actionSetColdTemperature")
        self.actionRestorePresets = QtWidgets.QAction(mainWindow)
        self.actionRestorePresets.setObjectName("actionRestorePresets")
        self.actionUserManual = QtWidgets.QAction(mainWindow)
        self.actionUserManual.setObjectName("actionUserManual")
        self.actionAboutThermstUtil = QtWidgets.QAction(mainWindow)
        self.actionAboutThermstUtil.setObjectName("actionAboutThermstUtil")
        self.actionReadTemperature = QtWidgets.QAction(mainWindow)
        self.actionReadTemperature.setObjectName("actionReadTemperature")
        self.actionConnectDevice = QtWidgets.QAction(mainWindow)
        self.actionConnectDevice.setObjectName("actionConnectDevice")
        self.menuHelp.addAction(self.actionUserManual)
        self.menuHelp.addAction(self.actionAboutThermstUtil)
        self.menuConnect_Device.addAction(self.actionConnectDevice)
        self.menuBar.addAction(self.menuConnect_Device.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        self.displayTabs.setCurrentIndex(1)
        self.startButton.clicked.connect(self.actionStart.trigger)
        self.stopButton.clicked.connect(self.actionStop.trigger)
        self.hotTemperatureInputBox.valueChanged['int'].connect(self.actionSetHotTemperature.trigger)
        self.coldTemperatureInputBox.valueChanged['int'].connect(self.actionSetColdTemperature.trigger)
        self.modeSelectorHotButton.clicked.connect(self.actionSetHotMode.trigger)
        self.modeSelectorColdButton.clicked.connect(self.actionSetColdMode.trigger)
        self.actionReadTemperature.triggered.connect(self.temperatureDisplay.clear)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Thermal Stimulator"))
        self.settingsBox.setTitle(_translate("mainWindow", "Settings"))
        self.modeSelectorLabel.setText(_translate("mainWindow", "Mode:"))
        self.modeSelectorHotButton.setText(_translate("mainWindow", "Hot"))
        self.modeSelectorColdButton.setText(_translate("mainWindow", "Cold"))
        self.hotTemperatureLabel.setText(_translate("mainWindow", "Hot Temperature:"))
        self.hotTempCelsiusLabel.setText(_translate("mainWindow", "ºC"))
        self.coldTemperatureLabel.setText(_translate("mainWindow", "Cold Temperature:"))
        self.coldTempCelsiusLabel.setText(_translate("mainWindow", "ºC"))
        self.label_3.setText(_translate("mainWindow", "Measurment Frecuency:"))
        self.label_2.setText(_translate("mainWindow", "ms"))
        self.restorePresetsButton.setText(_translate("mainWindow", "Restore presets"))
        self.label.setText(_translate("mainWindow", "Temperatura Actual:"))
        self.temperatureDisplay.setProperty("temperature", _translate("mainWindow", "28ºC"))
        self.startButton.setText(_translate("mainWindow", "Start"))
        self.stopButton.setText(_translate("mainWindow", "Stop"))
        self.logDisplayBox.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">Logs are stored in &quot;Logs&quot; folder, named after this application execution time and date</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ff0000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Connecting...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Conection succesful!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Awaiting comands</span></p></body></html>"))
        self.displayTabs.setTabText(self.displayTabs.indexOf(self.logTab), _translate("mainWindow", "Log"))
        self.displayTabs.setTabText(self.displayTabs.indexOf(self.graphTab), _translate("mainWindow", "Graph"))
        self.menuHelp.setTitle(_translate("mainWindow", "Help"))
        self.menuConnect_Device.setTitle(_translate("mainWindow", "Connection"))
        self.actionStart.setText(_translate("mainWindow", "Start"))
        self.actionStop.setText(_translate("mainWindow", "Stop"))
        self.actionSetHotMode.setText(_translate("mainWindow", "Set Hot Mode"))
        self.actionSetHotMode.setToolTip(_translate("mainWindow", "Set Hot Mode"))
        self.actionSetColdMode.setText(_translate("mainWindow", "Set Cold Mode"))
        self.actionSetColdMode.setToolTip(_translate("mainWindow", "Set Cold Mode"))
        self.actionSetHotTemperature.setText(_translate("mainWindow", "Set Hot Temperature"))
        self.actionSetHotTemperature.setToolTip(_translate("mainWindow", "Set Hot Temperature"))
        self.actionSetColdTemperature.setText(_translate("mainWindow", "Set Cold Temperature"))
        self.actionRestorePresets.setText(_translate("mainWindow", "Restore Presets"))
        self.actionRestorePresets.setToolTip(_translate("mainWindow", "Restore Presets"))
        self.actionUserManual.setText(_translate("mainWindow", "User Manual"))
        self.actionAboutThermstUtil.setText(_translate("mainWindow", "About ThermstUtil"))
        self.actionReadTemperature.setText(_translate("mainWindow", "ReadTemperature"))
        self.actionConnectDevice.setText(_translate("mainWindow", "Connect Device..."))
from pyqtgraph import PlotWidget
from resources import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())