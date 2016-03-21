import os,sys
import random
from time import *
from PyQt4 import QtGui,QtCore
         
class GuessingGame(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(600,50,480,300)
        self.setWindowTitle("Guessing Game")
        # Create place for Picture
        self.pic = QtGui.QLabel(self)
    
        header1=QtGui.QLabel("Guesses:",self)
        header1.setFont(QtGui.QFont("Arial",15,2))
        header1.move(210,30)
        guess1=QtGui.QLabel("Guess 1:",self)
        guess1.move(210,60)
        guess2=QtGui.QLabel("Guess 2:",self)
        guess2.move(210,80)        
        guess3=QtGui.QLabel("Guess 2:",self)
        guess3.move(210,100)        
        
        header2=QtGui.QLabel("Interface:",self)
        header2.setFont(QtGui.QFont("Arial",15,2))
        header2.move(210,150)
        guess4=QtGui.QLabel("Picture:",self)
        guess4.move(210,180)
        guess5=QtGui.QLabel("colour:",self)
        guess5.move(210,205)
        
        self.edit=QtGui.QLineEdit(self)
        self.edit.setGeometry(290,130,70,20)
    
        close_button=QtGui.QPushButton("Close",self)
        self.new_game_button=QtGui.QPushButton("New Game",self)
        close_button.setGeometry(210,240,70,20)
        self.new_game_button.setGeometry(290,240,70,20)
        self.guess_button=QtGui.QPushButton("Guess",self)
        self.guess_button.setGeometry(370,130,70,20)
        self.chng_button=QtGui.QPushButton("Change",self)
        self.chng_button.setGeometry(370,213,70,20)
        
        self.combo_picture=QtGui.QComboBox(self)
        self.combo_picture.addItem("mickey")
        self.combo_picture.addItem("pluto")
        self.combo_picture.setGeometry(290,185,70,20)
         
        self.combo_colour=QtGui.QComboBox(self)
        self.combo_colour.addItem("red")
        self.combo_colour.addItem("blue")
        self.combo_colour.setGeometry(290,213,70,20)
                        
        grid=QtGui.QGridLayout()
        grid.addWidget(self.pic,0,0)
        self.setLayout(grid)
        
        close_button.clicked.connect(self.closed)
        self.chng_button.clicked.connect(self.color_picture_selector)
        self.new_game_button.clicked.connect(self.new_game)
        
        self.ans1=QtGui.QLabel(self)
        self.ans1.move(290,65)
        self.message1=QtGui.QLabel(self)
        self.message1.move(370,65)
        self.message2=QtGui.QLabel(self)
        self.message2.move(370,85)
        self.message3=QtGui.QLabel(self)
        self.message3.move(370,105)            
        self.ans2=QtGui.QLabel(self)
        self.ans2.move(290,80)
        self.ans3=QtGui.QLabel(self)
        self.ans3.move(290,100)
         
        # Defaut Picture and colour.      
        self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        self.setAutoFillBackground(True)   
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/mickey.gif"))
    
    def new_game(self):
        self.ans1.clear()
        self.ans2.clear()
        self.ans3.clear()
        self.message1.clear()
        self.message2.clear()
        self.message3.clear()
        self.edit.clear()
        
    def color_picture_selector(self):
        text=self.combo_colour.currentText()
        self.setPalette(QtGui.QPalette(QtGui.QColor(str(text))))
        self.setAutoFillBackground(True)        
        text=self.combo_picture.currentText()
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/"+str(text)+".gif"))
        
    def closed(self):
        self.close() 
        
def main():      
    app=QtGui.QApplication(sys.argv)
    widget=GuessingGame()
    widget.show()    
    sys.exit(app.exec_())
main()