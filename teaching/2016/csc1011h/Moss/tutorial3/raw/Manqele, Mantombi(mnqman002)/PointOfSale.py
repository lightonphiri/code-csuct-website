# point of sale system 
# mantombi manqele
# 12/03/2016

from PyQt4 import QtGui
import sqlite3
import sys
from datetime import datetime

conn = sqlite3.connect('Stock_Table.db')
c=conn.cursor()

class Point_Of_Sale(QtGui.QWidget):	# Point_Of_Sale inherits from QWidget
    def __init__(self, parent=None):  	# parent defines parent widget
        QtGui.QWidget.__init__(self, parent)	# parent class constructor
        self.setWindowTitle("Point Of Sale System")
        self.setMinimumSize(430, 290)
        
        label1 = QtGui.QLabel("Ntombi's Tuck Shop", self)
        label1.setFont(QtGui.QFont('Times',14,3))
        label1.move(5, 15)	
        label2 = QtGui.QLabel('Select item to be sold:', self)
        label2.setFont(QtGui.QFont('Arial',12,1))
        label2.move(5, 60) 
        label3 = QtGui.QLabel('Enter the quantity:', self)
        label3.setFont(QtGui.QFont('Arial',12,1))
        label3.move(5, 100)     
        self.combo = QtGui.QComboBox(self) 
        self.combo.addItem('Bread') 	# adds item to combobox  
        self.combo.addItem('Milk')
        self.combo.addItem('Fruit Juice')
        self.combo.addItem('Eggs')
        self.combo.addItem('Jam')
        self.combo.addItem('Peanut Butter')
        self.combo.addItem('Ice Cream')
        self.combo.addItem('Coffee')
        self.combo.addItem('Tea')
        self.combo.addItem('Rice')
        self.combo.setGeometry(230, 60, 75, 23) 
        
        self.edit = QtGui.QLineEdit(self)	             # create LineEdit
        self.edit.setGeometry(230, 100, 75, 25)        
        
        self.setPalette(QtGui.QPalette(QtGui.QColor('magenta')))  # background colour
        self.setAutoFillBackground(True)  
        
        ok = QtGui.QPushButton("Okay",self)		# create okay button
        ok.clicked.connect(self.Select)                # connect okay button
        ok.setGeometry(330, 100, 75, 25)    
        close = QtGui.QPushButton("Close",self)       # create close button 
        close.clicked.connect(self.Quit)                # connect close button
        close.setGeometry(210, 250, 100, 25)
        report = QtGui.QPushButton("View Sales Report",self)		# create okay button
        report.clicked.connect(self.Sales_Report)                # connect sales report button
        report.setGeometry(100, 250, 100, 25)
        
        self.field = QtGui.QLabel("",self)
        self.field.setGeometry(5,150,500,25)
        self.field.setFont(QtGui.QFont('Arial',12,1))
        
        self.pixmap = QtGui.QPixmap("") 
        self.pic_label = QtGui.QLabel() 
        self.pic_label.setPixmap(self.pixmap)        

    def Quit(self):
        sys.exit() 
            
    def Sales_Report(self):
        c.execute("SELECT *FROM Sale")
        items = c.fetchall()
        stockcode=[]
        total_items=0
        for i in items:
            total_items+=int(i[1])
            stockcode.append(str(i[0]))
        c.execute("SELECT *FROM Stock")
        
        name= c.fetchall()  
        costprice=0
        salesprice=0
        for i in name:
            if str(i[0]) in stockcode:
                salesprice+=int(i[4])
                costprice+=int(i[3])
        profit=salesprice-costprice
        profit="R"+str(profit)
        salesprice="R"+str(salesprice)
        costprice="R"+str( costprice)
        
        self.pic_label.setPixmap(self.pixmap) 
        self.pic_label.setGeometry(80,100,300,300)
        self.pic_label.setPalette(QtGui.QPalette(QtGui.QColor('magenta')))  # background colour
        self.pic_label.setAutoFillBackground(True)
        sr = QtGui.QLabel("SALES REPORT",self.pic_label)
        sr.setFont(QtGui.QFont('Times',14,3))
        self.pic_label.setFont(QtGui.QFont('Arial',12,1))
        sold = QtGui.QLabel("Total number of items sold:",self.pic_label)
        sold.move(5,20)
        cp = QtGui.QLabel("Total cost price:",self.pic_label)
        cp.move(5,40)     
        sp = QtGui.QLabel("Total sales price:",self.pic_label)
        sp.move(5,60)     
        prof = QtGui.QLabel("Total profit:",self.pic_label)
        prof.move(5,80)        
        label=QtGui.QLabel(str(total_items),self.pic_label)
        label.move(250,20)        
        label=QtGui.QLabel(costprice,self.pic_label)
        label.move(250,40)
        label2=QtGui.QLabel(salesprice,self.pic_label)
        label2.move(250,60)
        label3=QtGui.QLabel(profit,self.pic_label)
        label3.move(250,80)        
        
        self.pic_label.show()
    
        
    def Select(self):
        item=self.combo.currentText()
        quantity=self.edit.displayText()
        c.execute("SELECT *FROM Stock WHERE Item=? ",(item,))
        info=c.fetchone()
        if int(quantity)<=int(info[-1]):
            self.field.clear()
            date=str(datetime.now())[0:11]
            time=str(datetime.now())[11:19]
            code=info[0]
            c.execute("INSERT INTO Sale(Code, Quantity, Date, Time) values(?,?,?,?)",(code,quantity,date,time))
            answer=int(info[-1])-int(quantity)
            print(answer)
            c.execute("UPDATE Stock SET Quantity=(?) WHERE Code=(?)",(answer,int(info[0]),))
            self.edit.clear()
            conn.commit()
        else:
            self.field.setText("Insufficient quantity entered for item.")
            self.edit.clear()
def main():
    app = QtGui.QApplication(sys.argv)
    my_widget = Point_Of_Sale()		# create Point_Of_Sale() object
    my_widget.show()
    sys.exit(app.exec_()) 

main()