# Tut 2 - MPHFAR001
#CSC1011H 

import sys , random
from PyQt4 import QtGui , QtCore 
#from QStyle import QStyleFactory
import subprocess

class Game_window(QtGui.QWidget) :
    def __init__(self, parent = None ) :
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(400,150,500,400)
        self.setWindowTitle("Guessing Game")
        self.grid = QtGui.QGridLayout()
        
    def main_inter(self) : # this is the main interface ,just key components
        guess_label = QtGui.QLabel("Guesses :",self)
        self.grid.addWidget(guess_label,0,9)
        
        guess_label.setFont(QtGui.QFont("Times",18))
        interface = QtGui.QLabel("Interface :",self)
        self.grid.addWidget(interface,5,9)
        interface.setFont(QtGui.QFont("Times",18))
        
        self.close_button = QtGui.QPushButton("Close",self)
        self.close_button.clicked.connect(self.close)

        self.grid.addWidget(self.close_button,8,9)
        
        self.restart = QtGui.QPushButton("New Game",self)
        self.grid.addWidget(self.restart,8,10)
        
        self.restart.clicked.connect(self.restartApp)
       
        
        self.rand_num = random.randint(1,10)
    # Uncomment the following to view the random number in a separate shell
        print("The random number is {}".format(self.rand_num))        

        self.count = 0
        
    def close(self) :
        sys.exit()
    def restartApp(self):
       
        subprocess.call("python" + " GuessingGame.py", shell=True)        
        self.close()
    def interface(self) : # This is the interface of the Game 
        imgBoxLabel = QtGui.QLabel("Picture :",self)
        self.grid.addWidget(imgBoxLabel,7,9)
        
        self.img_box = QtGui.QComboBox(self)
        self.img_box.addItem("Mickey")
        self.img_box.addItem("Pluto")
        self.grid.addWidget(self.img_box,7,10)
              
        
        self.colour_box = QtGui.QComboBox(self)
        self.colour_box.addItem("Red")
        self.colour_box.addItem("Blue")
        self.colour_box.addItem("Pink")
        self.colour_box.addItem("Gold")
        self.colour_box.addItem("Brown")
        self.colour_label = QtGui.QLabel("Colour",self)
        self.grid.addWidget(self.colour_label,6,9)
        self.grid.addWidget(self.colour_box,6,10)
        
        setButton = QtGui.QPushButton("Change")
        
        self.grid.addWidget(setButton,7,11)
        setButton.clicked.connect(self.set_interface)
        self.image_text = self.img_box.currentText()
        self.img = QtGui.QPixmap(self.image_text+".gif") #full picture name
        self.img_label = QtGui.QLabel(self)
        self.img_label.setPixmap(self.img)
        self.grid.addWidget(self.img_label,0,0,8,9)
        
   
    def set_interface(self) : #sets the interface when change button is clicked 
        
        #setting the image
        
        self.image_text = self.img_box.currentText()
        self.img = QtGui.QPixmap(self.image_text+".gif")
       
        self.img_label.setPixmap(self.img)
        self.img_label.update() # update the image based on the current text in combo box
        self.grid.addWidget(self.img_label,0,0,8,9)
        
        #setting the colour 
        self.text = self.colour_box.currentText()
        self.setPalette(QtGui.QPalette(QtGui.QColor(self.text)))   
        self.setAutoFillBackground(True)
    
    def game_inter(self) :  # Game Interface
        guess_button = QtGui.QPushButton("Guess")
        self.grid.addWidget(guess_button,4,11)
        
        guess1 = QtGui.QLabel("Guess 1 :",self)
        self.grid.addWidget(guess1,1,9)
        guess2 = QtGui.QLabel("Guess 2 :",self)
        self.grid.addWidget(guess2,2,9)
        guess3 = QtGui.QLabel("Guess 3 :",self)
        self.grid.addWidget(guess3,3,9)
       
        self.tries = QtGui.QLineEdit("",self) # Input from the user 
        self.grid.addWidget(self.tries,4,10)
       
        guess_button.clicked.connect(self.gbclicked) # starts the game once guess button clicked 
        
    def gbclicked(self) :    
        self.guess = self.tries.text() # gets the text the user inputs in the tries line edit 
        
        # THE FOLLOWING IS AN EQUIVALENT TO A FOR LOOP RUNNING 3 TIMES
        
        if self.count == 0 :
            u_input = self.guess
            input_label = QtGui.QLabel(u_input)
            self.grid.addWidget(input_label ,self.count+1, 10)
            
            
            if int(u_input) == self.rand_num :
                output = QtGui.QLabel("Correct")
                self.grid.addWidget(output,self.count+1,11) # ADD TO REQUIRED GRID POSITION BASED ON THE INDEX / count 
                #print(output)   
                self.count+=1 
            if int(u_input) > self.rand_num : 
                output = QtGui.QLabel("Too Big")
                self.grid.addWidget(output,self.count+1,11) 
                self.count+=1
            if int(u_input) < self.rand_num :
                output = QtGui.QLabel("Too Small")
                self.grid.addWidget(output,self.count+1,11)             
                self.count+=1
                           
        elif self.count == 1 :
            u_input = self.guess
            input_label = QtGui.QLabel(u_input)
            self.grid.addWidget(input_label ,self.count+1, 10)
            
            if int(u_input) == self.rand_num :
                output = QtGui.QLabel("Correct")
                self.grid.addWidget(output,self.count+1,11)
                #print(output)   
                self.count+=1
            if int(u_input) > self.rand_num : 
                output = QtGui.QLabel("Too Big")
                self.grid.addWidget(output,self.count+1,11) 
                self.count+=1
            if int(u_input) < self.rand_num :
                output = QtGui.QLabel("Too Small")
                self.grid.addWidget(output,self.count+1,11)             
                self.count+=1        
        elif self.count == 2 :
            u_input = self.guess
            input_label = QtGui.QLabel(u_input)
            self.grid.addWidget(input_label ,self.count+1, 10)
            
            if int(u_input) == self.rand_num :
                output = QtGui.QLabel("Correct")
                self.grid.addWidget(output,self.count+1,11)
                #print(output)   
                self.count+=1
            if int(u_input) > self.rand_num : 
                output = QtGui.QLabel("Too Big")
                self.grid.addWidget(output,self.count+1,11) 
                self.count+=1
            if int(u_input) < self.rand_num :
                output = QtGui.QLabel("Too Small")
                self.grid.addWidget(output,self.count+1,11)             
                self.count+=1       
                         
def main() :
    
    guess= QtGui.QApplication(sys.argv)
    guess.setFont(QtGui.QFont("Arial",10))
    my_game = Game_window()
    my_game.main_inter()
    my_game.interface()
    my_game.game_inter()
  
    game_grid = my_game.grid # main game grid
    my_game.setLayout(game_grid)    
    my_game.show() # display grid after all variables are set 
    
    sys.exit(guess.exec_())
    
main() 