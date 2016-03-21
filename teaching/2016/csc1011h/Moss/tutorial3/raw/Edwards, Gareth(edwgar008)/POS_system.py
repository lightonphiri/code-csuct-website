# POS system for a tuckshop
# EDWGAR008
# Gareth Edwards

import sys
from PyQt4 import QtGui,QtCore
import sqlite3
from datetime import datetime

class PopupWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(300,300,400,200)
        self.setWindowTitle("Sales Report")
        
        self.sold = QtGui.QLabel('',self)
        self.costprice = QtGui.QLabel('',self)
        self.profit = QtGui.QLabel('',self)
        self.saleP = QtGui.QLabel('',self)
        
        #self.close = QtGui.QPushButton('Close')
        #self.close.clicked.connect(self.Click_close)
        
        VertBox = QtGui.QVBoxLayout()
        VertBox.addWidget(self.sold)
        VertBox.addWidget(self.costprice)
        VertBox.addWidget(self.saleP)
        VertBox.addWidget(self.profit)
        #VertBox.addWidget(self.close)
        
        grid_layout2 = QtGui.QGridLayout()
        grid_layout2.addLayout(VertBox,0,0)
        self.setLayout(grid_layout2)        
        
    #def Click_close(self):
        #self.close()
        
        
        #self.setLayout(VertBox)
        
class POSWidget(QtGui.QWidget):
    def __init__(self,parent=None,counter=0,ic=0,cc=0,pc=0):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(250, 250, 300, 150)
        self.setWindowTitle("Tuckshop")
        self.counter = counter
        self.item_count = ic
        self.cost_count = cc
        self.profit_count = pc
        
        self.combo = QtGui.QComboBox()
        self.combo.addItem('Apples')
        self.combo.addItem('Brownies')
        self.combo.addItem('Chips')
        self.combo.addItem('Chocolate')
        self.combo.addItem('Cooldrink')
        self.combo.addItem('Jelly Babies')
        self.combo.addItem('Oranges')
        self.combo.addItem('Palony Rolls')
        self.combo.addItem('Peanuts')
        self.combo.addItem('Pies')
        
        #item = self.combo.currentText()
        
        self.edit = QtGui.QLineEdit()
        num = self.edit.displayText()
        SR = QtGui.QPushButton('Sales Report')
        
        ok = QtGui.QPushButton('OK')
        ok.clicked.connect(self.okClicked)
        #ok.clicked.connect(self.count)
        
        close = QtGui.QPushButton('Close',self)
        close.clicked.connect(self.closeClicked)
        
        self.label = QtGui.QLabel('',self)        # Displays message informing user of stocks
        
        self.label2 = QtGui.QLabel('',self)
        
        label_pos = QtGui.QHBoxLayout()
        label_pos.addWidget(self.label)
        label_pos.addWidget(self.label2)
        
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.combo)
        hbox.addWidget(self.edit)
        
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(SR)
        hbox2.addWidget(close)
        hbox2.addWidget(ok)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(label_pos)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        
        
        grid_layout = QtGui.QGridLayout()
        grid_layout.addLayout(vbox,0,0)
        self.setLayout(grid_layout)
        
        SR.clicked.connect(self.Report)
        
        
    
    def Report(self):
        self.pop = PopupWidget()
        
        self.pop.sold.setText('Items sold: '+str(self.item_count))
        self.pop.costprice.setText('Total Cost Price: '+'R'+str(self.cost_count))
        self.pop.saleP.setText('Total Sales Price: '+'R'+str(self.counter))
        self.pop.profit.setText('Total profit on items: '+'R'+str(self.profit_count))
        
        self.pop.show()
            
    def closeClicked(self):
        self.close()
     
        
    def okClicked(self):
        #self.count+=int(quant)
        db = sqlite3.connect('ShopDatabase.db')   # Fetches necessary db file
        item = self.combo.currentText()           # saves text chosen from combo box
        quant = self.edit.displayText()           # saves text typed in edit bar
        #print(item)
        item = '"'+item+'"'
        item_m = self.combo.currentText()
        self.pop = PopupWidget()
        
        
        command = 'select InStock from Stock where Name = '+item
        #print(command)
        
        command_s = 'select SalesPrice from Stock where Name = '+item
        cursor1 = db.execute(command_s)
        for row in cursor1:
            sale_price = row[0]
            
        sale_total = int(quant)*sale_price
        self.counter+=sale_total                      # total sales price
        #print(self.counter)                
        
        self.item_count+=int(quant)
        #print(self.item_count)
        
        command_c = 'select CostPrice from Stock where Name = '+item
        cursor2 = db.execute(command_c)
        for row in cursor2:
            cost_price = row[0]
        
        cost_total = int(quant)*cost_price
        self.cost_count+=cost_total                  # total cost price
        #print(self.cost_count)
        
        profit = self.counter - self.cost_count     # profit
        self.profit_count=profit
        
        #self.pop.sold.setText(str(self.item_count))
        
        
        inStock_val = db.execute(command)          
        for row in inStock_val:
            stock_quant = row[0]                  # assigns the amount of items in stock to the variable stock_quant        
        
        
        if int(quant) > stock_quant:
            if stock_quant != 0:
                message = 'We only have '+str(stock_quant)+' '+item_m
                self.label.setText(message)
                self.edit.clear()                
            elif stock_quant == 0:
                self.label.setText('We are out of stock. Sorry')
                self.edit.clear()
            
        
        elif int(quant) <= stock_quant:
            
            quant = int(quant)
            
            new_val = stock_quant-int(quant)
            new_val = str(new_val)
            string = 'update Stock set InStock = '+new_val+' where Name = '+item
            
            StockCode = 'select StockCode from Stock where Name = '+item        # stock code of item selected
            cursor = db.execute(StockCode)
            for i in cursor:
                StockCode = i[0]

            ItemSold = int(quant)
            TOT = datetime.now()
            
            db.execute('insert into Sales values (?,?,?)',(StockCode,ItemSold,TOT))
            
            db.execute(string)
            db.commit()
            self.edit.clear()
            #print(self.count)

    

    
                                   
            
def main():
    app = QtGui.QApplication(sys.argv)
    widget = POSWidget()
    widget.show()
    sys.exit(app.exec_())
    
    
main()
    
        
    