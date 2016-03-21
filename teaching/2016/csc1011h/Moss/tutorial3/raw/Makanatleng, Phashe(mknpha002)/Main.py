from PyQt4 import QtGui, QtCore
import sys,sqlite3, time, os

class MainWidget(QtGui.QWidget):
    def __init__(self,parent= None):
        QtGui.QWidget.__init__(self,parent)
        
        self.setGeometry(300,300,600,300)
        
        self.setWindowTitle("Tuckshop Point of Sale")
        
        self.setWindowIcon(QtGui.QIcon("shop.png"))
        
        self.btnClose = QtGui.QPushButton("Close",self)
        
        self.Database = ''
        self.TableName1 = ''
        self.TableName2 = ''
        
        self.btnOk = QtGui.QPushButton("Ok",self)
        
        self.edit = QtGui.QLineEdit(self)
        
        self.cmbChoose = QtGui.QComboBox()
        
        self.btnReport = QtGui.QPushButton("Sales Report",self)
        
        self.lblHead = QtGui.QLabel("--------Tuck Shop (POS)--------",self)
        self.lblHead.setFont(QtGui.QFont("Courier",18,QtGui.QFont.Bold,False))
        
        self.lblChoose = QtGui.QLabel("Choose Item",self)
        self.lblChoose.setFont(QtGui.QFont("Courier",14))
        
        
        self.lblQuantity = QtGui.QLabel("Enter the Quantity",self)
        self.lblQuantity.setFont(QtGui.QFont("Courier",14))
        
        self.theGrid = QtGui.QGridLayout()

        self.theGrid.setRowMinimumHeight(0,30)
        self.theGrid.setRowMinimumHeight(1,15)
        self.theGrid.setRowMinimumHeight(2,15)
        self.theGrid.setRowMinimumHeight(3,15)
        self.theGrid.setRowMinimumHeight(4,15)
     
        self.theGrid.setColumnMinimumWidth(0,20)
        self.theGrid.setColumnMinimumWidth(1,100)
        
        self.theGrid.addWidget(self.btnClose,4,0)
        
        self.theGrid.addWidget(self.btnOk,3,1)
        
        self.theGrid.addWidget(self.edit,2,1)
        
        self.theGrid.addWidget(self.cmbChoose,1,1)
        
        self.theGrid.addWidget(self.btnReport,4,1)
        
        self.theGrid.addWidget(self.lblHead,0,0,1,2)
        
        self.theGrid.addWidget(self.lblQuantity,2,0)
        
        self.theGrid.addWidget(self.lblChoose,1,0)
        self.theGrid.setColumnStretch(0,100)
        self.theGrid.setColumnStretch(1,150)

        self.setLayout(self.theGrid)
        
        self.show()
        
        QtGui.QMessageBox.information(self,"Instructions","Choose the product you want in the drop down list and enter a quantity in the edit box")
        
        self.btnClose.clicked.connect(self.close_)
        self.btnOk.clicked.connect(self.RecordTransaction)
        self.btnReport.clicked.connect(self.runReport)
        
    def runReport(self):
        os.system('report.py')
    def DatabaseInfo(self,Database,TableName1,TableName2):
        self.Database = Database
        self.TableName1 = TableName1
        self.TableName2 = TableName2

    def PopulateList(self):
        
        db = sqlite3.connect(self.Database)
        cursor = db.execute("Select * from "+self.TableName1)
        tuple_ = []
        
        string = ""
        for row in cursor:
            #Stock Code,Name of Item,Item Description,Cost Price,Sales Price, Quantity in Stock
            tuple_ = row
            
            string = tuple_[1]+"_"+tuple_[2] #Adds Item Name and Description together
            
            self.cmbChoose.addItem(string) #adds items and description to combobox
            
    def RecordTransaction(self):
        
        choice = self.cmbChoose.currentText()
        choice = choice[0:choice.index("_")] #separating name from description
        QuantitySold = int(self.edit.displayText())
        db = sqlite3.connect(self.Database) # database we are reading from
        
        cursor = db.execute("Select * from "+self.TableName1)
        
        stockcode = ''
        salesprice = 0.00
        QuantityInStock = 0
        for row in cursor:
            if choice in row:
                stockcode = row[0]
                QuantityInStock = row[5]
                break #stop loop if item is found
            else:
                continue
            
        date_string = time.strftime("%Y/%m/%d")
        
        time_string = time.strftime("%H:%M:%S")
        
        QtGui.QMessageBox.information(self,"Information",stockcode+'_'+str(QuantitySold)+'_'+date_string+'_'+time_string+"---------"+str(QuantityInStock))
        
        if QuantitySold<QuantityInStock:
            db.execute("Insert into "+self.TableName2+" values (?,?,?,?)",(stockcode,QuantitySold,date_string,time_string))
            QuantityInStock = QuantityInStock-1
            aString = "Update "+self.TableName1+" set QuantityInStock = "+str(QuantityInStock)+" where StockCode = \""+stockcode+"\""
            
            db.execute("Update "+self.TableName1+" set QuantityInStock = "+str(QuantityInStock)+" where StockCode = \""+stockcode+"\"")
            
            QtGui.QMessageBox.information(self,"Information","Executed1")
            db.commit()
            QtGui.QMessageBox.information(self,"Information","Executed")
        else:
            if QuantityInStock==0:
                QtGui.QMessageBox.warning(self,"Information","Item "+choice+" out of Stock")
            else:
                QtGui.QMessageBox.warning(self,"Information","Quantity of Item in Stock : "+ QuantityInStock)
                
    def close_(self):
        self.close()
    
          
def main():
    app = QtGui.QApplication(sys.argv)
    
    widget = MainWidget()
    widget.DatabaseInfo("Tuckshop.db","Stock","SalesRecords")
    widget.PopulateList()
    sys.exit(app.exec_())
    
    
main()