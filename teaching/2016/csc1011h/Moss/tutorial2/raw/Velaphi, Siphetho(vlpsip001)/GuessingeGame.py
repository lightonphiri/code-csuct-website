import sys
from PyQt4 import QtGui,QtCore
from random import*

class GuessingGame(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(250,250,400,300)
        self.setWindowTitle("Guessing Game")
        
        self.pixmap= QtGui.QPixmap('mickey.gif')
        self.pic_label= QtGui.QLabel()
        self.pic_label.setPixmap(self.pixmap)        
        
        self.label= QtGui.QLabel()
        self.setPalette(QtGui.QPalette(QtGui.QColor("red")))
        
        gausses_label= QtGui.QLabel("Guesses:",self)
        gausses_label.setFont(QtGui.QFont('Arial',14,10))
        
        self.gausse1_label= QtGui.QLabel("Guess 1:")
        self.gausse2_label= QtGui.QLabel("Guess 2:")
        self.gausse3_label= QtGui.QLabel("Guess 3:")
        
        self.gauss_text1= QtGui.QLabel() 
        self.gauss_text2= QtGui.QLabel() 
        self.gauss_text3= QtGui.QLabel() 
        self.comment1= QtGui.QLabel()
        self.comment2= QtGui.QLabel()
        self.comment3= QtGui.QLabel()
        
        self.edit= QtGui.QLineEdit(self)
        self.x=self.edit.displayText()
        self.gausse_button= QtGui.QPushButton("Guess")
        self.gausse_button.clicked.connect(self.guess)
        
        self.grid= QtGui.QGridLayout()
        self.grid.addWidget(gausses_label,0,0)
        self.grid.addWidget(self.gausse1_label,1,0)
        self.grid.addWidget(self.gauss_text1,1,1)
        self.grid.addWidget(self.comment1,1,3)
        self.grid.addWidget(self.gausse2_label,2,0)
        self.grid.addWidget(self.gauss_text2,2,1)
        self.grid.addWidget(self.comment2,2,3)
        self.grid.addWidget(self.gausse3_label,3,0)
        self.grid.addWidget(self.gauss_text3,3,1)
        self.grid.addWidget(self.comment3,3,3)
        self.grid.addWidget(self.edit,4,2)
        self.grid.addWidget(self.gausse_button,4,3)
        grid_widget= QtGui.QWidget()
        grid_widget.setLayout(self.grid)
        
        interface_label= QtGui.QLabel("Interface:",self)
        interface_label.setFont(QtGui.QFont('Arial',14,10))
        
        self.picture_label = QtGui.QLabel("Picture:")
        self.colour_label= QtGui.QLabel("clour:")
        self.picture_combo= QtGui.QComboBox(self)
        self.picture_combo.addItem("Mickey")
        self.picture_combo.addItem("Pluto")
        self.colour_combo = QtGui.QComboBox()
        self.colour_combo.addItem("Red")
        self.colour_combo.addItem("Blue")
        self.change_Button= QtGui.QPushButton("Change")
        self.change_Button.clicked.connect(self.change_pic)
        self.change_Button.clicked.connect(self.change_colour)
        self.close_button= QtGui.QPushButton("Close")
        self.close_button.clicked.connect(self.buttonClicked)
        self.new_game_button= QtGui.QPushButton("New Game")
        self.new_game_button.clicked.connect(self.new_game)
        
        grid2= QtGui.QGridLayout() 
        grid2.addWidget(interface_label,0,0)
        grid2.addWidget(self.picture_label,1,0)
        grid2.addWidget(self.picture_combo,1,1)
        grid2.addWidget(self.colour_label,2,0)
        grid2.addWidget(self.colour_combo,2,1)
        grid2.addWidget(self.change_Button,2,2)
        grid2.addWidget(self.close_button,3,0)
        grid2.addWidget(self.new_game_button,3,1)
        grid2_widget= QtGui.QWidget()
        grid2_widget.setLayout(grid2)
        
        vbox2= QtGui.QVBoxLayout()
        vbox2.addWidget(grid_widget)
        vbox2.addWidget(grid2_widget)
        self.vbox2_widget= QtGui.QWidget()
        self.vbox2_widget.setLayout(vbox2)
        
        hbox3= QtGui.QHBoxLayout()
        hbox3.addWidget(self.pic_label)
        hbox3.addWidget(self.vbox2_widget)
        self.setLayout(hbox3)
        self.counter=3
        self.rand_number= randint(0,3)
        
    def change_pic(self):
        self.picture= self.picture_combo.currentText()
        if self.picture=="Pluto":
            self.pixmap= QtGui.QPixmap('pluto.gif')
            self.pic_label.setPixmap(self.pixmap) 
        else:
            self.pixmap= QtGui.QPixmap('mickey.gif')
            self.pic_label.setPixmap(self.pixmap) 
    def change_colour(self):
        self.label= self.colour_combo.currentText()
        if self.label=="Blue":
            self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
        else:
            self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
    def buttonClicked(self):
        self.close()
    
    def guess(self):
        guess=self.rand_number
        user_guess= self.edit.displayText()
        self.edit.clear()
        if int(user_guess)==guess:
            if self.counter==3:
                self.gauss_text1.setText(user_guess)
                self.comment1.setText("Correct!")
                self.counter-=3
                if self.counter==0:
                    self.edit.setText("WON")
            elif self.counter==2:
                self.gauss_text2.setText(user_guess)
                self.comment2.setText("Correct!")
                self.counter-=2
                if self.counter==0:
                    self.edit.setText("WON")
            elif self.counter==1:
                self.gauss_text3.setText(user_guess)
                self.comment3.setText("Correct!")
                self.counter-=1
                if self.counter==0:
                    self.edit.setText("WON")                           
        elif int(user_guess)>guess:
            if self.counter==3:
                self.gauss_text1.setText(user_guess)
                self.comment1.setText("To big")
                self.counter-=1
                if self.counter==0:
                    self.edit.setText("LOST")                
                print(self.counter)
            elif self.counter==2:
                self.gauss_text2.setText(user_guess)
                self.comment2.setText("To big")
                self.counter-=1
                if self.counter==0:
                    self.edit.setText("LOST")                
            elif self.counter==1:
                self.gauss_text3.setText(user_guess)   
                self.comment3.setText("To big")
                self.counter-=1
                if self.counter==0:
                    self.edit.setText("LOST")                               
        elif int(user_guess)<guess:
            if self.counter==3:
                self.gauss_text1.setText(user_guess)
                self.comment1.setText("To small")
                self.counter-=1
                if self.counter==0:
                    self.edit.setText("LOST")                
            elif self.counter==2:
                self.gauss_text2.setText(user_guess)
                self.comment2.setText("To small")
                self.counter-=1
                if self.counter==0:
                    self.edit.setText("LOST")                
            elif self.counter==1:
                self.gauss_text3.setText(user_guess)
                self.comment3.setText("To small")
                self.counter-=1
                if self.counter==0:
                    self.edit.setText("LOST")  
                    
    def new_game(self):
        self.edit.clear()
        self.comment1.clear()
        self.comment2.clear()
        self.comment3.clear()
        self.gauss_text1.clear()
        self.gauss_text2.clear()
        self.gauss_text3.clear()
        self.counter=3
        self.rand_number= randint(0,3)
                
def main():
    app = QtGui.QApplication(sys.argv)
    widget= GuessingGame()
    widget.show()
    sys.exit(app.exec_())
main()