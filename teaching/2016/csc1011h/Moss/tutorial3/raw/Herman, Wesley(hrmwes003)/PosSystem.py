# A Point of Sale system
# Wesley Herman
# HRWES003



import sys
import sqlite3
from PyQt4 import QtGui, QtCore
from PyQt4 import *
from QuantityInStockLoop import QuantityInStockLoop
from StockCodeLoop import StockCodeLoop
from CostPriceLoop import CostPriceLoop
from SalesPriceLoop import SalesPriceLoop
import pickle
import datetime

# open databases
db5 = sqlite3.connect("Stock.db")
db7 = sqlite3.connect("Sales.db")
       

class PosSystem(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.cw = QtGui.QWidget(self)
        self.setGeometry(275, 125, 300, 300)
        self.setWindowTitle("POS System")
        self.w = None
# counters        
        self.total_sales = 0
        self.total_cost = 0
        self.total_income = 0
       
# GUI items       
        heading_label = QtGui.QLabel("POS System")
        heading_label.setFont(QtGui.QFont("Arial",24))
        
        item_label = QtGui.QLabel("Item to be sold:")
                
        self.item_combo = QtGui.QComboBox()
        self.item_combo.addItem("Chips")
        self.item_combo.addItem("Biscuits")
        self.item_combo.addItem("Chocolate")
        self.item_combo.addItem("Cooldrink")
        self.item_combo.addItem("Juice")
        self.item_combo.addItem("Bubblegum")
        self.item_combo.addItem("Lollypop")
        self.item_combo.addItem("Marshmallows")
        self.item_combo.addItem("Biltong")
        self.item_combo.addItem("Dry Wors")
        
        quantity_label = QtGui.QLabel("Quantity:")
        self.quantity_edit = QtGui.QLineEdit()
        
        self.sales_report = QtGui.QPushButton("Sales Report")
        self.ok = QtGui.QPushButton("OK")
        self.clos = QtGui.QPushButton("Close")
        
        grid = QtGui.QGridLayout()
        grid.addWidget(item_label, 0, 0)
        grid.addWidget(self.item_combo, 0, 1)
        grid.addWidget(quantity_label, 1, 0)
        grid.addWidget(self.quantity_edit, 1, 1)
        
        grid_widget = QtGui.QWidget()
        grid_widget.setLayout(grid)
        
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.sales_report)
        hbox.addWidget(self.ok)
        hbox.addWidget(self.clos)
        hbox_widget = QtGui.QWidget()
        hbox_widget.setLayout(hbox)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(heading_label)
        vbox.addWidget(grid_widget)
        vbox.addWidget(hbox_widget)
        vbox_widget = QtGui.QWidget()
        self.setLayout(vbox)
        
# default value
        item_combo_text="'Chips'"  
        
# signals for buttons       
        self.connect(self.ok, QtCore.SIGNAL("clicked()"), self.okButtonClicked)
        self.connect(self.clos, QtCore.SIGNAL("clicked()"), self.closeButtonClicked)
        self.connect(self.sales_report, QtCore.SIGNAL("clicked()"), self.salesReportButtonClicked)

        
# signals for threads        
        self.loop_thread = QuantityInStockLoop()
        self.loop_thread.update_label_signal.connect(self.loop_thread_slot)
        
        self.loop_thread_f_slot = StockCodeLoop()
        self.loop_thread_f_slot.update_label_signal.connect(self.loop_thread_slot_f)
        
        self.cost_price_loop = CostPriceLoop()
        self.cost_price_loop.update_label_signal.connect(self.cost_price_slot)
        
        self.sales_price_loop = SalesPriceLoop()
        self.sales_price_loop.update_label_signal.connect(self.sales_price_slot)
        
    def sales_price_slot(self, txt):
        sales = int(txt)
        quantity_user_input = self.quantity_edit.displayText()
        no = int(quantity_user_input)
        transaction_income = no*sales
        self.total_income+=transaction_income
        print(self.total_income)
        
    def cost_price_slot(self, txt):
        cost = int(txt)
        quantity_user_input = self.quantity_edit.displayText()
        no = int(quantity_user_input)
        transaction_cost = no*cost
        self.total_cost+=transaction_cost
        
# Slot for QuantityInStock        
    def loop_thread_slot(self, txt):                              
        x=txt

        quantity_user_input = self.quantity_edit.displayText()
        if int(x)<int(quantity_user_input):
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("Error: Insufficient stock available")
            msgBox.addButton(QtGui.QMessageBox.Cancel)
            msgBox.setDefaultButton(QtGui.QMessageBox.Cancel)
            ret = msgBox.exec_()             
        else:
            c = db5.cursor()
            newQuantity = int(x) - int(quantity_user_input)
            it_combo_text = self.item_combo.currentText()
            nq = "'" + str(newQuantity) + "'"
            ict = "'" + str(it_combo_text) + "'"
            cursor = c.execute('UPDATE Stock set QuantityInStock={tes} where ItemName={tess}'.format(tes=newQuantity, tess=ict))
            db5.commit()
            
# slot for StockCode        
    def loop_thread_slot_f(self, tx):
        h = tx
        quantity_user_input = self.quantity_edit.displayText()
        sold = int(quantity_user_input)
        self.total_sales+=sold
        cd = db7.cursor()
        sc = "'" + h + "'"
        date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        time= "'" + str(date) + "'"
        cursor = cd.execute('INSERT into Sales values ({stockcode}, {sales}, {time})'.format(stockcode=h, sales=sold, time=time))
        db7.commit()


# link here        
    def okButtonClicked(self):
        item_combo_text = self.item_combo.currentText()
        outFile = open("check_text.txt", "wb")
        pickle.dump(item_combo_text, outFile)
        outFile.close() 

        self.loop_thread.start()
        
        outFile = open("check_StockCode.txt", "wb")
        pickle.dump(item_combo_text, outFile)
        outFile.close() 

        self.loop_thread_f_slot.start()    
        self.cost_price_loop.start()
        self.sales_price_loop.start()

        
    def closeButtonClicked(self):
        self.close()        

# pop up here        
    def salesReportButtonClicked(self):
        total_profit = self.total_income - self.total_cost
        x = "Sales Report" + "\n" + "Total items sold: " + str(self.total_sales) + "\n" + "Total cost price: " + str(self.total_cost) + "\n" + "Total income: " + str(self.total_income) + "\n" + "Total profit: " + str(total_profit)
        mBox = QtGui.QMessageBox()
        mBox.setWindowTitle("Sales Report")
        mBox.setText(x)
        mBox.addButton(QtGui.QMessageBox.Cancel)
        mBox.setDefaultButton(QtGui.QMessageBox.Cancel)
        ret = mBox.exec_()         
       

def main():
    app = QtGui.QApplication(sys.argv)
    pos_system = PosSystem()
    pos_system.show()
    sys.exit(app.exec_())
                    
main()