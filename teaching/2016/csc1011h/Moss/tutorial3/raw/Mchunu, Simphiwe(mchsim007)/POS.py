# Point of sale system - OOP
# Simphiwe Mchunu
# 14 March 2016

import sys
from PyQt4 import QtGui
from datetime import datetime, date, time
import sqlite3

class POS(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setWindowTitle("Point of Sale System:")
        self.setGeometry(500,200,150,200)
        self.setPalette(QtGui.QPalette(QtGui.QColor('fuchsia')))
        self.setAutoFillBackground(True)        
        
        ''' Sets and Display picture'''
        self.pixmap = QtGui.QPixmap('tuckshop.png')
        self.pic_label = QtGui.QLabel(self)
        self.pic_label.setPixmap(self.pixmap)        
        
        self.quantity = QtGui.QLabel('Quantity:')
        self.label = QtGui.QLabel('WELCOME!!!')
        self.empty = QtGui.QLabel('',self)
        self.line_edit = QtGui.QLineEdit()
        self.ok_button = QtGui.QPushButton('OK')
        self.ok_button.clicked.connect(self.ok) # connects ok_button to the ok method
        self.close_button1 = QtGui.QPushButton('Close')
        self.close_button1.clicked.connect(self.close_button) # connects close_button to the close method
        self.sales_report_button = QtGui.QPushButton('Sales Report')
        self.sales_report_button.clicked.connect(self.sales_report) # connects the sales_report_button to the sales_report method
        
        
        '''Creating combo box, adding items to it'''
        self.item_combo_box = QtGui.QComboBox()
        self.item_combo_box.addItem('Select Option:')
        self.item_combo_box.addItem('Filled roll, chicken')
        self.item_combo_box.addItem('Pizza bread slice')
        self.item_combo_box.addItem('Bread bun, cheese, bacon sprinkled up')
        self.item_combo_box.addItem('Quinche (with ham)')
        self.item_combo_box.addItem('Mince Pie- Potato top, bread base')
        self.item_combo_box.addItem('Noodles, Chicken')
        self.item_combo_box.addItem('Noodles, Beef')
        self.item_combo_box.addItem('Buttered Current Bun')
        self.item_combo_box.addItem('Muffin, Bran')
        self.item_combo_box.addItem('Muffin, Apple')
        self.item_combo_box.addItem('Muffin, Blueberry')
        self.item_combo_box.addItem('Popcorn')
        self.item_combo_box.addItem('Zing')
        self.item_combo_box.addItem('Water')
        self.item_combo_box.addItem('Primo')
        self.item_combo_box.addItem('Wrap, Chicken')
        self.item_combo_box.addItem('Wrap, Ham')
        self.item_combo_box.addItem('Muffin, Sulfana')
        
        
        
        '''Creating grid layout'''
        self.grid = QtGui.QGridLayout()
        '''add widgets to grid layout'''
        self.grid.addWidget(self.pic_label,0,0,10,1)
        self.grid.addWidget(self.label,0,1)
        self.grid.addWidget(self.item_combo_box,1,1,1,2)
        self.grid.addWidget(self.quantity,2,1)
        self.grid.addWidget(self.line_edit,2,2)
        self.grid.addWidget(self.ok_button,3,1)
        self.grid.addWidget(self.close_button1,3,2)
        self.grid.addWidget(self.sales_report_button,4,1)
        self.grid.addWidget(self.empty,5,1)
        
        '''Creates place holders for sales report details'''
        self.number = QtGui.QLabel('') 
        self.total_cost = QtGui.QLabel('')
        self.total_sales = QtGui.QLabel('')
        self.profit2 = QtGui.QLabel('')
        self.number1 = QtGui.QLabel('')
        self.total_cost1 = QtGui.QLabel('')
        self.total_sales1 = QtGui.QLabel('')
        self.profit1 = QtGui.QLabel('') 
        '''add widgets to grid layout'''
        self.grid.addWidget(self.number,7,1)
        self.grid.addWidget(self.total_cost,8,1)
        self.grid.addWidget(self.total_sales,9,1)
        self.grid.addWidget(self.profit2,10,1)
        self.grid.addWidget(self.number1,7,2)
        self.grid.addWidget(self.total_cost,8,2)
        self.grid.addWidget(self.total_sales,9,2)
        self.grid.addWidget(self.profit1,10,2) 
        self.grid.addWidget(self.total_cost1,8,2)
        self.grid.addWidget(self.total_sales1,9,2)
        self.setLayout(self.grid)
        
    '''method for an ok button'''
    def ok(self):
        self.text = self.item_combo_box.currentText()
        self.line_edit1 = self.line_edit.displayText()
        dbfile = sqlite3.connect('tuckshopdetails.db')
        self.info_var = dbfile.execute('select Quantity_in_Stock from Stock where Name_of_item = ?',(self.text,));
        self.fetch_var = self.info_var.fetchone()
        dbfile.commit()
        self.info_var2 = dbfile.execute('select Cost_Price from Stock where Name_of_item =?',(self.text,))
        self.info_var3 = dbfile.execute('select Selling_Price from Stock where Name_of_item=?',(self.text,))
        self.info_var4 = self.info_var2.fetchone()
        self.info_var5 = self.info_var3.fetchone()
        self.line_edit.clear()
        if int(str(self.fetch_var)[1:2])>=int(self.line_edit1):
            dbfile.execute('insert into Sales values (?,?,?,?)',(int(str(self.fetch_var)[1:2]),self.line_edit1,str(datetime.now().date()),str(datetime.now().time()),))
            
            quantity=int(str(self.fetch_var)[1:2])-int(self.line_edit1)
            dbfile.execute('update Stock set Quantity_in_Stock=? where Name_of_item =? ',((quantity),(self.text),))
            self.profit = str(int(self.line_edit1)*int(str(self.info_var5)[1:3]) - int(self.line_edit1)*int(str(self.info_var4)[1:3]))
            dbfile.commit()
        elif int(str(self.fetch_var)[1:2])<int(self.line_edit1):
            self.empty.setText('Not enough stock to proceed with transaction')
            dbfile.commit()
        elif int(str(self.fetch_var[1:2]))==0:
            self.empty.setText('No Available stock')
            dbfile.commit()
        else:
            self.empty.setText('No Stock recognised')
            dbfile.commit()
    '''Method for sales report'''
    def sales_report(self):
        self.number.setText('Total Stock sold:')
        self.total_cost.setText('Total Cost Price:')
        self.total_sales.setText('Total Sales Price:')
        self.profit2.setText('Profit:')
        self.number1.setText(self.line_edit1)
        self.total_cost1.setText(str(self.info_var4)[1:3])
        self.total_sales1.setText(str(self.info_var5)[1:3])
        self.profit1.setText(self.profit)    

    '''Method for exit button'''   
    def close_button(self):
        sys.exit() 


def main():
        app= QtGui.QApplication(sys.argv)
        widget= POS()
        widget.show()
        sys.exit(app.exec_())
main()