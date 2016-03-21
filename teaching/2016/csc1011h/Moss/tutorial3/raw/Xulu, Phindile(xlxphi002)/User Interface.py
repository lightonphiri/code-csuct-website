#PRogram to create a Tuckshop user interface
#Phindle Xulu   
#11 March 2016

import sqlite3
import sys
from PyQt4 import QtGui
from datetime import datetime, date,time

class Tuckshop_system(QtGui.QWidget):                 #Creates main window
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.tuckshop=sqlite3.connect("Tuckshop.db")
        self.setWindowTitle("Zama Zama Tuckshop")       #Creates a window title with the name of the store
        self.setGeometry(250,250,500,500)               #Sets x,y,width and height size of the window
        self.item_name=QtGui.QLabel("Item:")
        self.combo_box=QtGui.QComboBox()                #Creates a Combo Box with the items to select
        self.setPalette(QtGui.QPalette(QtGui.QColor(20,40,75)))         #Change colour of the main widget
        self.combo_box.setStyleSheet('QPushButton {background-color: #A3C1DA; color: 50,80,200;}') #Change colour of combo_box text
        
        #self.AutoFillBackground(True)
        self.combo_box.addItem("OREOS")
        self.combo_box.addItem("Aero")
        self.combo_box.addItem("Cheese Simba Chips")
        self.combo_box.addItem("BBQ Simba Chips")
        self.combo_box.addItem("Astros")
        self.combo_box.addItem("Chappies")
        self.combo_box.addItem("Maynards")
        self.combo_box.addItem("Sour Worms")
        self.combo_box.addItem("Banana")
        self.combo_box.addItem("Peach")
        
        self.quantity_label=QtGui.QLabel("Quantity:")
        self.quantity_text=QtGui.QLineEdit()
        self.quantity_text.setPalette(QtGui.QPalette(QtGui.QColor("green")))        #Change colour of textbox
        
        self.ok=QtGui.QPushButton("OK")                 #Create OK Push Button
        self.ok.clicked.connect(self.ok_button)         #Connects the ok button to the ok function
        self.ok.setStyleSheet('QPushButton {background-color: #A3C1DA; color: 50,80,200;}') #Change colour of push button
        self.sales_record_button=QtGui.QPushButton("Sales Record")               
        self.sales_record_button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: 50,80,200;}')
        self.sales_record_button.clicked.connect(self.sales_record)     #Connects the sales record button to the sales record function
        self.record_label=QtGui.QLabel("Sales Record:")
        self.no_of_items_label=QtGui.QLabel("")
        self.no_of_items=0                  #Initial value of number of items bought
        self.total_cost_label=QtGui.QLabel("")
        self.total_cost=0                   #Initial value of cost for items bought
        self.total_sales_label=QtGui.QLabel("")
        self.total_sales=0                  #Initial value for total sales price of number of items sold
        self.profit_label=QtGui.QLabel("")
        
        self.error_message=QtGui.QLabel("")
        self.close_button=QtGui.QPushButton("Close") 
        self.close_button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: 50,80,200;}')
        self.close_button.clicked.connect(self.close)                   #Connects the close cutton to the close function
        
        #Add Widgets to the layout
        self.grid=QtGui.QGridLayout() 
        self.grid.addWidget(self.item_name,0,0)
        self.grid.addWidget(self.combo_box,0,1)
        self.grid.addWidget(self.quantity_label,1,0)
        self.grid.addWidget(self.quantity_text,1,1)
        self.grid.addWidget(self.error_message,2,0)
        self.grid.addWidget(self.ok,3,0)
        self.grid.addWidget(self.sales_record_button,3,1)
        self.grid.addWidget(self.record_label,5,0)
        self.grid.addWidget(self.no_of_items_label,5,1)
        self.grid.addWidget(self.total_cost_label,6,1)
        self.grid.addWidget(self.total_sales_label,7,1)
        self.grid.addWidget(self.profit_label,8,1)
        self.grid.addWidget(self.close_button,9,1)
        self.setLayout(self.grid)
        
    def ok_button(self):                                                #To record the sale and keep track of the profit number of items sold and the total cost and sales price
        self.item=self.combo_box.currentText()                           #Get name of item
        self.error_message.clear()
        self.quantity=self.quantity_text.displayText()                  #Get wanted quantity
        stockcode=self.tuckshop.execute("select StockCode from [Stock Table] where Item=(?)",(self.item,)) #Get stock code
        self.stockcode=stockcode.fetchone()
        quantity_stock=self.tuckshop.execute("select Quantity from [Stock Table] where Item=(?)",(self.item,))  #Gets quantity in stock
        self.quantity_in_stock=quantity_stock.fetchone()
       
        if int(self.quantity)<=int(str(self.quantity_in_stock)[1:2]):                   #Check if there are enough items in stock
            current_quantity=int(str(self.quantity_in_stock)[1:2])-int(self.quantity)                   # Subtracts bought stock from the total stock in tuckshop database to get total number of items not sold
            self.tuckshop.execute("update [Stock Table] set Quantity=(?) where Item=(?)",(str(current_quantity),(self.item))) # Updates quantity of stock in the database
            self.no_of_items+=int(self.quantity)
            self.quantity=self.quantity_text.displayText()                      #Get quantity wanted by user
            sales_price=self.tuckshop.execute("select SalesPrice from [Stock Table] where Item=(?)",(self.item,))
            self.sales_price=sales_price.fetchone()
            cost_price=self.tuckshop.execute("select CostPrice from [Stock Table] where Item=(?)",(self.item,))
            self.cost_price=cost_price.fetchone()
            self.tuckshop.execute("insert into Sales (StockCode , Quantity, Date, Time ) values((?),(?),(?),(?))",(str(self.stockcode)[2:7],float(self.quantity),str(datetime.now().date()),str(datetime.now().time())[0:8]))
            self.total_cost+=float(str(self.cost_price)[1:5])*float(self.quantity)                          #Totals all cost prices
            self.total_sales+=float(str(self.sales_price)[1:5])*float(self.quantity)                        #Totals all sales prices
            self.quantity_text.clear()
            
        elif int(self.quantity)>int(str(self.quantity_in_stock)[1:2]) or self.quantity<0:                      #If there are less than required items in stock
            self.error_message.setText("Not enough items in stock. Items in stock: "+(str(self.quantity_in_stock)[1:2]))        #Desplays error message with the number of items in stock        
            self.quantity_text.clear()
        self.tuckshop.commit()
        
        
    def sales_record(self):                                                         #Displays all the records to the user
        self.no_of_items_label.setText("Number of items:       "+str(self.no_of_items))
        self.total_cost_label.setText("Total Cost:               R"+str(self.total_cost))
        self.total_sales_label.setText("Total Sales Price:    R"+str(self.total_sales))
        self.profit=self.total_sales-self.total_cost             #Calculates profit 
        self.profit_label.setText("Total Profit:            R"+str(self.profit))
        
    def close(self):
        sys.exit()
        
def main():
    app=QtGui.QApplication(sys.argv)
    tuc_widget=Tuckshop_system()
    tuc_widget.show()
    sys.exit(app.exec_())
main()