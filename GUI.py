# -*- coding: utf-8 -*-
# Created by: D.Dvorak to project in CTU
# Created by: PyQt5 UI code generator 5.15.4, Qt Creator, PyCharm Community 2022.2
# The project creates time series of measurements and displays shifts
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showMaximized()
        MainWindow.setWindowIcon(QIcon('img/icon.png'))
        MainWindow.setWindowTitle('Time series of levelling measurements (Trimble DINI // Leica LS15 & LS10)')
        self.central = QtWidgets.QWidget(MainWindow)
        self.central.setObjectName("central")
        self.add_button = QtWidgets.QPushButton(self.central)
        self.add_button.setGeometry(QtCore.QRect(60, 900, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.delete_button = QtWidgets.QPushButton(self.central)
        self.delete_button.setGeometry(QtCore.QRect(190, 900, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("add_button")
        self.graph_button = QtWidgets.QPushButton(self.central)
        self.graph_button.setGeometry(QtCore.QRect(320, 900, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graph_button.setFont(font)
        self.graph_button.setObjectName("graph_button")
        self.exp = QtWidgets.QPushButton(self.central)
        self.exp.setGeometry(QtCore.QRect(450, 900, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exp.setFont(font)
        self.exp.setObjectName("exp")
        self.table = QtWidgets.QTableWidget(self.central)
        self.table.setGeometry(QtCore.QRect(60, 80, 1800, 800))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.db_name = QtWidgets.QLabel(self.central)
        self.db_name.setGeometry(QtCore.QRect(60, 20, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.db_name.setFont(font)
        self.db_name.setObjectName("db_name")
        self.db_name_text = QtWidgets.QLabel(self.central)
        self.db_name_text.setGeometry(QtCore.QRect(160, 20, 500, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.db_name_text.setFont(font)
        self.db_name_text.setText("Levelling.db --sqlite3")
        self.db_name_text.setObjectName("db_name_text")
        MainWindow.setCentralWidget(self.central)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.add_button.setText(_translate("MainWindow", "Add data"))
        self.delete_button.setText(_translate("MainWindow", "Delete data"))
        self.graph_button.setText(_translate("MainWindow", "Graph"))
        self.exp.setText(_translate("MainWindow", "Export"))
        self.db_name.setText(_translate("MainWindow", "DB name:"))

