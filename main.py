# -*- coding: utf-8 -*-
# Created by: D.Dvorak to project in CTU
# Created by: PyQt5 UI code generator 5.15.4, Qt Creator, PyCharm Community 2022.2
# The project creates time series of measurements and displays shifts

# Library of functions
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
import sys
from datetime import datetime
import sqlite3
points = []

# Graphics
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QIcon('.img/icon.png'))
        MainWindow.setWindowTitle('Time series of levelling measurements (Trimble DINI // Leica LS15 & LS10)')
        self.central = QtWidgets.QWidget(MainWindow)
        self.central.setObjectName("central")
        self.add_button = QtWidgets.QPushButton(self.central)
        self.add_button.setGeometry(QtCore.QRect(192, 500, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(OpenWindowAddMeas)
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
        # self.action.setText(_translate("MainWindow", "Choose DB")) #min. priority
        self.add_button.setText(_translate("MainWindow", "Add data"))
        self.graph_button.setText(_translate("MainWindow", "Graph"))
        self.exp.setText(_translate("MainWindow", "Export"))
        self.coordinates_button.setText(_translate("MainWindow", "Coordinates"))
        self.fix_label.setText(_translate("MainWindow", "DB name:"))

# Add measurement
class OpenWindowAddMeas(list):
    def __init__(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec_():
            file = dialog.selectedFiles()
            return file

    def AddMeasurementToList(self):
        if next((item for item in points if item['point_id'] == point['point_id']), True) == True:
            points.append(point_id)

    def Time(self):
        now_time = datetime.now()
        current_time = now_time.strftime("%d.%m.%Y %H:%M")
        return current_time

    def ParserTrimble(self, current_date, lines):
        for line in lines:
            data = line.split('|')
            if line.find('|Rz') != -1:
                z = float(data[5].split()[1])
                pointId = data[2].split()[1]
                AddMeasurementToList({'point_id': pointId, 'altitude': z, 'time': current_date})

    @staticmethod
    def _ReadFile(file):
        # read measurement from text file from Trimble devices
        print('Prošel jsem do _ReadFile')
        with open(file) as file:
            lines = file.read().splitlines()
        file.close()
        return lines

# Database
class Database:
    def __init__(self):
        pass

    def InsertToDB(self):
        con = sqlite3.connect('database.db')
        for point in points:
            val = [points['point_id'], points['time'], points['altitude']]
            con.execute('INSERT INTO db_name VALUES (?,?,?)', val)
            con.commit()
        con.close()

    def CreateDB(self):
        if os.path.isfile('database.db') != True:
            db = sqlite3.connect('database.db')
            db.execute('create table db_name (point_id varchar, time date, altitude float'
                       'UNIQUE (point_id, time) ON CONFLICT IGNORE)')
            db.close()

    def ShowDB(self): #for view in main window
        #calculate a difference of time series shifts
        pass

    def InsertToDBC(self): #for coordinates
        CC = sqlite3.connect('database.db')
        CC.execute('INSERT INTO db_name_coordinates VALUES (?,?,?)')
        CC.commit()
        CC.close()

    def CreateDBC(self): #for coordinates
        CC = sqlite3.connect('database.db')
        CC.execute('create table db_name_coordinates (point_id varchar, X integer, Y integer'
                       'UNIQUE point_id PRIMERY KEY point_id)')
        CC.close()

# Graph
class Graph:
    def __init__(self):
        super().__init__()
        self.QtWidgetsGraph

    def QtWidgetsGraph(self):
        #connect to db in class Database
        #parametres of graph (set a x and y lines)
        pass

# Coordinates
class Coordinates:
    def __init__(self):
        #run a qfiledialogCOOR
        #if incorrect data format - PopUpAlert
        #if db exist - InsertToDBC
        #else CreateDBC and after InsertToDBC
        pass

    def PopUpAlert(self):
        pass

    def QFileDialogCOOR(self):
        pass

# Export
class ExportDB:
    def qWidgetForExport(self):
        #place to export file

    def ExportBoth(self):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        data = cur.execute("SELECT * FROM db_name JOIN db_name_coordinates ON db_name.point_id = db_name_coordinates.point_id ")
        #etc

# Run App
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


