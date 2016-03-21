# GuessingGame.py
# mantombi manqele
# 04/03/2016

import sys
from PyQt4 import QtGui
from random import *

random_num = randint(0,10)

class Guessing_Game(QtGui.QWidget):	# Guessing-Game inherits from QWidget
    def __init__(self, parent=None):  	# parent defines parent widget
        QtGui.QWidget.__init__(self, parent)	# parent class constructor
        self.setWindowTitle('Guessing Game')
        self.setMinimumSize(468, 260)
        
        self.counter=0
        label1 = QtGui.QLabel('Guesses:', self)
        label1.setFont(QtGui.QFont('Arial',14,3))
        label1.move(200, 15)	
        label2 = QtGui.QLabel('Interface:', self)
        label2.setFont(QtGui.QFont('Arial',14,3))
        label2.move(200, 133)
        
        close = QtGui.QPushButton("Close",self)		# create close button
        close.setGeometry(200, 220, 75, 25)
        close.clicked.connect(self.Quit)                # connect close button to quit game
        self.new_game = QtGui.QPushButton("New Game", self)	# create cancel button
        self.new_game.clicked.connect(self.reset)
        self.new_game.setGeometry(280, 220, 75, 25)
        guess = QtGui.QPushButton("Guess",self)		# create guess button
        guess.clicked.connect(self.Game)                # connect guess button
        guess.setGeometry(360, 100, 75, 25)  
        change = QtGui.QPushButton("Change",self)		# create change button
        change.clicked.connect(self.Colour_Picture)           # connect change button
        change.setGeometry(360, 189, 75, 25)        
        
        self.combo = QtGui.QComboBox(self) 
        self.combo.addItem('red') 	# adds item to combobox  
        self.combo.setGeometry(280, 190, 75, 23)
        self.combo.addItem('blue')
        self.combo1 = QtGui.QComboBox(self) 
        self.combo1.addItem('mickey') 	 
        self.combo1.setGeometry(280, 160, 75, 23)
        self.combo1.addItem('pluto')    
        
        self.edit = QtGui.QLineEdit(self)	             # create LineEdit
        self.edit.setGeometry(280, 100, 75, 25)
        
        self.setPalette(QtGui.QPalette(QtGui.QColor('red')))  # default background colour
        self.setAutoFillBackground(True)  

        self.pixmap = QtGui.QPixmap('mickey.gif')       # default picture colour
        self.pic_label = QtGui.QLabel(self) 
        self.pic_label.setPixmap(self.pixmap)
        
        field1=QtGui.QLabel("Guess 1:",self)        # create fields for guesses
        field1.setGeometry(200,45,42,10)
        field2=QtGui.QLabel("Guess 2:",self)
        field2.setGeometry(200,65,42,10)
        field3=QtGui.QLabel("Guess 3:",self)
        field3.setGeometry(200,85,42,10)
        
        self.field4=QtGui.QLabel("",self)         # create fields for guesses entered by user
        self.field4.setGeometry(280,45,42,10)
        self.field5=QtGui.QLabel("",self)
        self.field5.setGeometry(280,65,42,10)
        self.field6=QtGui.QLabel("",self)
        self.field6.setGeometry(280,85,42,10)  
        
        self.field7=QtGui.QLabel("",self)        # create fields to indicate if the values entered are too high, too small or correct
        self.field7.setGeometry(362,45,42,12)
        self.field8=QtGui.QLabel("",self)
        self.field8.setGeometry(362,65,42,12)
        self.field9=QtGui.QLabel("",self)
        self.field9.setGeometry(362,85,42,12)        

    def Quit(self):
        sys.exit()
        
    def Colour_Picture(self):
        c_name=self.combo.currentText()
        p_name=self.combo1.currentText()
        
        if c_name=="blue":
            self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            self.setAutoFillBackground(True) 
            if p_name=="pluto":
                self.pixmap = QtGui.QPixmap('pluto.gif')
                self.pic_label.setPixmap(self.pixmap)                 
                self.pic_label.show()
            else:
                self.pixmap = QtGui.QPixmap('mickey.gif')
                self.pic_label.setPixmap(self.pixmap)                 
                self.pic_label.show()                
        elif c_name=="red":
            self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            self.setAutoFillBackground(True) 
            if p_name=="pluto":
                self.pixmap = QtGui.QPixmap('pluto.gif')
                self.pic_label.setPixmap(self.pixmap)                 
                self.pic_label.show()
            else:
                self.pixmap = QtGui.QPixmap('mickey.gif')
                self.pic_label.setPixmap(self.pixmap)                 
                self.pic_label.show()                       
                
    def Game(self):
        number=self.edit.displayText()
        if int(number)>random_num and self.counter==0:
                self.field4.setText(number)
                self.field7.setText("Too high")
                self.edit.clear()
                self.counter+=1
        elif int(number)>random_num and self.counter==1:
            self.field5.setText(number)
            self.field8.setText("Too high")
            self.edit.clear()
            self.counter+=1 
        
        elif int(number)>random_num and self.counter==2:
            self.field6.setText(number)
            self.field9.setText("Too high")
            self.edit.clear()
            self.counter+=1 
        elif int(number)<random_num and self.counter==0:
            self.field4.setText(number)
            self.field7.setText("Too small")
            self.edit.clear()
            self.counter+=1
        elif int(number)<random_num and self.counter==1:
            self.field5.setText(number)
            self.field8.setText("Too small")
            self.edit.clear()
            self.counter+=1 
            
        elif int(number)<random_num and self.counter==2:
            self.field6.setText(number)
            self.field9.setText("Too small")
            self.edit.clear()
            
            
        if int(number)==random_num and self.counter==0:
            self.field4.setText(number)
            self.field7.setText("Correct")
            self.edit.clear()
            self.counter+=1
        elif int(number)==random_num and self.counter==1:
            self.field5.setText(number)
            self.field8.setText("Correct")
            self.edit.clear()
            
            
        elif int(number)==random_num and self.counter==2:
            self.field6.setText(number)
            self.field9.setText("Correct")
            self.edit.clear()
            
    def reset(self):
        self.counter=0
        self.field4.clear()
        self.field5.clear()
        self.field6.clear()
        self.field7.clear()
        self.field8.clear()
        self.field9.clear()
        
def main():
    app = QtGui.QApplication(sys.argv)
    my_widget = Guessing_Game()		# create Guessing_Game object
    my_widget.show()
    sys.exit(app.exec_()) 
main()