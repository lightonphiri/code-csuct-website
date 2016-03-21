import sys
from PyQt4 import QtGui, QtCore


class SalesWidget(QtGui.QWidget):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        #setting up window with dimensions, title and background colour
        self.setGeometry(250, 250, 250, 200)
        self.setWindowTitle('Sales Window')
        self.setPalette(QtGui.QPalette(QtGui.QColor('magenta')))
        self.setAutoFillBackground(True)
        
        #creating combobox, adding items in and setting maximum and minimum dimensional values
        self.stock_combo_label=QtGui.QComboBox()
        self.stock_combo_label.addItem('Monster')
        self.stock_combo_label.addItem('Oreo')
        self.stock_combo_label.addItem('Colddrink')
        self.stock_combo_label.addItem('Peanuts')
        self.stock_combo_label.addItem('Chocstix')
        self.stock_combo_label.addItem('Mini cheddars')
        self.stock_combo_label.addItem('Doritos')
        self.stock_combo_label.addItem('Water')
        self.stock_combo_label.addItem('Cigarettes')
        self.stock_combo_label.addItem('Bread')
        self.stock_combo_label.setMaximumSize(150,25)
        self.stock_combo_label.setMinimumSize(100,25)
        
        #Creating line edit and setting maximum and minimum dimensional values
        self.edit_quantity=QtGui.QLineEdit()
        self.text=self.edit_quantity.displayText()
        self.edit_quantity.setMaximumSize(150,25)
        self.edit_quantity.setMinimumSize(100,25)
        
        #creating ok button and setting maximum and minimum dimensional values
        self.ok=QtGui.QPushButton('OK')
        self.ok.setMaximumSize(150,25)
        self.ok.setMinimumSize(100,25)
        
        #creating cancel button and setting maximum and minimum dimensional values
        self.cancel=QtGui.QPushButton('Cancel')
        self.cancel.setMaximumSize(150,25)
        self.cancel.setMinimumSize(100,25)

        #creating report button and setting maximum and minimum dimensional values
        self.report=QtGui.QPushButton('Report')
        self.report.setMaximumSize(120,25)
        self.report.setMinimumSize(80,25)        

        #Horizontal_1 layout being set, and added widgets
        hbox1=QtGui.QHBoxLayout()
        hbox1.addWidget(self.stock_combo_label)
        hbox1.addStretch(5)
        hbox1.addWidget(self.edit_quantity)
        hbox_widget1=QtGui.QWidget()
        hbox_widget1.setLayout(hbox1)
        
        #Horizontal_2 layout being set, and added widgets
        hbox2=QtGui.QHBoxLayout()
        hbox2.addWidget(self.ok)
        hbox2.addStretch(5)
        hbox2.addWidget(self.cancel)
        hbox_widget2=QtGui.QWidget()
        hbox_widget2.setLayout(hbox2)        
        
        #VBox layout containing horizontal layout widgets
        vbox=QtGui.QVBoxLayout()
        vbox.addWidget(hbox_widget1)
        vbox.addWidget(hbox_widget2)
        vbox.addWidget(self.report)
        vbox_widget=QtGui.QWidget()
        self.setLayout(vbox)        
        
        #connecting buttons        
        self.ok.clicked.connect(self.okClicked)
        self.cancel.clicked.connect(self.closeClicked)
        self.report.clicked.connect(self.reportClicked)
        
    def okClicked(self):
        print(self.text) #prints text from line edit
    
    def closeClicked(self):
        self.close() #closes the window
    
    def reportClicked(self):
        pass #no function
        
def main():
    #activates and closes the window createed above
    app=QtGui.QApplication(sys.argv)
    sales_widget=SalesWidget()
    sales_widget.show()
    sys.exit(app.exec_())
    
main()