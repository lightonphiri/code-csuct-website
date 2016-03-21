# Ndlovu Mxoleleni'
# NDLMXO003
# POS

"""importing required modules"""
import sys
from PyQt4 import QtGui
import sqlite3

class Point_of_sale(QtGui.QWidget):         # creating guessing Game class
    def __init__(self, parent=None):            # parent defines parent widget
        QtGui.QWidget.__init__(self, parent)            # super class constructor
        self.setGeometry(650,250,250,200)               # x,y,width,height based on screen
        self.setWindowTitle("Point Of Sale")            # set window title
        
        self.edit = QtGui.QLineEdit()
        
        self.ok = QtGui.QPushButton("OK")
        
        self.close = QtGui.QPushButton("Close")
        self.close.clicked.connect(self.ButtonClicked)
        
        self.combo_1 = QtGui.QComboBox()
        self.combo_1.addItem("500ml Can")
        self.combo_1.addItem("Energade")
        self.combo_1.addItem("maynards")
        self.combo_1.addItem("Pie")
        self.combo_1.addItem("Popcorn")
        self.combo_1.addItem("Toppper biscuits")
        self.combo_1.addItem("Eet Sum Moo")
        self.combo_1.addItem("Still Water")
        self.combo_1.addItem("Orbit Gum")
        self.combo_1.addItem("Lays Chips")
        
        grid = QtGui.QGridLayout()          # create grid layout
        
        """# add items in their position"""
        grid.addWidget(self.combo_1,0,0)
        grid.addWidget(self.edit,0,1)
        grid.addWidget(self.ok,1,0)
        grid.addWidget(self.close,1,1)
        
        self.setLayout(grid) 
        
        
    def ButtonClicked(self):            # defining a close function called ButtonClicked
        sys.exit()        
        
        
def main():         # defining main()
    app = QtGui.QApplication(sys.argv)
    my_widget = Point_of_sale()         # create MyWidget object
    my_widget.show()
    sys.exit(app.exec_())
    
main()           # calling the main function