from PyQt4 import QtCore
from time import *
import sqlite3
import pickle


class StockCodeLoop(QtCore.QThread):

    update_label_signal = QtCore.pyqtSignal(str)       # create signal

    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
    def run(self):          # run executed when start() method called
        inFile = open("check_StockCode.txt", "rb")
        newList = pickle.load(inFile) 
        t = str(newList)
        db = sqlite3.connect("Stock.db")
        cd = db.cursor()
        s = "'" + t + "'"
        cursor = cd.execute('SELECT StockCode FROM Stock WHERE ItemName={tes}'.format(tes=s))
        answer = str(cd.fetchone())
        finall = answer[1:-2]
        self.update_label_signal.emit(str(finall))
