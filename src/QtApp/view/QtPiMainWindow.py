#!/usr/bin/python3
import sys
from PyQt4 import QtGui
from QtApp.view.mainwindow import Ui_mainwindow

class QtPiMainWindow(QtGui.QMainWindow):
    def __init__(self, model):
        super(QtPiMainWindow, self).__init__()
        self.model = model
        self.initUI()

    def initUI(self):
        self.win = Ui_mainwindow()
        self.win.setupUi(self)
        self.win.flightStatusTable.setModel(self.model.getDepartureListModel())
