# An GUI program that creates a Guessing Game 
# Xhanti Singatha
# 04 March 2016


import random
import sys

from PyQt4 import QtGui, QtCore

class GuessingGame(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(250,250,200,150)
        self.setWindowTitle('Guessing Game')
        self.guess_num = random.randint(1,10)     # generating the random number 
        self.i = 1                                # keeps track of the number guesses 
        
        # colour
        
        self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        self.setAutoFillBackground(True)        
        
        # setting the image
        
        self.pic = QtGui.QPixmap('mickey.gif')
        self.picture_label = QtGui.QLabel(self)      
        self.picture_label.setPixmap(self.pic)
        
        # creating the controls
        
        label = QtGui.QLabel('Guesses:',self)
        label.setFont(QtGui.QFont('Times',20,2))    # setting the font
        
        guess1 = QtGui.QLabel('Guess 1:',self)      # guess 1 label
        guess2 = QtGui.QLabel('Guess 2:',self)      # guess 2 label
        guess3 = QtGui.QLabel('Guess 3:',self)      # guess 3 label
    
        self.edit_bar = QtGui.QLineEdit()
        self.guess = QtGui.QPushButton('Guess')
        
        label2 = QtGui.QLabel('Interface:',self)    # interface label
        label2.setFont(QtGui.QFont('Times',20,2))   # setting the font 
        
        picture = QtGui.QLabel('Picture:',self)      # picture label
        colour = QtGui.QLabel('Colour:',self)       # colour label
        
        self.change = QtGui.QPushButton('Change')
        self.close = QtGui.QPushButton('Close')
        self.new_game = QtGui.QPushButton('New Game')
        
        self.picture_combo = QtGui.QComboBox()
        self.picture_combo.addItem('mickey')
        self.picture_combo.addItem('pluto')
        
        self.colour_combo = QtGui.QComboBox()
        self.colour_combo.addItem('red')
        self.colour_combo.addItem('blue')
        
        self.guess_label1 = QtGui.QLabel('')
        self.guess_label2 = QtGui.QLabel('')
        self.guess_label3 = QtGui.QLabel('')
        
        self.output1 = QtGui.QLabel('')
        self.output2 = QtGui.QLabel('')
        self.output3 = QtGui.QLabel('')
        
        # layout of the controls
        
        grid = QtGui.QGridLayout()
        grid.addWidget(self.picture_label,0,0,8,1)
        
        grid.addWidget(label,0,1)
        grid.addWidget(guess1,1,1)
        grid.addWidget(guess2,2,1)
        grid.addWidget(guess3,3,1)
        
        grid.addWidget(self.guess_label1,1,2)
        grid.addWidget(self.guess_label2,2,2)
        grid.addWidget(self.guess_label3,3,2)        
        
        grid.addWidget(self.output1,1,3)
        grid.addWidget(self.output2,2,3)
        grid.addWidget(self.output3,3,3)
        
        grid.addWidget(self.edit_bar,4,2)
        grid.addWidget(self.guess,4,3)
        grid.addWidget(label2,5,1)
        grid.addWidget(picture,6,1)
        grid.addWidget(self.picture_combo,6,2)
        grid.addWidget(colour,7,1)
        grid.addWidget(self.colour_combo,7,2)
        grid.addWidget(self.change,7,3)
        grid.addWidget(self.close,8,1)
        grid.addWidget(self.new_game,8,2)
        
        grid_widget = QtGui.QWidget()
        self.setLayout(grid)

        # Event Handling
        
        self.close.clicked.connect(self.buttonClicked)
        self.change.clicked.connect(self.changeColour)
        self.change.clicked.connect(self.changePicture) 
        self.guess.clicked.connect(self.guess_response)
        self.new_game.clicked.connect(self.newgame)
        
    # function for closing window 
    
    def buttonClicked(self):                   
        sys.exit()
        
    # function for changing colour on the interface
    
    def changeColour(self):                     
        self.text = self.colour_combo.currentText()
        
        if self.text =='blue':
            self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            self.setAutoFillBackground(True) 
        else:
            self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            self.setAutoFillBackground(True)
            
    # function for changing picture on the interface
     
    def changePicture(self):
        self.text2 = self.picture_combo.currentText()
        
        if self.text2 == 'pluto':
            self.pic = QtGui.QPixmap('pluto.gif')      
            self.picture_label.setPixmap(self.pic) 
            
        else:
            self.pic = QtGui.QPixmap('mickey.gif')     
            self.picture_label.setPixmap(self.pic)      
            
            
            
     # function for changing colour on the interface       

    def guess_response(self):
        self.text_1 = self.edit_bar.displayText()
        
        if self.i == 1:                                 # this checks the first guess 
            if self.guess_num == int(self.text_1):
                self.guess_label1.setText(self.text_1)
                self.output1.setText('Correct!')
                self.edit_bar.clear()
                self.i+=2
                
            elif self.guess_num<int(self.text_1):
                self.guess_label1.setText(self.text_1)
                self.output1.setText('To big')
                self.edit_bar.clear()

            elif self.guess_num>int(self.text_1):
                self.guess_label1.setText(self.text_1)
                self.output1.setText('To small')
                self.edit_bar.clear()

                
            self.i+=1

             
        elif self.i == 2:                              # this checks the second guess
            self.text_2 = self.edit_bar.displayText()
            
            if self.guess_num == int(self.text_2):
                self.guess_label2.setText(self.text_2)
                self.output2.setText('Correct!')
                self.edit_bar.clear()
                self.i+=1
                
            elif self.guess_num<int(self.text_2):
                self.guess_label2.setText(self.text_2)
                self.output2.setText('To big')
                self.edit_bar.clear()
            
            elif self.guess_num>int(self.text_2):
                self.guess_label2.setText(self.text_2)
                self.output2.setText('To small')  
                self.edit_bar.clear()
                
            self.i +=1 
            

        elif self.i == 3:                              # this checks the third guess
            
            self.text_3 = self.edit_bar.displayText()
            
            if self.guess_num == int(self.text_3):
                self.guess_label3.setText(self.text_3)
                self.output3.setText('Correct!')
                self.edit_bar.clear()
                self.i-=3
                
            elif self.guess_num<int(self.text_3):
                self.guess_label3.setText(self.text_3)
                self.output3.setText('To big')
                self.edit_bar.clear()
                
            elif self.guess_num>int(self.text_3):
                self.guess_label3.setText(self.text_3)
                self.output3.setText('To small') 
                self.edit_bar.clear()
            self.i-=3
                
       
                
    # this clears all the labels and restarts the game      
    
    def newgame(self):
        self.guess_num = random.randint(1,10)
        self.i = 1
        self.edit_bar.clear()
        self.guess_label1.clear()
        self.guess_label2.clear()
        self.guess_label3.clear()
        
        self.output1.clear()
        self.output2.clear()
        self.output3.clear()        

 
    
def main():
    app = QtGui.QApplication(sys.argv)
    Guessing_Game = GuessingGame()
    Guessing_Game.show()
    
    sys.exit(app.exec_())
    
main()