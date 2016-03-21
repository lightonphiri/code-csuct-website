from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import QtCore

import sys

class button(QWidget):
    def __init__(self, parent = None, widget=None):    
        QWidget.__init__(self, parent)
        layout = QGridLayout(self)
 
class GuessingGame(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.button = QPushButton('Guess', self)
        self.button.move(380, 85)        
        self.resize(470, 260)
        self.button = QPushButton("Change",self)
        self.button.move(380,177)
        self.button = QPushButton("Close",self)
        self.button.move(225,207)
        self.button = QPushButton("New Game",self)
        self.button.move(305,207)
        self.setWindowTitle('Guessing Game')        #title the window
        
        # guesses interface
        
        heading = QtGui.QLabel('Guesses:',self)	    # create label
        heading.setFont(QtGui.QFont("Arial",15))
        heading.move(225, 10)			    # x,y based on window
        labelG1 = QtGui.QLabel("Guess 1:", self)
        labelG1.move(225, 40)
        labelG2 = QtGui.QLabel("Guess 2:", self)
        labelG2.move(225, 55)			    # x,y based on window
        labelG3 = QtGui.QLabel("Guess 3:", self)
        labelG3.move(225, 70)
        edit = QtGui.QLineEdit(self)
        edit.setGeometry(300,87,70,20)
        
        # layout control interface
        heading2 = QtGui.QLabel("Interface:",self)
        heading2.setFont(QtGui.QFont("Arial",15))
        heading2.move(225,120)
        pic = QtGui.QLabel("Picture:",self)
        pic.move(225, 150)
        col = QtGui.QLabel("Colour:",self)
        col.move(225, 180)
        
        
        # combo boxes for colour pick
        self.cp = ["red", "blue"]     # Create and fill the combo box to choose the colourpick
        self.colourpick = QComboBox(self)
        self.colourpick.addItems(self.cp)
        self.colourpick.setMinimumWidth(100)
        self.colourpick.move(270, 179) 
        
        # combo boxes for image pick
        self.pp = ["mickey", "pluto"]     # Create and fill the combo box to choose the colourpick
        self.picturepick = QComboBox(self)
        self.picturepick.addItems(self.pp)
        self.picturepick.setMinimumWidth(100)
        self.picturepick.move(270, 149)     
        
        

        
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = GuessingGame()
    win.show()
    sys.exit(app.exec_())