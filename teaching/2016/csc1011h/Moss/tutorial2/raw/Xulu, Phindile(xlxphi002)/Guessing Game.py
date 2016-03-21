# Program to create a GUI Based Guessing Game
# Phindile Xulu                 
#03/05/2016

import sys
from PyQt4 import QtGui,QtCore
import random


class MainWindow(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setWindowTitle("Guessing Game")
        self.setGeometry(300,300,300,300)
        
        
    #Creating widgets for guessing
        self.guesses_label=QtGui.QLabel("Guesses:")
        self.guesses_label.setFont(QtGui.QFont("Times",15,0))
        self.guesses_label.setMinimumSize(2,2)
        self.guess1=QtGui.QLabel("Guess 1:")
        self.guess2=QtGui.QLabel("Guess 2")
        self.guess3=QtGui.QLabel("Guess 3")               
        self.ans_1=QtGui.QLabel("")
        self.ans_2=QtGui.QLabel("")
        self.ans_3=QtGui.QLabel("")
        self.response1=QtGui.QLabel("")
        self.response2=QtGui.QLabel("")
        self.response3=QtGui.QLabel("")
        self.answer=(QtGui.QLineEdit(self))
        self.guess_button=QtGui.QPushButton("Guess")
        self.guess_button.clicked.connect(self.guess_clicked)
        self.a=1
        self.num_to_guess=1
        grid=QtGui.QGridLayout()
        
   #Adding guessing widgets to layout
        grid.addWidget(self.guesses_label,0,4) 
        grid.addWidget(self.guess1,1,4)
        grid.addWidget(self.guess2,2,4)
        grid.addWidget(self.guess3,3,4)
        grid.addWidget(self.ans_1,1,5)
        grid.addWidget(self.ans_2,2,5)
        grid.addWidget(self.ans_3,3,5)
        grid.addWidget(self.response1,1,6)
        grid.addWidget(self.response2,2,6)
        grid.addWidget(self.response3,3,6)       
        grid.addWidget(self.answer,4,5)
        grid.addWidget(self.guess_button,4,6)
        

        
        
    #Creating customisation widgets
        self.setPalette(QtGui.QPalette(QtGui.QColor("red")))
        self.interface_label=QtGui.QLabel("Interface:")
        self.interface_label.setFont(QtGui.QFont("Times",15,3))
        self.picture_label=QtGui.QLabel("Picture:")
        self.picture_combo=QtGui.QComboBox()
        self.picture_combo.addItem("mickey")
        self.picture_combo.addItem("pluto")
        
        self.colour_label=QtGui.QLabel("Colour")
        self.colour_combo=QtGui.QComboBox()
        self.colour_combo.addItem("red")
        self.colour_combo.addItem("blue")
        
       
        
        self.setPalette(QtGui.QPalette(QtGui.QColor("red")))       
        self.picture=QtGui.QPixmap("mickey.gif")
        self.label_picture=QtGui.QLabel()
        self.label_picture.setPixmap(self.picture)
        
        self.change=QtGui.QPushButton("Change")
        
        self.change.clicked.connect(self.change_interface)
        self.close=QtGui.QPushButton("Close")
        self.close.clicked.connect(self.exit)
        self.new_game=QtGui.QPushButton("New Game")
        self.new_game.clicked.connect(self.restart)
        
        #Adding customisation widgets to the layout
        
        grid.addWidget(self.label_picture,0,0,8,3)
        grid.addWidget(self.interface_label,5,4)
        grid.addWidget(self.picture_label,6,4)
        grid.addWidget(self.picture_combo,6,5)
        grid.addWidget(self.colour_label,7,4)
        grid.addWidget(self.colour_combo,7,5)
        grid.addWidget(self.change,7,6)
        grid.addWidget(self.close,8,4)
        grid.addWidget(self.new_game,8,5)
        self.setLayout(grid)  
                

   
    
    def guess_clicked(self):                    #button that responds if the guess button is clicked and compares the random number to the one the user enter
        
        self.user_ans=self.answer.displayText()     # Get text from the textBox
        
        if int(self.user_ans)>(self.num_to_guess) and self.a ==1:
            self.ans_1.setText(self.user_ans)
            self.response1.setText("To big")
            self.answer.clear()
            self.a+=1                       #tracks the number of guesses the user has inputed
            
        elif int(self.user_ans)>self.num_to_guess and self.a==2:
            self.ans_2.setText(self.user_ans)
            self.response2.setText("To big")
            self.answer.clear()
            self.a+=1            
               
        elif int(self.user_ans)>(self.num_to_guess) and self.a==3:
            self.ans_3.setText(self.user_ans)
            self.response3.setText("To big")
            self.answer.clear()
            self.a+=1
        if  int(self.user_ans)<(self.num_to_guess) and self.a == 1:
            
            self.ans_1.setText(self.user_ans)
            self.response1.setText("To small")
            self.answer.clear() 
            self.a+=1
      
        elif  int(self.user_ans)<self.num_to_guess and self.a==2:
            self.ans_2.setText(self.user_ans)
            self.response2.setText("To small")
            self.answer.clear()
            self.a+=1
        elif  int(self.user_ans)<(self.num_to_guess) and self.a ==3:
            self.ans_3.setText(self.user_ans)
            self.response3.setText("To small") 
            self.answer.clear()
            self.a+=1
                              
        if int(self.user_ans)==self.num_to_guess and self.a==1:
            self.ans_1.setText(self.user_ans)
            self.response1.setText("Correct!")
            self.a=4
            self.answer.clear()
            

        elif int(self.user_ans)==self.num_to_guess and self.a==2:
            self.ans_2.setText(self.user_ans)
            self.response2.setText("Correct!") 
            self.answer.clear()
            self.a=4
           
     
            
       
        elif int(self.user_ans)==self.num_to_guess and self.a==3:
            self.ans_3.setText(self.user_ans)
            self.response3.setText("Correct!")
            self.answer.clear()
            self.a=4
            
        elif self.a==4:             #When the user has had three tries or got the answer correct. it prevents extra tries
            self.a=1
                                 
    
    def change_interface(self):         #Changes colour and text of the game based on what the user has selected
        self.colour=self.colour_combo.currentText()
        self.picture_name=self.picture_combo.currentText()
        if self.picture_name=="mickey":
            self.picture=QtGui.QPixmap("mickey.gif")
            self.label_picture.setPixmap(self.picture)
            if self.colour=="red":
                self.setPalette(QtGui.QPalette(QtGui.QColor("red")))
            elif self.colour=="blue":
                self.setPalette(QtGui.QPalette(QtGui.QColor("blue")))
        
            
        
        elif self.picture_name=="pluto":
            self.picture=QtGui.QPixmap("pluto.gif")
            self.label_picture.setPixmap(self.picture)
            if self.colour=="red":
                self.setPalette(QtGui.QPalette(QtGui.QColor("red")))
            elif self.colour=="blue":
                self.setPalette(QtGui.QPalette(QtGui.QColor("blue"))) 
                
    def restart(self):                  #Creates a new game with a new random number
        self.ans_1.clear()
        self.ans_2.clear()
        self.ans_3.clear()
        self.response1.clear()
        self.response2.clear()
        self.response3.clear()
        self.a=1
        
        if self.a==1:
            self.num_to_guess=random.randint(1,11)
            
    def exit(self):
        sys.exit()
    
def main():
    app=QtGui.QApplication(sys.argv)
    widgets=MainWindow()
    widgets.show()
    sys.exit(app.exec())
   
           
    
    
main()