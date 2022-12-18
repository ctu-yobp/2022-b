# -*- coding: utf-8 -*-
# Created by: D.Dvorak to project in CTU
# Created by: PyQt5 UI code generator 5.15.4, Qt Creator, PyCharm Community 2022.2
# The project creates time series of measurements and displays shifts

# Library of functions
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# Graphics
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.central = QtWidgets.QWidget(MainWindow)
        self.central.setObjectName("central")
        self.action = QtWidgets.QPushButton(self.central)
        self.action.setGeometry(QtCore.QRect(50, 500, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action.setFont(font)
        self.action.setObjectName("action")
        self.add_button = QtWidgets.QPushButton(self.central)
        self.add_button.setGeometry(QtCore.QRect(192, 500, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.graph_button = QtWidgets.QPushButton(self.central)
        self.graph_button.setGeometry(QtCore.QRect(320, 500, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graph_button.setFont(font)
        self.graph_button.setObjectName("graph_button")
        self.exp = QtWidgets.QPushButton(self.central)
        self.exp.setGeometry(QtCore.QRect(470, 500, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exp.setFont(font)
        self.exp.setObjectName("exp")
        self.table = QtWidgets.QTableWidget(self.central)
        self.table.setGeometry(QtCore.QRect(50, 90, 691, 391))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.coordinates_button = QtWidgets.QPushButton(self.central)
        self.coordinates_button.setGeometry(QtCore.QRect(620, 500, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coordinates_button.setFont(font)
        self.coordinates_button.setObjectName("coordinates_button")
        self.fix_label = QtWidgets.QLabel(self.central)
        self.fix_label.setGeometry(QtCore.QRect(40, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.fix_label.setFont(font)
        self.fix_label.setObjectName("fix_label")
        self.name_of_action = QtWidgets.QLabel(self.central)
        self.name_of_action.setGeometry(QtCore.QRect(180, 20, 561, 41))
        self.name_of_action.setText("")
        self.name_of_action.setObjectName("name_of_action")
        MainWindow.setCentralWidget(self.central)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.action.setText(_translate("MainWindow", "Výběr action"))
        self.add_button.setText(_translate("MainWindow", "Přidat data"))
        self.graph_button.setText(_translate("MainWindow", "graph_button"))
        self.exp.setText(_translate("MainWindow", "Export"))
        self.coordinates_button.setText(_translate("MainWindow", "Souřadnice"))
        self.fix_label.setText(_translate("MainWindow", "NÁZEV:"))

# Add measurement
class OpenWindowAddMeas:
    def OpenFile(OpenFile):
        pass

# Choose action of measurement

# Graph

# Export

# Coordinates

# Run App
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())