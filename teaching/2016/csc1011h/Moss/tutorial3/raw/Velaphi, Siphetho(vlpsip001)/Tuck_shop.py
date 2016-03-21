import sys
from PyQt4 import QtGui
import sqlite3
#import Stock_table
conn=sqlite3.connect("Stock_table.db")
p=conn.cursor()
conn2=sqlite3.connect("Sale.db")
t=conn2.cursor()

from datetime import datetime
class MyWidget(QtGui.QWidget):	# MyWidget inherits from QWidget
    def __init__(self, parent=None):  	# parent defines parent widget
        QtGui.QWidget.__init__(self, parent)	# super class constructor
        self.setGeometry(250, 250, 400, 300)       	# x,y,width,height
        self.setWindowTitle('Widget Window')  #set window tit
        
        self.box=QtGui.QComboBox()
        self.box.addItem('Banana')
        self.box.addItem('Apple')
        self.box.addItem('Guava')
        self.box.addItem('Peach')
        self.box.addItem('Mango')
        self.box.addItem('Pear')
        self.box.addItem('Orange')
        self.box.addItem('Chery')
        self.box.addItem('Rusrberry')
        self.box.addItem('Ovacado')
        self.edit=QtGui.QLineEdit()
        self.fruit_label=QtGui.QLabel("Choose fruit:")
        self.edit_label= QtGui.QLabel("How many:")
        self.ok_button= QtGui.QPushButton("OK")
        self.ok_button.clicked.connect(self.ok)
        self.report_button=QtGui.QPushButton('Sales report')
        self.report_button.clicked.connect(self.report)
        self.close_button=QtGui.QPushButton("Close")
        self.close_button.clicked.connect(self.buttonClicked)
        self.grid=QtGui.QGridLayout()
        self.grid.addWidget(self.fruit_label,0,0)
        self.grid.addWidget(self.box,0,1)
        self.grid.addWidget(self.edit_label,1,0)
        self.grid.addWidget(self.edit,1,1)
        self.grid.addWidget(self.ok_button,2,0)
        self.grid.addWidget(self.report_button,2,1)
        self.grid.addWidget(self.close_button,2,2)
        self.setLayout(self.grid)
        self.error=QtGui.QLabel("",self)
        self.error.setGeometry(20,150,200,50)
        self.Vbox=QtGui.QVBoxLayout()
        self.sold_label= QtGui.QLabel("")
        self.cost_label=QtGui.QLabel("")
        self.sale_label=QtGui.QLabel("")
        self.profit_label=QtGui.QLabel("")
        self.Vbox.addWidget(self.sold_label)
        self.Vbox.addWidget(self.cost_label)
        self.Vbox.addWidget(self.sale_label)
        self.Vbox.addWidget(self.profit_label)
        self.widget=QtGui.QWidget()
        
        self.widget.setLayout(self.Vbox)
        
    def buttonClicked(self):		# buttonClicked slot event handler
        self.close()
    def ok(self):
        quantity= self.edit.displayText()
        item= self.box.currentText()
        p.execute("SELECT *FROM Stock WHERE Item=?",(item,))
        items=p.fetchone()
        date=str(datetime.now())[0:11]
        time=str(datetime.now())[11:19]
       
        if int(items[-1])>=int(quantity):
            self.error.clear()
            
            t.execute("INSERT INTO sale(stock,Quantity,Time,Date) values(?,?,?,?)",(items[0],items[-1],time,date)) 
            conn2.commit()
            left_stock=int(items[-1])-int(quantity)
            p.execute("UPDATE Stock SET Quantity=(?) WHERE Item=(?)",(left_stock,item,))
            conn.commit()
            self.edit.clear()
        else:
            self.error.setText("Item is out of Stock")
            self.edit.clear()
            
    def report(self):
        self.widget.setGeometry(20,20,300,300)
        t.execute("SELECT *FROM sale")
        items=t.fetchall() 
        total_number_of_items=0
        stockcode=[]
        for i in items:
            total_number_of_items+=int(i[1])
            stockcode.append(str(i[0]))
        total_number_of_items=str(total_number_of_items)
        p.execute("SELECT *FROM Stock")
        item=p.fetchall() 
        saleprice=0
        costprice=0
        print(item)
        for i in item:
            costprice+=i[3]
            saleprice+=i[4]
        profit=str(costprice-saleprice)
        costprice=str(costprice)
        saleprice=str(saleprice)        
        print(profit)
        self.profit_label.setText("The total profit:   R"+profit)
        self.cost_label.setText("The cost price:   R"+costprice)
        self.sale_label.setText("The sales price:   R"+saleprice)
        self.sold_label.setText("Total items sold  "+total_number_of_items)
        self.widget.show()        
        
def main():
    app = QtGui.QApplication(sys.argv)
    my_widget = MyWidget()		# create MyWidget object
    my_widget.show()
    sys.exit(app.exec_())
main()