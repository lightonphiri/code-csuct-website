# MPHFAR001 Tutorial 3 _ DATABASE 

import sys , sqlite3 
from datetime import *

from PyQt4 import QtGui , QtCore

class StockApp (QtGui.QWidget) :
    def __init__(self,parent = None ) :
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(400,100,600,100)
        self.setWindowTitle("Stock Database")
        self.grid = QtGui.QGridLayout()
        self.close = QtGui.QPushButton("Close")
        self.grid.addWidget(self.close,4,4,1,7)
        self.close.clicked.connect(self.close_app)     
        self.setPalette(QtGui.QPalette(QtGui.QColor("light blue")))
        self.sdb = sqlite3.connect("StockDatabase.db")
        self.total_sales , self.total_cost_price , self.total_sales_price , self.profit = 0 , 0 , 0 , 0
         
    def interface( self ) :
        item_label = QtGui.QLabel("Items",self)
        self.grid.addWidget(item_label,0,1)
        input_label = QtGui.QLabel("Number of Items",self)
        self.grid.addWidget(input_label,0,7)
        
        self.items  = QtGui.QComboBox(self)
        items_list = self.sdb.execute("select name_of_item from Stocks")
        for i in items_list :
            self.items.addItem(str(i).strip("( ) ' ,"))
        self.grid.addWidget(self.items,1,1,1,4)
        
        self.quant = QtGui.QLineEdit(self)
        self.grid.addWidget(self.quant,1,5,1,6)
        
        ok = QtGui.QPushButton("Buy",self)
        ok.clicked.connect(self.okClicked)
        self.grid.addWidget(ok,1,12)
        
        self.salesButton = QtGui.QPushButton("View Sales")
        self.grid.addWidget(self.salesButton,3,4,1,7) 
        self.salesButton.clicked.connect(self.salesReport)
        
    def salesReport(self) :
        sales = QtGui.QMessageBox(self)
        sales.setText("{:30}{}\n\n{:30}R {}\n\n{:30}R {}\n\n{:30}R {:.2f}".format("Total Number of items sold ",self.total_sales,"Total Cost Price",self.total_cost_price,"Total Sales Price",self.total_sales_price,"Total Profit So far" ,self.profit))
        sales.exec_()
       
             
    def okClicked(self) :
        wanted_quant = self.quant.text()
        wanted_item  = self.items.currentText()
        in_stock = self.sdb.execute("select Quantity from stocks where name_of_item = '{}' ".format(wanted_item)) # Checks how much is in the stock 
            
        item_code = self.sdb.execute("select stockCode from stocks where name_of_item = '{}'".format(wanted_item))
        
        sale_price = self.sdb.execute("select salesPrice from stocks where name_of_item = '{}'".format(wanted_item))
        cost = self.sdb.execute("select costPrice from stocks where name_of_item = '{}'".format(wanted_item))
        
        for sale  in sale_price:
            for s in sale :
                sales_price = s
                
        for cos in cost  :
            for c in cos :
                cost_price = c
        
        for code in item_code : 
            for c in code :
                stock_code =  c
          
        for i in in_stock : # Returns Cursor 
            for x in i :       # this is the value of  what is in stock                 
                if int(wanted_quant) > x :
                    err =  QtGui.QMessageBox(self)
                    err.setText("Unfortunalety , We Do Not Have Enough Stock ")
                    err.exec_()          
                else :  # This is where the prgrams records a sale and updates the values in the stock database
                    
                    
                    new_quant = x - int(wanted_quant)
                    self.sdb.execute("UPDATE stocks set Quantity = {} WHERE name_of_item = '{}' ".format(int(new_quant),str(wanted_item))) 
                    
                    self.total_sales += int(wanted_quant) 
                    date = datetime.now()
                    self.sdb.execute("insert into Sales values ( {} , {}, '{}' )".format((stock_code),(self.total_sales),(date)))
                    
                    self.total_sales_price +=sales_price
                    self.total_cost_price += cost_price
                    self.profit  += (sales_price - cost_price)*int(wanted_quant)
                    
                    
            self.sdb.commit()
                
    def close_app(self) :
        sys.exit()
          
    def commit(self) :
        self.sdb.commit()

def main() :
    app =  QtGui.QApplication(sys.argv) 
    stockapp = StockApp()
    
    stockapp.setFont(QtGui.QFont("Calibri",13))
    
    stockapp.interface()
    appGrid = stockapp.grid
    stockapp.setLayout(appGrid)
    stockapp.show()
   
    sys.exit(app.exec_())

            
main()
     