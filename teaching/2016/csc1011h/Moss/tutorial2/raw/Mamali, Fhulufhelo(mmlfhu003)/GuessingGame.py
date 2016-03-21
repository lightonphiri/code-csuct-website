import sys 
from PyQt4 import QtGui
app=QtGui.QApplication(sys.argv)
import random
guess=random.randint(0,10) # Taking random numbers from 0 to 10
class Game(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.picture_name="mickey.gif"
        self.setMaximumSize(500,300) # Possible maximum window
        label1=QtGui.QLabel('Guess 1:',self)
        label1.move(239,45)         
        self.setWindowTitle("Guessing Game") # Tittle of the window
        self.pic1=QtGui.QPixmap(self.picture_name) # The initial background picture
        self.piclabel=QtGui.QLabel(self)
        self.piclabel.setPixmap(QtGui.QPixmap(self.pic1))
        self.piclabel.move(0,40)
        self.setPalette(QtGui.QPalette(QtGui.QColor('red'))) # The initial background color
        self.setAutoFillBackground(True )  
        push1=QtGui.QPushButton("Change",self) # creating button for changing color and picture
        push1.setGeometry(400,215,75,25)
        new_game_button=QtGui.QPushButton("New Game",self) # Button to start new game
        new_game_button.setGeometry(320,250,75,25) # possetioning the button  
        quit_button=QtGui.QPushButton("Close",self) # closing button
        quit_button.setGeometry(240,250,75,25)
        game_button=QtGui.QPushButton("Guess",self) # Guessing button
        game_button.setGeometry(400,115,75,25)        
        self.edit1=QtGui.QLineEdit(self)
        self.edit1.setGeometry(320,115,75,22) 
        self.counterombo1=QtGui.QComboBox(self)
        self.counterombo1.addItem("red")
        self.counterombo1.addItem("blue")
        self.counterombo1.setGeometry(320,215,75,22)        
        self.counterombo2=QtGui.QComboBox(self)
        self.counterombo2.addItem("mickey")
        self.counterombo2.addItem("pluto")
        self.counterombo2.setGeometry(320,185,75,22)
        label=QtGui.QLabel('Guesses:',self)
        label.setFont(QtGui.QFont('Arial',15))                                                      
        label.move(240,10)
        label=QtGui.QLabel('Interface:',self)
        label.setFont(QtGui.QFont('Arial',15))
        label.move(240,150)
        label_picture=QtGui.QLabel('Picture:',self)
        label_picture.move(240,185)
        label_color=QtGui.QLabel('Colour:',self)
        label_color.move(240,215)        
        quit_button.clicked.connect(self.quit) # connecting the quit button to the quit method
        push1.clicked.connect(self.pic_color) # connecting the push1 button to the pic(picture) method
        game_button.clicked.connect(self.game) # Connecting the game button to the main game 
        new_game_button.clicked.connect(self.new) # connecting the new game button to the resert method
        self.label2=QtGui.QLabel(" ",self) # null (empty) field 1
        self.label2.setGeometry(240,37,300,30)
        self.label3=QtGui.QLabel(" ",self) # null (empty) field 2
        self.label3.setGeometry(240,60,300,30) 
        self.label4=QtGui.QLabel(" ",self) # null (empty) field 3
        self.label4.setGeometry(240,87,300,30)   
        self.counter=0 # Trials counter

        
        label1=QtGui.QLabel('Guess 2:',self)
        label1.move(239,65)  
        label1=QtGui.QLabel('Guess 3:',self)
        label1.move(239,95)              
    # Method to close the game
    def quit(self):
        sys.exit() 
    # method which smultenously changes the background picture and color if selelcted 
    def pic_color(self):
        self.pic_selection=self.counterombo2.currentText() # Taking the name of the selected picture
        self.pic_selection=self.counterombo2.currentText() 
        self.color_name=self.counterombo1.currentText()
        self.color_name=self.counterombo1.currentText()
        if self.pic_selection=="mickey" and self.color_name=="blue": # Blue and Mickey condition
            self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            self.setAutoFillBackground(True )            
            self.pic1=QtGui.QPixmap(self.pic_selection)
            self.piclabel.setPixmap(self.pic1)
            self.piclabel.move(0,40) # seting the picture to the initial position
            self.piclabel.show()
        elif self.pic_selection=="mickey" and self.color_name=="red": # mickey and red condition
            self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            self.setAutoFillBackground(True )            
            self.pic1=QtGui.QPixmap(self.pic_selection)
            self.piclabel.setPixmap(self.pic1)
            self.piclabel.move(0,40) # seting the picture to the initial position
            self.piclabel.show()        
        elif self.pic_selection=="pluto" and self.color_name=="red":
            self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            self.setAutoFillBackground(True )             
            self.pic1=QtGui.QPixmap(self.pic_selection)
            self.piclabel.setPixmap(self.pic1)
            piclabel=QtGui.QLabel(self)
            piclabel.move(0,40) # seting the picture to the initial position  
            piclabel.show() 
        elif self.pic_selection=="pluto" and self.color_name=="blue": # Pluto and blue condition
            self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            self.setAutoFillBackground(True )             
            self.pic1=QtGui.QPixmap(self.pic_selection)
            self.piclabel.setPixmap(self.pic1)
            piclabel=QtGui.QLabel(self)
            piclabel.move(0,40) # seting the picture to the initial position
            #piclabel.setPixmap(self.pic1)  
            piclabel.show()
          
    def game(self):
       
        entered_guess=self.edit1.displayText() 
        # by using "self.edit1.clear()" im clearing the current text from the edit box
        if self.counter<=2: # As long as if counter is still less or equal to 2 GET  IN 
            if entered_guess==str(guess) and  self.counter==0: # if the guess is Correct and counter is 0 Lebel to the FIELD NUMBER 1( whic is an empty field)
                labeler="{0:<26} {1:<26}{2}".format("        ",entered_guess,"Correct")
                self.label2.setText(labeler)
                self.edit1.clear()
            elif entered_guess==str(guess) and  self.counter==1:  # if the guess is Correct and counter is 1 Lebel to the FIELD NUMBER 2( whic is an empty field)
                
                labeler="{0:<26} {1:<26}{2}".format("        ",entered_guess,"Correct")
                self.label3.setText(labeler)
                self.edit1.clear()          
            elif entered_guess==str(guess) and  self.counter==2:  # if the guess is Correct and counter is 2 Lebel to the FIELD NUMBER 3( whic is an empty field)
                labeler="{0:<26} {1:<26}{2}".format("        ",entered_guess,"Correct")
                self.label4.setText(labeler)
                self.edit1.clear()                    
               
            elif eval(entered_guess)>guess and self.counter==0:  # if the guess is Too High and counter is 0 Lebel to the FIELD NUMBER 1( whic is an empty field)
                labeler="{0:<26} {1:<26}{2}".format("        ",entered_guess,"Too high")
                self.label2.setText(labeler)
                self.edit1.clear()
                self.counter+=1
            elif eval(entered_guess)>guess and self.counter==1: # if the guess is Too High and counter is 2 Lebel to the FIELD NUMBER 2( whic is an empty field)
                    labeler="{0:<26} {1:<26}{2}".format("        ",entered_guess,"Too high")
                    self.label3.setText(labeler)
                    self.edit1.clear()
                    self.counter+=1
            elif eval(entered_guess)>guess and self.counter==2: # if the guess is Too High and counter is 3 Lebel to the FIELD NUMBER 3( whic is an empty field)
                labeler="{0:<26} {1:<26}{2}".format("        ",entered_guess,"Too high")
                self.label4.setText(labeler)
                self.edit1.clear()
                self.counter+=1            
            elif eval(entered_guess)<guess and self.counter==0: # if the guess is Too Small and counter is 0 Lebel to the FIELD NUMBER 1( whic is an empty field)
                labeler="{0:<26} {1:<26}{2}".format("        ",entered_guess,"Too Small")
                self.label2.setText(labeler)
                self.edit1.clear()
                self.counter+=1            
        
            elif eval(entered_guess)<guess and self.counter==1: # if the guess is Too Small and counter is 1 Lebel to the FIELD NUMBER 2( whic is an empty field)
                labeler="{0:<26} {1:<26}{2}".format("        ",entered_guess,"Too Small")
                self.label3.setText(labeler)
                self.edit1.clear()
                self.counter+=1          
            elif eval(entered_guess)<guess and self.counter==2: # if the guess is Too Small and counter is 2 Lebel to the FIELD NUMBER 3( whic is an empty field)
                labeler="{0:<26} {1:<26}{2}".format("        ",entered_guess,"Too Small")
                self.label4.setText(labeler)
                self.edit1.clear()
                self.counter+=1                 
    def new(self):
        # Clearing the text from label 1,2,3 if this function is called
        self.label2.clear()
        self.label3.clear()
        self.label4.clear()
        self.counter=0

def main():     
    game=Game()    
    game.show()
    sys.exit(app.exec_())
main()