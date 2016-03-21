# Dikgang Thapelo
# Guessing Game
# 06 March 2016

# Importing necessary modules
import sys
import random
from PyQt4 import QtGui, QtCore

# Creating a class named MainWidget
class MainWidget(QtGui.QWidget):
    SecretNumber=random.randint(1,10) # Computing the number the player has to guess
    count=1  # the variable will be Incremented for each guess, and stops on the last guess which is 3 
    
    def __init__(self, parent=None):  	
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(250, 250, 300, 300)
        self.setWindowTitle('Guessing Game')
        
        #Creating Labels
        self.guess_label = QtGui.QLabel('Guesses:',self)
        self.guess_label.setFont(QtGui.QFont('Arial',20,0))   
         
        self.editbox = QtGui.QLineEdit()		
        self.guessbutton = QtGui.QPushButton("Guess")
        
        self.interface_label = QtGui.QLabel('Interface:',self)
        self.interface_label.setFont(QtGui.QFont('Arial',20,0))
        
        self.picture_label = QtGui.QLabel('Picture:')
        self.colour_label = QtGui.QLabel('Colour:') 
        
        self.changebutton = QtGui.QPushButton("Change")
                
        self.closebutton = QtGui.QPushButton("Close")
        self.newbutton = QtGui.QPushButton("New Game")         
        
        # Creating two combo box,one for colours and the other one for pictures
        self.picture_combo = QtGui.QComboBox()
        self.picture_combo.addItem('mickey') 
        self.picture_combo.addItem('pluto')
        self.colour_combo = QtGui.QComboBox()
        self.colour_combo.addItem('Red')
        self.colour_combo.addItem('Blue')
        
        # Creating a default picture label
        self.pictureText = self.picture_combo.currentText()     
        picture = QtGui.QPixmap(self.pictureText+'.gif') 
        self.pic_label = QtGui.QLabel() 
        self.pic_label.setPixmap(picture)         
                
        # Creating a grid layout      
        self.grid = QtGui.QGridLayout()
        
        # Adding the widgets to the grid layout
        self.grid.addWidget(self.guess_label,0,3)  
        
        self.grid.addWidget(self.editbox,4,4)
        self.grid.addWidget(self.guessbutton,4,5)
        
        self.grid.addWidget(self.interface_label,5,3)       
        self.grid.addWidget(self.picture_label,6,3)      
        self.grid.addWidget(self.colour_label,7,3)
        
        self.grid.addWidget(self.picture_combo,6,4)
        self.grid.addWidget(self.colour_combo,7,4)
        
        self.grid.addWidget(self.changebutton,7,5)
        
        self.grid.addWidget(self.closebutton,8,3)
        self.grid.addWidget(self.newbutton,8,4)           
          
        self.grid.addWidget(self.pic_label,0,0,10,3)         
        
        # Creating a default window background colour
        self.textcolour = self.colour_combo.currentText()       
        self.setPalette(QtGui.QPalette(QtGui.QColor(self.textcolour)))
        self.setAutoFillBackground(True)        
       
        # Adding the grid layout to the window
        self.setLayout(self.grid)
        
        # Event handling, connect signals to their slots
        self.connect(self.closebutton,QtCore.SIGNAL('clicked()'), self.closewindow)
        self.connect(self.changebutton,QtCore.SIGNAL('clicked()'),self.changewindow)
        self.connect(self.guessbutton,QtCore.SIGNAL('clicked()'),self.guess_result)
        self.connect(self.newbutton,QtCore.SIGNAL('clicked()'),self.restart)
       
    def restart(self):
        # Restarting the game
        self.guess.close()
        self.guesshint.close()
        self.guessAnswer.close()
        
              
    def closewindow(self):
        #Closing the window
        self.close()
        
    def changewindow(self):
        # Changing the background colour and the picture on the window
        self.textcolour = self.colour_combo.currentText()       
        self.setPalette(QtGui.QPalette(QtGui.QColor(self.textcolour)))
        self.setAutoFillBackground(True)
                
        self.pic_label.hide()       
        self.pictureText = self.picture_combo.currentText()     
        picture = QtGui.QPixmap(self.pictureText+'.gif') 
        self.pic_label = QtGui.QLabel() 
        self.pic_label.setPixmap(picture)   
        self.grid.addWidget(self.pic_label,0,0,10,3)      
        
    def guess_result(self):                                                 
        # Manipulating the users guesses and returning the appropriate response  
        
        if MainWidget.count < 4 : 
            self.guess = QtGui.QLabel('Guess '+str(MainWidget.count)+':')           
            
            self.inputNumber=str(self.editbox.displayText())
            self.guessAnswer = QtGui.QLabel(self.inputNumber)
            
            self.grid.addWidget(self.guess,MainWidget.count,3)
            self.grid.addWidget(self.guessAnswer,MainWidget.count ,4)
            
            if self.inputNumber!=str(MainWidget.SecretNumber):
                if int(self.inputNumber) < MainWidget.SecretNumber:
                    self.guesshint = QtGui.QLabel('to small')
                else:
                    self.guesshint = QtGui.QLabel('to big')
                self.grid.addWidget(self.guesshint,MainWidget.count ,5)
            else:
                self.guesshint = QtGui.QLabel('correct')
                self.grid.addWidget(self.guesshint,MainWidget.count ,5)                
                MainWidget.count=4              
            self.editbox.clear()
            MainWidget.count+=1 

        
# Defining and calling the Mainwiget Class                                                     
def main():
    app = QtGui.QApplication(sys.argv)
    my_widget = MainWidget()		
    my_widget.show()
    sys.exit(app.exec_())
main()
