from PyQt5.QtWidgets import *
import os
import random
points = []

class TrimbleParser(QFileDialog):
    def OpenFile(self):
        name = QFileDialog.getOpenFileName(self, "Open Measurement", os.getenv('HOME'), "(*.DAT)")
        with open(name[0], 'r') as MeasFile:
            addmeasfile = MeasFile.readlines()
        for line in addmeasfile:
            if line.find('|Rz') != -1:
                meas = self.getMeas(line)
                self.addPoint(points, {'id': meas['id'], 'altitude': meas['altitude']})
        return points

    def getMeas(self, line):
        data = line.split('|')
        altitude = float((data[5].split()[1]))
        pointId = data[2].split()[1]
        return {"id": pointId, "altitude": altitude}

    def addPoint(self, points, point):
        if next((item for item in points if item['id'] == point['id']),True) == True:
            points.append(point)
