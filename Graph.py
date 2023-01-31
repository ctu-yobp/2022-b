from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import pyqtgraph as pg

class Graph(QtWidgets.QMainWindow):
    def __init__(self, connection, cursor):
        super().__init__()
        self.connection = connection
        self.cursor = cursor
        self.create_layouts()

    def create_layouts(self):
        self.main_layout = pg.PlotWidget(axisItems={'bottom': pg.DateAxisItem()})
        self.setCentralWidget(self.main_layout)

        #make shifts
        listtable = []
        stage = [item[0] for item in self.cursor.execute('SELECT distinct(timestamp) FROM points ORDER BY timestamp').fetchall()]
        points = [item[0] for item in self.cursor.execute('SELECT distinct(id) FROM points ORDER BY id').fetchall()]
        for pointshifts in points:
            diff_pointshifts = []
            first_choosestage = None
            for choosestage in stage:
                data = self.cursor.execute('SELECT * FROM points WHERE id = ? AND timestamp = ?',(pointshifts, choosestage)).fetchone()
                if data == None:
                    diff_pointshifts.append(None)
                elif first_choosestage == None:
                    first_choosestage = data
                    diff_pointshifts.append([0])
                else:
                    diff = (data[2] - first_choosestage[2]) * 1000
                    diff_pointshifts.append([format(diff, '.2f')])
            listtable.append(diff_pointshifts)

        # prepare list for show in graph
        list = str(listtable).replace('[', '').replace(']', '').replace('None', '0').replace(' ', '').replace("'", '')
        list2 = list.split(',')

        #retype to float
        data = []
        for element in list2:
            data.append(float(element))
        # define the data
        unixtime = [item[0] for item in self.cursor.execute('SELECT distinct(unixtimestamp) FROM points ORDER BY unixtimestamp').fetchall()]

        # set properties
        self.main_layout.setBackground('w')
        self.main_layout.setLabel('left', 'Shifts', units='mm')
        self.main_layout.setLabel('bottom', 'Time', units='Unixtime')
        self.main_layout.showGrid(x=True, y=True)
        self.main_layout.addLegend()
        pen = pg.mkPen(color=(255, 0, 0))

        #plot
        for i in range(0, len(data), len(unixtime)):
            dat = data[i:i+len(unixtime)]
            self.main_layout.plot(unixtime, dat, symbol='o', pen=pen)
            self.main_layout.show()





