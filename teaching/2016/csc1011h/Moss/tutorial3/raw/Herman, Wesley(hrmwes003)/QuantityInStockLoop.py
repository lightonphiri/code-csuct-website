from PyQt4 import QtCore
from time import *
import sqlite3
import pickle

class QuantityInStockLoop(QtCore.QThread):

    update_label_signal = QtCore.pyqtSignal(str)       

    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
    def run(self):          # run executed when start() method called
        inFile = open("check_text.txt", "rb")
        newList = pickle.load(inFile) 
        t = str(newList)

        db = sqlite3.connect("Stock.db")
        c = db.cursor()

        s = "'" + t + "'"
        cursor = c.execute('SELECT QuantityInStock FROM Stock WHERE ItemName={tes}'.format(tes=s))
        answer = str(c.fetchone())

        final = answer[1:-2]

        self.update_label_signal.emit(str(final))
