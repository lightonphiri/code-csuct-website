from PyQt4 import QtCore
from time import *
import sqlite3
import pickle

# defines a thread which emits signals with values 0 to 99
class LoopThreadTesting(QtCore.QThread):

    update_label_signal = QtCore.pyqtSignal(str)       # create signal

    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
    def run(self):          # run executed when start() method called
        inFile = open("check_text.txt", "rb")
        newList = pickle.load(inFile) 
        t = str(newList)
        #print(t)
        db = sqlite3.connect("Stock.db")
        c = db.cursor()
        #s = "'Chips'"
        #s = PosSystem.get_text()
        s = "'" + t + "'"
        #print(s)
        #t = "CHP0050"
        cursor = c.execute('SELECT QuantityInStock FROM Stock WHERE ItemName={tes}'.format(tes=s))
        answer = str(c.fetchone())
        final = answer[1:-2]
        #final_ans = int(final)
        self.update_label_signal.emit(str(final))
