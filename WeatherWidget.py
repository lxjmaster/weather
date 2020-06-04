# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Weather(object):
    def setupUi(self, Weather):
        Weather.setObjectName("Weather")
        Weather.resize(466, 315)
        Weather.setMinimumSize(QtCore.QSize(466, 315))
        Weather.setMaximumSize(QtCore.QSize(466, 315))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/app2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Weather.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Weather)
        self.groupBox.setGeometry(QtCore.QRect(40, 10, 381, 211))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 221, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CityLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.CityLabel.setFont(font)
        self.CityLabel.setObjectName("CityLabel")
        self.horizontalLayout.addWidget(self.CityLabel)
        self.CityEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.CityEdit.setObjectName("CityEdit")
        self.horizontalLayout.addWidget(self.CityEdit)
        self.WeatherResult = QtWidgets.QTextEdit(self.groupBox)
        self.WeatherResult.setGeometry(QtCore.QRect(30, 70, 321, 121))
        self.WeatherResult.setObjectName("WeatherResult")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Weather)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 250, 271, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Clear = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Clear.setObjectName("Clear")
        self.horizontalLayout_2.addWidget(self.Clear)
        self.Search = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Search.setObjectName("Search")
        self.horizontalLayout_2.addWidget(self.Search)

        self.retranslateUi(Weather)
        self.Clear.clicked.connect(self.WeatherResult.clear)
        QtCore.QMetaObject.connectSlotsByName(Weather)

    def retranslateUi(self, Weather):
        _translate = QtCore.QCoreApplication.translate
        Weather.setWindowTitle(_translate("Weather", "天气查询"))
        self.groupBox.setTitle(_translate("Weather", "天气查询"))
        self.CityLabel.setText(_translate("Weather", "城市:"))
        self.Clear.setText(_translate("Weather", "清空"))
        self.Search.setText(_translate("Weather", "查询"))

import src_rc
