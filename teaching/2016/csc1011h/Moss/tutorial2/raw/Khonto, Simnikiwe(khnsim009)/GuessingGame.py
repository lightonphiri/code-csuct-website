import sys
from PyQt4 import QtGui,QtCore
import random

class GridWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(250, 250, 200, 150)
        self.setWindowTitle('Guessing Game')
        
        guess_label = QtGui.QLabel('Guesses:',self)          #labels of the game
        guess_label.setFont(QtGui.QFont('Times',18))
        guess_no_label1 = QtGui.QLabel('Guess 1:',self)
        guess_no_label2 = QtGui.QLabel('Guess 2:',self)
        guess_no_label3 = QtGui.QLabel('Guess 3:',self)
        interface_label = QtGui.QLabel('Interface:',self)
        interface_label.setFont(QtGui.QFont('Times',18))
        self.picture_label = QtGui.QLabel('Picture:',self)
        self.colour_label = QtGui.QLabel('Colour:',self) 
        self.label1 = QtGui.QLabel('',self)
        self.label2 = QtGui.QLabel('',self)
        self.label3 = QtGui.QLabel('',self)
        self.label4 = QtGui.QLabel('',self)
        self.label5 = QtGui.QLabel('',self)
        self.label6 = QtGui.QLabel('',self)
        
        self.check = 0                                                  # count variable
        self.rand_guess = 1
        self.guess_edit = QtGui.QLineEdit(self)                         # button clicks
        self.guess_button = QtGui.QPushButton("Guess",self)
        self.guess_button.clicked.connect(self.guess)                      # connect button guess to guess function
        self.change_button = QtGui.QPushButton("Change",self)
        self.change_button.clicked.connect(self.changing)                  # connect change_button to changing function
        close_button = QtGui.QPushButton("Close",self)                    
        close_button.clicked.connect(self.close)                            # connect close_button to close function
        self.new_game_button = QtGui.QPushButton("New Game",self)
        self.new_game_button.clicked.connect(self.new_game)                # connect new_game_button to new_game function
        
        self.picture_combo = QtGui.QComboBox(self)                      # combo click for the picture
        self.picture_combo.addItem("pluto")                         # add picture to the combo
        self.picture_combo.addItem("mickey")
        self.picture_text = self.picture_combo.currentText()
        self.pixmap = QtGui.QPixmap("pluto.gif")
        self.pic_label = QtGui.QLabel(self)                           # constuctor
        self.pic_label.setPixmap(self.pixmap)                            # set the picture                   
        
        self.colour_combo = QtGui.QComboBox(self)                       # combo click for the changing the colour
        self.colour_combo.addItem("red")                            # add colour to combo
        self.colour_combo.addItem("blue")
        self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        
        grid = QtGui.QGridLayout()                             # construct the grid
        grid.addWidget(self.pic_label,0,0,8,1)
        grid.addWidget(guess_label,0,2)
        grid.addWidget(guess_no_label1,1,2)
        grid.addWidget(guess_no_label2,2,2)
        grid.addWidget(guess_no_label3,3,2)
        grid.addWidget(self.guess_edit,4,3)
        grid.addWidget(self.guess_button,4,4)
        grid.addWidget(interface_label,5,2)
        grid.addWidget(self.picture_label,6,2)        
        grid.addWidget(self.colour_label,7,2)
        grid.addWidget(self.picture_combo,6,3)
        grid.addWidget(self.colour_combo,7,3)
        grid.addWidget(self.change_button,7,4)
        grid.addWidget(close_button,8,2)
        grid.addWidget(self.new_game_button,8,3)
        grid.addWidget(self.label1,1,3)
        grid.addWidget(self.label2,2,3)
        grid.addWidget(self.label3,3,3)
        grid.addWidget(self.label4,1,4)
        grid.addWidget(self.label5,2,4)
        grid.addWidget(self.label6,3,4)
        self.setLayout(grid)                            # set the grid layout
    
    def close(self):                                   # constructor for close button 
        sys.exit()
        
    def guess(self,random):                                    # function for the guesses
        self.user_guess = self.guess_edit.displayText()
        if int(self.user_guess) > (self.rand_guess) and self.check ==0:
            self.label1.setText(self.user_guess)
            self.check += 1
            self.guess_edit.clear()
            self.label4.setText('To big')
    
        elif int(self.user_guess) > (self.rand_guess) and self.check ==1:
            self.label2.setText(self.user_guess)
            self.check += 1
            self.guess_edit.clear()
            self.label5.setText('To big')
            
        elif int(self.user_guess) >(self.rand_guess) and self.check ==2:
            self.label3.setText(self.user_guess)
            self.check += 1
            self.guess_edit.clear()
            self.label6.setText(str('To big'))
            
        if int(self.user_guess) <(self.rand_guess) and self.check ==0:
            self.label1.setText(self.user_guess)
            self.check += 1
            self.guess_edit.clear()
            self.label4.setText('To small')
            
        elif int(self.user_guess) < (self.rand_guess) and self.check ==1:
            self.label2.setText(self.user_guess)
            self.check += 1
            self.guess_edit.clear()
            self.label5.setText('To small')
            
        elif int(self.user_guess) < self.rand_guess and self.check ==2:
            self.label3.setText(self.user_guess)
            self.check += 1
            self.guess_edit.clear()
            self.label6.setText('To small') 
            
        if int(self.user_guess) == (self.rand_guess) and self.check ==0:
            self.label1.setText(self.user_guess)
            self.check += 2
            self.guess_edit.clear()
            self.label4.setText('Correct!')
            
        elif int(self.user_guess) == (self.rand_guess) and self.check ==1:
            self.label2.setText(self.user_guess)
            self.check += 3
            self.guess_edit.clear()
            self.label5.setText('Correct!')
            
        elif int(self.user_guess) == (self.rand_guess) and self.check ==2:
            self.label3.setText(self.user_guess)
            self.check += 4
            self.guess_edit.clear()
            self.label6.setText('Correct!') 
        elif self.check == 3:
            self.check == 1
            
    def changing(self):                                              # set colour
        self.colour_text = self.colour_combo.currentText()
        self.picture_text = self.picture_combo.currentText()        
        if self.colour_text == 'blue' and self.picture_text == 'mickey':
            self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            self.pixmap = QtGui.QPixmap("mickey.gif")
            self.pic_label.setPixmap(self.pixmap) 
            
        elif self.colour_text == 'red' and self.picture_text == 'mickey':
            self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            self.pixmap = QtGui.QPixmap("mickey.gif") 
            self.pic_label.setPixmap(self.pixmap)            
        
        elif self.picture_text == 'pluto' and self.colour_text == 'blue':
            self.pixmap = QtGui.QPixmap("pluto.gif")
            self.pic_label.setPixmap(self.pixmap)
            self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
        
        elif self.picture_text == 'pluto' and self.colour_text == 'red':
            self.pixmap = QtGui.QPixmap("pluto.gif")
            self.pic_label.setPixmap(self.pixmap)
            self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            
    def new_game(self):                                        #function to start a new game 
        self.label1.clear()
        self.label2.clear()
        self.label3.clear()
        self.check=0
        self.label4.clear()
        self.label5.clear()
        self.label6.clear()
        self.guess_edit.clear()  
        if self.check ==0:
            self.rand_guess = random.randint(1,10)          # generate random number for every new game  
            
            
def main(): 
    app = QtGui.QApplication(sys.argv)
    abs_widget = GridWidget()
    abs_widget.show()
    sys.exit(app.exec_())

main()