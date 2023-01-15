from PyQt5 import QtWidgets
from GUI import Ui_MainWindow
from Timestamp import *
from TrimbleParser import *
import sys
import sqlite3 as sql
import os
import csv
from PyQt5.QtWidgets import QMessageBox
#from pyqtgraph import PlotWidget, plot
#import pyqtgraph as pg
os.system('python Connection.py')
os.system('python CreateTable.py')

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showDB()
        self.ui.add_button.clicked.connect(self.btnAddMeas)
        self.ui.delete_button.clicked.connect(self.btnDeleteMeas)
        self.ui.exp.clicked.connect(self.btnExportMeas)
        self.ui.graph_button.clicked.connect(self.btnGraphMeas)

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
        self.ui.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

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
                    diff_pointshifts.append(['%.2f' % diff])
            listtable.append(diff_pointshifts)
        #prepare list for show in widget
        list = str(listtable).replace('[','').replace(']','').replace('None','N').replace(' ','')
        data = list.split(',')

        #set a shifts
        index = 0
        for indexcolumn, datacolumn in enumerate(points):
            for indexline, dataline in enumerate(data[index:index+len(stage)]):
                self.ui.table.setItem(indexline, indexcolumn+1, QTableWidgetItem(str(dataline)))
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

    def btnGraphMeas(self):
        pass

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()