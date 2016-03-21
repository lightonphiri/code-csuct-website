import os
from PyQt4 import QtGui, QtCore
import sys,sqlite3, time

class ReportWidget(QtGui.QWidget):
    def __init__(self,parent= None):
        
        QtGui.QWidget.__init__(self,parent)
        
        self.setGeometry(300,300,400,300)
        
        self.setWindowTitle("Sales Report")
        
        self.setWindowIcon(QtGui.QIcon("shop.png"))
        
        self.totalNumberSold = 0
        
        self.totalCostPrice = 0
        
        self.totalSalesPrice = 0
        
        self.totalProfit = 0
        
        self.Database = ''
        self.TableName1 = ''
        self.TableName2 = ''
        
        self.lblTotalNumberOfItemsSold = QtGui.QLabel("Total Number of Items Sold :",self)
        self.lblTotalNumberOfItemsSold.setFont(QtGui.QFont("Courier", 14))
        self.lblOutput1 = QtGui.QLabel("",self)
        
        self.lblTotalCostPrice = QtGui.QLabel("Total Cost Price :",self)
        self.lblTotalCostPrice.setFont(QtGui.QFont("Courier", 14))
        self.lblOutput2 = QtGui.QLabel("",self)
        
        self.lblTotalSalesPrice = QtGui.QLabel("Total Sales Price:",self)
        self.lblTotalSalesPrice.setFont(QtGui.QFont("Courier", 14))
        self.lblOutput3 = QtGui.QLabel("",self)
        
        self.lblTotalProfit = QtGui.QLabel("Total Profit :")
        self.lblTotalProfit.setFont(QtGui.QFont("Courier", 14))
        self.lblOutput4 = QtGui.QLabel("",self)
        
        self.btnClose = QtGui.QPushButton("Close",self)        
        
        self.theGrid_ = QtGui.QGridLayout()
        
        self.theGrid_.addWidget(self.lblTotalNumberOfItemsSold,0,0)
        self.theGrid_.addWidget(self.lblOutput1,0,1)
        self.theGrid_.addWidget(self.lblTotalCostPrice,1,0)
        self.theGrid_.addWidget(self.lblOutput2,1,1)
        self.theGrid_.addWidget(self.lblTotalSalesPrice,2,0)
        self.theGrid_.addWidget(self.lblOutput3,2,1)
        self.theGrid_.addWidget(self.lblTotalProfit,3,0)
        self.theGrid_.addWidget(self.lblOutput4,3,1)
        self.theGrid_.addWidget(self.btnClose,4,0)
        
        self.setLayout(self.theGrid_)
        self.btnClose.clicked.connect(self.close_)

    def DatabaseInfo(self,Database,TableName1,TableName2):
        self.Database = Database
        self.TableName1 = TableName1
        self.TableName2 = TableName2        
        
        
    def close_(self):
        self.close()
        
        
    def CalculateOutput(self):
        db = sqlite3.connect(self.Database)

        stockcode = ''
        price = 0.00
   
        totalNrOfItemsSold = 0
        totalSalesPrice = 0.00
        totalProfit = 0.00
        
        #Calculate Total number of Items Sold
        cursor = db.execute("Select SalesRecords.QuantitySold FROM "+self.TableName2)
        for row in cursor:
            totalNrOfItemsSold = totalNrOfItemsSold + row[0]

        #Calculate Total Cost Price, Total Sales Price:
        
        cursor = db.execute("Select Stock.StockCode,Stock.CostPrice,Stock.SalesPrice,SalesRecords.QuantitySold FROM Stock INNER JOIN SalesRecords ON Stock.StockCode=SalesRecords.StockCode")
        
        totalCostPrice = 0.00    
        totalSalesPrice = 0.00
        for row in cursor:
            totalCostPrice = totalCostPrice + row[1]
            totalSalesPrice = totalSalesPrice + row[2]
    
        #Calculate Total Profit:
        totalProfit = totalSalesPrice - totalCostPrice
        
        self.lblOutput1.setText(str(totalNrOfItemsSold))
        self.lblOutput2.setText(str(totalCostPrice))
        self.lblOutput3.setText(str(totalSalesPrice))
        self.lblOutput4.setText(str(totalProfit))
        
def SalesReport():
    app_ = QtGui.QApplication(sys.argv)
    Widget_ = ReportWidget()
    Widget_.DatabaseInfo("Tuckshop.db","Stock","SalesRecords")
    Widget_.CalculateOutput()
    Widget_.show()
    sys.exit(app_.exec_())
    
SalesReport()
