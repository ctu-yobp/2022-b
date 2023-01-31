# -*- coding: utf-8 -*-
# Created by: D.Dvorak to project in CTU
# Created by: PyQt5 UI code generator 5.15.4, Qt Creator, PyCharm Community 2022.2
# The project creates time series of measurements and displays shifts

import sqlite3
from Timestamp import *
from TrimbleParser import *
import sys
import sqlite3 as sql
import os
import csv
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui
from Graph import *

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showDB()

        self.connection = sqlite3.connect("Levelling.db")
        self.cursor = self.connection.cursor()

        self.ui.add_button.clicked.connect(self.btnAddMeas)
        self.ui.delete_button.clicked.connect(self.btnDeleteMeas)
        self.ui.exp.clicked.connect(self.btnExportMeas)
        self.ui.graph_button.clicked.connect(self.btnGraphMeas)

    def btnGraphMeas(self):
        self.add_graph_window = Graph(self.connection, self.cursor)
        self.add_graph_window.show()

    def btnAddMeas(self):
        self.trimble = TrimbleParser()
        addpoints = self.trimble.OpenFile()
        self.timestamps = TimestampsClass()
        date, date_unix = self.timestamps.Time()

        try:
            self.conn = sql.connect("Levelling.db")
            for addpoint in addpoints:
                val = [addpoint['id'], date, addpoint['altitude'], date_unix]
                self.c = self.conn.cursor()
                self.c.execute("INSERT INTO points VALUES (?,?,?,?)",val)
                self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.about(self, "Alert", "Measurement added to DB")
        except Exception:
            QMessageBox.about(self, 'Error', 'Could not add measurement to the database.')
        self.showDB()

    def PointForView(self, points):
        points.insert(0, 'Timestamp')
        return points

    def showDB(self):
        self.ui.table.clear()
        db = sql.connect('Levelling.db')
        cur = db.cursor()
        idinheader = [item[0] for item in cur.execute('SELECT distinct(id) FROM points ORDER BY id').fetchall()]
        stage = [item[0] for item in cur.execute('SELECT distinct(timestamp) FROM points ORDER BY timestamp').fetchall()]
        pointsforview = self.PointForView(idinheader)
        rows = len(stage)
        columns = len(pointsforview)
        self.ui.table.setRowCount(rows)
        self.ui.table.setColumnCount(columns)
        self.ui.table.setHorizontalHeaderLabels((pointsforview))

        #take a shifts
        listtable = []
        points = [item[0] for item in cur.execute('SELECT distinct(id) FROM points ORDER BY id').fetchall()]
        for pointshifts in points:
            diff_pointshifts = []
            first_choosestage = None
            for choosestage in stage:
                data = cur.execute('SELECT * FROM points WHERE id = ? AND timestamp = ?', (pointshifts, choosestage)).fetchone()
                if data == None:
                    diff_pointshifts.append(None)
                elif first_choosestage == None:
                    first_choosestage = data
                    diff_pointshifts.append([0])
                else:
                    diff = (data[2] - first_choosestage[2]) * 1000
                    diff_pointshifts.append([format(diff, '.2f')])
            listtable.append(diff_pointshifts)
        #prepare list for show in widget
        list = str(listtable).replace('[','').replace(']','').replace('None','N').replace(' ','').replace("'",'')
        data = list.split(',')

        #set a shifts
        index = 0
        for indexcolumn, datacolumn in enumerate(points):
            for indexline, dataline in enumerate(data[index:index+len(stage)]):
                self.ui.table.setItem(indexline, indexcolumn+1, QTableWidgetItem(dataline))
            index += len(stage)

        #set a timestamp
        for indexline, dataline in enumerate(stage):
            self.ui.table.setItem(indexline, 0, QTableWidgetItem(str(dataline)))


    def btnDeleteMeas(self):
        try:
            self.conn = sql.connect("Levelling.db")
            self.c = self.conn.cursor()
            self.c.execute('DELETE FROM points WHERE unixtimestamp = (SELECT MAX(unixtimestamp) FROM points)')
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.about(self, "Alert", "Measurement deleted from DB")
        except Exception:
            QMessageBox.about(self, 'Error', 'Could not delete measurement from the database.')
        self.showDB()

    def btnExportMeas(self):
        name = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        db = sql.connect('Levelling.db')
        cur = db.cursor()
        selectquery = "SELECT id, timestamp, level FROM points ORDER BY unixtimestamp"
        cur.execute(selectquery)
        with open(name[0], "w", encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cur.description])
            csv_writer.writerows(cur)
        QMessageBox.about(self, "Alert", "Measurement exported from DB.")
        self.showDB()

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


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()