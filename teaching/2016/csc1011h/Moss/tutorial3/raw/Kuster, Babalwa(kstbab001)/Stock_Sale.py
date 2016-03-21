import sys
from PyQt4 import QtGui,QtCore
import sqlite3
from datetime import date, datetime

class ItemsSold(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(250, 250, 200, 150)
        self.setWindowTitle('Sale')
        
        #label
        title =  QtGui.QLabel('The Amazing Fruit!!!',self)
        quantity = QtGui.QLabel('Quantity Number:',self)
        select = QtGui.QLabel('Select Item:',self)        
        edit = QtGui.QLineEdit(self)
        title .setFont(QtGui.QFont('Chiller',30))
        report = QtGui.QLabel('Sale Report:',self)
        
        #button
        self.ok=QtGui.QPushButton('Ok')
        self.cancel=QtGui.QPushButton('Cancel')
        self.report=QtGui.QPushButton("Report")
        
        #combo
        self.combo=QtGui.QComboBox()
        self.combo.addItem('Watermelon')
        self.combo.addItem('Orange')
        self.combo.addItem('Avocado')
        self.combo.addItem('Mango')
        self.combo.addItem('Kiwi')
        self.combo.addItem('Strawberry')
        self.combo.addItem('Pineapple')
        self.combo.addItem('Pulm')
        self.combo.addItem('Banana')
        self.combo.addItem('Apple')
        
        #pic
        self.pic=QtGui.QPixmap('new.jpg')
        self.pic_label=QtGui.QLabel()
        self.pic_label.setPixmap(self.pic) 
        
        #grid
        grid=QtGui.QGridLayout()
        grid.addWidget(title,0,0,1,2)
        grid.addWidget(self.pic_label,1,0,2,2)
        grid.addWidget(select,5,0)
        grid.addWidget(self.combo,5,1)
        grid.addWidget(quantity,6,0)
        grid.addWidget(edit,6,1)
        grid.addWidget(self.ok,7,0)
        grid.addWidget(self.cancel,7,1)
        grid.addWidget(report,8,0)
        grid.addWidget(self.report,8,1)        
        self.setLayout(grid)
        self.setPalette(QtGui.QPalette(QtGui.QColor('lime')))
        self.connect(self.ok,QtCore.SIGNAL('clicked()'), self.OK)
        self.connect(self.cancel,QtCore.SIGNAL('clicked()'), self.CANCEL)
        self.connect(self.report,QtCore.SIGNAL('clicked()'), self.REPORT)
        #REAL DEAL 
    def OK(self):
        self.db = sqlite3.connect('Stock_Items.db')
        self.cur =self.db.cursor()
        self.today = datetime.now()
        self.text=self.combo.currentText()
        self.text_edit=self.edit.displayText()
        quant=list(self.cur.execute('select Quantity_Stock from Stock_Items=?',(self.text)))
        code=list(self.cur.execute('select Stock_Code from Stock_Items=?',(self.text)))
        self.db.commit()
        if int(self.text_edit)==quant[0] or int(self.text_edit)<quant[0]:
            self.insert = self.cur.execute('INSERT into Sale_Price values (?,?,?)',(code[0],quant[0],self.today)) 
            self.new_num=quant[0]-int(text_edit)
            self.update= self.cur.execute('UPDATE Stock  SET Quantity_Stock=? WHERE Item_Name=?',(self.new_num,self.text))
        else:
            error=("There is no sufficient quantity of item selected")
            return error
    def CANCEL(self):
        sys.exit()       
    def REPORT(self):
                '''#self.db = sqlite3.connect('Stock_Items.db')
                self.cur = self.db.cursor()		
                self.text = self.combo.currentText()
                self.All = self.cur.execute('SELECT * FROM Stock WHERE Item_Name=?',(self.text))
                self.List=list(self.All)
                self.profit= self.All[4]-self.All[3]
                
                
                app1 = QtGui.QApplication(sys.argv)   						
                widget = QtGui.QWidget() 	
                widget.resize(300, 200)	
                widget.setWindowTitle('Sale Report')
                
                sale_R = QtGui.QLabel('SALE REPORT',self)
                item_num = QtGui.QLabel('Number of items:',self)
                cost = QtGui.QLabel('Cost price:',self)
                sale = QtGui.QLabel('Sale price:',self)
                prof = QtGui.QLabel('Profit:',self)
                item_hold=QtGui.QLabel('',self)
                cost_hold=QtGui.QLabel('',self)
                sale_hold=QtGui.QLabel('',self)
                prof_hold=QtGui.QLabel('',self)
                
                grid1=QtGui.QGridLayout()
                grid1.addWidge(sale_R,0,0,1,2)
                grid1.addWidge(item_num,1,0)
                grid1.addWidge(item_hold,1,1)
                grid1.addWidge(cost,2,0)
                grid1.addWidge(cost_hold,2,1)
                grid1.addWidge(sale,3,0)
                grid1.addWidge(sale_hold,3,1)
                grid1.addWidge(prof,4,0)
                grid1.addWidge(prof_hold,4,)
                self.setLayout(grid1)
                widget.show() 		
                sys.exit(app.exec_()) 	'''
        
def main():
    app = QtGui.QApplication(sys.argv)
    sale=ItemsSold()
    sale.show()
    sys.exit(app.exec_())
            
main()
            