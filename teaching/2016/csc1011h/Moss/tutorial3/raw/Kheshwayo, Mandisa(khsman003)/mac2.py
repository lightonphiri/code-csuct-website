import sys
from PyQt4 import QtGui
import sqlite3

import datetime
date=datetime.date.today()
time=datetime.datetime.time(datetime.datetime.now())
date1=str(date)
time1=str(time)

class MAC_store(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(250, 250, 200, 150)
        self.setWindowTitle('Grid Window')
        
        #background colour
        a=self.setPalette(QtGui.QPalette(QtGui.QColor('violet')))
        self.setAutoFillBackground(True)
        
        
        #labels
        self.mac_label=QtGui.QLabel('MAC STORE',self)
        self.mac_label.setFont(QtGui.QFont('Informal Roman',38,3))
        
        self.items=QtGui.QLabel('Choose items',self)
        self.items.setFont(QtGui.QFont('Arial',18,2))

        self.quantity=QtGui.QLabel('Quantity',self)
        self.quantity.setFont(QtGui.QFont('Arial',18,2))
        
        #buttons
        self.ok=QtGui.QPushButton('Ok')
        self.ok.clicked.connect(self.ok1)
        
        self.sales_report=QtGui.QPushButton('Sale Report')
        self.sales_report.clicked.connect(self.report)
        
        self.close=QtGui.QPushButton('Close')
        self.close.clicked.connect(self.closet)
        
       
        
        #picture
        self.pixmap = QtGui.QPixmap('MAC.jpg')
        self.picture_label = QtGui.QLabel(self) 
        self.picture_label.setPixmap(self.pixmap)
        
        
        #combo box
        self.stock=QtGui.QComboBox()
        self.stock.addItem('MAC_lipstick')
        self.stock.addItem('MAC nail polish')
        self.stock.addItem('MAC lip liner')
        self.stock.addItem('MAC eye line')
        self.stock.addItem('MAC_mascara')
        self.stock.addItem('MAC_foundation')
        self.stock.addItem('MAC_powder')
        self.stock.addItem('bag')
        self.stock.addItem('weave')
        self.stock.addItem('nail_deco')
        self.stockCurrent= self.stock.currentText()
        
        
        #edits
        self.choice_edit=QtGui.QLineEdit()
        
        
        #grid
        grid=QtGui.QGridLayout()
        grid.addWidget(self.picture_label,0,0,5,1)
        grid.addWidget(self.mac_label,0,2)
        grid.addWidget(self.items,1,2)
        grid.addWidget(self.stock,1,4)
        grid.addWidget(self.quantity,2,2)
        grid.addWidget(self.choice_edit,2,4)
        grid.addWidget(self.ok,4,2)
        grid.addWidget(self.sales_report,4,4)
        grid.addWidget(self.close,5,3)
        self.setLayout(grid)
      
    def closet(self):
        sys.exit()
              
    #sqlite3
    def ok1(self):
        self.stockCurrent= self.stock.currentText()
        self.choice_current= self.choice_edit.displayText()
        db = sqlite3.connect('stock-data-base.db')
        c = db.cursor()
        a=c.execute('SELECT * from stock_table where name=?',(self.choice_current,));
        b=a.fetchone()
        db.commit()
        b=list(b)
        left=b[2]-int(self.stockCurrent)
        update=c.execute('UPDATE stock_table set quantity=? where name=?',(left,self.choice_current,));
        db.commit()
        
        if int(self.stockCurrent) > b[1] :
            choice=QtGui.QMessageBox.question(self,'error','sales',QtGui.QMessageBox.Cancel)
            if choice==QtGui.QMessageBox.Cancel:
                sys.Cancel()
 
             
        elif b[1]<=0:
            choice=QtGui.QMessageBox.question(self,'error','sales',QtGui.QMessageBox.Cancel)
            if choice==QtGui.QMessageBox.Cancel:
                sys.Cancel()
         
        else:
            sale=c.execute('INSERT into sale_table values(?,?,?,?)',(b[1],self.stockCurrent,date1,time1));
            db.commit()
        db.close()   
    def report(self):
        report=QtGui.QMessageBox.question(self,'sales report','sales report must be shown here',QtGui.QMessageBox.Cancel)
        if report==QtGui.QMessageBox.close:
            sys.close()
    
    
def main():
    app=QtGui.QApplication(sys.argv)
    my_store=MAC_store()
    my_store.show()
    sys.exit(app.exec_())
main()