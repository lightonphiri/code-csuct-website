import sqlite3
import sys
import time 
import datetime
from PyQt4 import QtGui, QtCore

class POS(QtGui.QWidget):
    
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(250, 250, 200, 150)
        self.setWindowTitle('Point of Sale')
        self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        
        #set buttons
        okbutton = QtGui.QPushButton('OK')
        closebutton = QtGui.QPushButton('Close')
        editbutton = QtGui.QLineEdit(self)
        text = editbutton.displayText()
        okbutton.setMinimumSize(80,20)
        okbutton.setMaximumSize(100,25)
        closebutton.setMinimumSize(80,20)
        closebutton.setMaximumSize(100,25)        
        editbutton.setMinimumSize(80,20)
        editbutton.setMaximumSize(100,25)
        
        #set labels
        s = QtGui.QLabel('selcect item',self)
        q = QtGui.QLabel('enter quantity',self)
        
        combo = QtGui.QComboBox(self) # constructor
        combo.addItem('Pepsi')
        combo.addItem('Refresh')
        combo.addItem('Bonaqua')
        combo.addItem('fanta')
        combo.addItem('7up')
        combo.addItem('Play')
        combo.addItem('Dragon')
        combo.addItem('Red bull')
        combo.addItem('Monster')
        combo.addItem('Boost')
        text = combo.currentText() # gets selected text	 
        
        grid = QtGui.QGridLayout()
        grid.addWidget(editbutton,2,2)
        grid.addWidget(okbutton,3,2)
        grid.addWidget(s,1,1)
        grid.addWidget(q,2,1)
        grid.addWidget(combo,1,2)
        grid.addWidget(closebutton,3,3)
        self.setLayout(grid)
        
        combo.activated[str].connect(self.onActivated)
        
    def onActivated(self, text):
        self.lbl.setText(text)
        
        get = combo.displayText()
        get_q = editbutton.getText()
        
        db_open = connect('myStore.db')
        amount = db_open.execute("select Quantity where Item Name = get")
        
        # connect ok, close click event to buttonClicked slot event handler        
        self.connect(okbutton,QtCore.SIGNAL('clicked()'),sel.buttonClicked)
        self.connect(closebutton,QtCore.SIGNAL('clicked()'),self.buttonClicked)
    
    def buttonClicked(self):
        sel.close()# close the window
       
createdb = sqlite3.connect('tut.db') #creat a data base
c = createdb.cursor()
    
def create_table():
    c.execute('''CREATE TABLE Stock Table(stock code INTEGER, name of item TEXT, brief description TEXT, cost price REAL, sales price REAL, quantity in stock INTEGER )''')
    
def data_entry():
    c.execute("INSERT INTO Stock Table()" ) 
    
def read_from_table():
    c.execute('SELECT Stock Code FROM myStore where item=')
    
def create_table2():
    c.execute('''CTREATE TABLE Sales Table(stock code INTEGER, quantity sold INTEGER, datestamp TEXT)''')

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fronttimestamp(unix).strftime('%y-%m-%d %H:%M:%S'))
    c.execute("ENSERT INTO Sales Table(unix,datestamp)VALUES()")

def main():
    app = QtGui.QApplication(sys.argv)
    a = POS()
    a.show()
    sys.exit(app.exec_())    
    createdb.commit()
    read_from_table()
    c.close()
    createdb.close()
    data_entry()
main()