# Journal
# Wanga Mulaudzi
# 7 March 2016

# import all necessary modules
import sqlite3
import datetime
import sys
from PyQt4 import QtGui, QtCore

db = sqlite3.connect('tuckshop.db')

# lists
total_items_sold = []
total_cost_price = []
total_sales_price = []
total_profit = []

class PopupWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(250,250,200,130)
        self.setWindowTitle('Sales Report')        

class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        # create window
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(250,250,200,130)
        self.setWindowTitle('Tuck Shop')
        self.popup = None
        
        # edit line
        self.edit = QtGui.QLineEdit(self)
        
        # labels to display messages
        description = QtGui.QLabel()
        description.setText('Pick your item:')
        display = QtGui.QLabel()
        display.setText('Quantity:')
        self.message = QtGui.QLabel()
        
        # buttons
        ok = QtGui.QPushButton("OK")
        close = QtGui.QPushButton("Close")
        sales_report = QtGui.QPushButton("Sales Report")
        
        # create combo box
        self.combo = QtGui.QComboBox()
        self.combo.addItem('Cadbury')
        self.combo.addItem('Coke 330ml')
        self.combo.addItem('Fanta Orange 330ml')
        self.combo.addItem('Kitkat Family Size')
        self.combo.addItem('Lightly Salted Lays Chips')
        self.combo.addItem('Jumping Jacks Popcorn')
        self.combo.addItem('Magnum Ice Cream')
        self.combo.addItem('Eatsumore Biscuits')
        self.combo.addItem('Chilli Puffs')
        self.combo.addItem('Milk Tart')
        
        # create grid
        grid = QtGui.QGridLayout()
        grid.addWidget(description,0,0)
        grid.addWidget(self.combo,0,1)
        grid.addWidget(display,2,0)
        grid.addWidget(self.edit,2,1)
        grid.addWidget(ok,3,0)
        grid.addWidget(self.message,4,0,1,2)
        grid.addWidget(close,3,1)
        grid.addWidget(sales_report,3,2)
        
        # set the layout of the grid
        self.setLayout(grid)
        
        # connect the buttons
        self.connect(ok, QtCore.SIGNAL('clicked()'), self.okButtonClicked)
        self.connect(close, QtCore.SIGNAL('clicked()'), self.closeButtonClicked)
        self.connect(sales_report, QtCore.SIGNAL('clicked()'), self.salesButtonClicked)
        
    def okButtonClicked(self):
        # current text on the combo box
        self.text = self.combo.currentText() 
        print(self.text)
        
        quantity = int(self.edit.text()) # get the amount of item wanted
        total_items_sold.append(quantity)    
        print(quantity)

        time = str(datetime.datetime.now()) # get the time
        
        # check whether there is enough stock of the item
        value = db.execute("SELECT Quantity FROM Stock WHERE NameOfItem ='"+self.text+"'")
        print(value)
        #row1 = None
        for row in value:
            row1 = row[0]
        print(row1)
        
        if row1 > 0: # if there is stock, get the stock code and add it into Sales
            stock_code = db.execute("SELECT StockCode FROM Stock WHERE NameOfItem ='"+self.text+"'")
            for row in stock_code:
                row2 = row[0]
            
            db.execute("INSERT into Sales VALUES (?,?,?)",(row2, row1, time))
            new_value = row1 - quantity # update the quantity of the item in Stock
            db.execute("UPDATE Stock SET Quantity ='"+str(new_value)+"'WHERE StockCode ='"+row2+"'")
            
            # display message
            self.message.setText(str(quantity)+' x '+self.text+' recorded in sales.')
            
            # get the cost and append to total cost
            cost = db.execute("SELECT CostPrice FROM Stock WHERE NameOfItem = '"+self.text+"'")
            for row in cost:
                cost1 = row[0]
            cost1 = cost1 * quantity
            total_cost_price.append(cost1)
            
            # get the sales and append to toal sales
            sales = db.execute("SELECT SalesPrice FROM Stock WHERE NameOfItem = '"+self.text+"'")
            for row in sales:
                sales1 = row[0]
            sales1 = sales1 * quantity   
            total_sales_price.append(sales1)
            
            # calculate total profit
            profit = sales1 - cost1
            total_profit.append(profit)  
            
            self.message.setText(str(quantity)+' x '+self.text+' recorded in sales')
            
        #display message
        else:
            self.message.setText(self.text+' is not in stock')
            
        db.commit()

    def salesButtonClicked(self):    
        # display total number of items sold
        tot1 = 0
        for i in total_items_sold:
            tot1 = tot1 + i
        
        # display the total cost price
        tot2 = 0
        for i in total_cost_price:
            tot2 = tot2 + i
        
        # display the total sales price
        tot3 = 0
        for i in total_sales_price:
            tot3 = tot3 + i
        
        # display the profit so far
        tot4 = 0
        for i in total_profit:
            tot4 = tot4 + i
        
        # display message on popup window
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("Total number of items sold: "+str(tot1)+"\nTotal cost price: "+str(tot2)+"\nTotal sales price: "+str(tot3)+"\nTotal profit: "+str(tot4))
        msg.setWindowTitle("Sales Report")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        
        retval = msg.exec_()
            
    def closeButtonClicked(self):
        self.close()
         
        
def main():
    app = QtGui.QApplication(sys.argv)
    my_widget = MyWidget()
    my_widget.show()
    sys.exit(app.exec_())
        
main()