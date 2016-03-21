import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from sqlite3 import*


class POS(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(300,300,400,400)
        self.setWindowTitle('Point of Sale')
        
        combo=QtGui.QComboBox()
        db1=connect('Point of sale.db')
        self.db2=db1.execute('select stock_code from Stock')
        for i in self.db2:
            combo.addItem(str(i))
        label=QtGui.QLabel('Quantity:')
        label1=QtGui.QLabel('Select Stock code:')
        edit=QtGui.QLineEdit()
        ok=QtGui.QPushButton('OK')
        report=QtGui.QPushButton('report')
        self.cancel=QtGui.QPushButton('Close')
        grid=QtGui.QGridLayout()
        grid.addWidget(combo,0,1)
        grid.addWidget(label1,0,0)
        grid.addWidget(label,1,0)
        grid.addWidget(edit,1,1)
        grid.addWidget(ok,2,0)
        grid.addWidget(self.cancel,2,1)
        grid.addWidget(report)
        self.setLayout(grid)
        
        
        self.connect(self.cancel,QtCore.SIGNAL('clicked()'), self.buttonClicked)
    def buttonClicked(self):
        self.close()
        
        
        
        
def main():
    app=QtGui.QApplication(sys.argv)
    P=POS()
    P.show()
    
    sys.exit(app.exec_())
main()
        

