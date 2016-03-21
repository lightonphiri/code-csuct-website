import sys
from PyQt4 import QtGui,QtCore
import random

class GuessingGame(QtGui.QWidget):
    
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(250,250,250,250) # this is my default window size
        self.setWindowTitle("Guessing Game") # this is my window title
        self.secret_number = random.randint(1,10)
        self.label = QtGui.QLabel()
        self.label.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        self.label.setAutoFillBackground(True)        
        
        
        self.pixmap = QtGui.QPixmap('mickey.gif') # allows us to take the picture from the directory
        self.pic_label = QtGui.QLabel()
        self.pic_label.setPixmap(self.pixmap) # place the picture to where we want it to be
        
        title_1 = QtGui.QLabel("Guesses:")      # title name  for guesses
        title_1.setFont(QtGui.QFont('Times',20)) # set the size for the name
        
        self.label_guess1 = QtGui.QLabel("guess 1:")  # displayed word to the user
        self.label_guess2 = QtGui.QLabel("") # this act as a place holder waiting for the user to enter something so that it pops as guess 2
        self.label_guess3 = QtGui.QLabel("")  # this act as a place holder waiting for the user to enter something so that it pops as guess 3
        self.edit = QtGui.QLineEdit()  # this is the slot where the user is going to  enter the entries
        self.label1 = QtGui.QLabel("") # this act as a place holder waiting for the user to enter something so that it pops
        self.label2 = QtGui.QLabel("")  # # this act as a place holder waiting for the user to enter something so that it pops
        
        self.label3 = QtGui.QLabel("")
        self.response1 = QtGui.QLabel("") # this is a holder for the response to display to the user
        self.response2 = QtGui.QLabel("")
        self.response3 = QtGui.QLabel("")
        self.grid = QtGui.QGridLayout()     # creating a layout on how our widgets should placed n stuctured
        self.grid.addWidget(title_1,0,0)
        self.grid.addWidget(self.label_guess1,1,0)
        self.grid.addWidget(self.label_guess2,2,0)
        self.grid.addWidget(self.label_guess3,3,0)
        self.grid.addWidget(self.label1,1,1)
        self.grid.addWidget(self.label2,2,1)
        self.grid.addWidget(self.edit,4,2)
        self.grid.addWidget(self.label3,3,1)
        self.grid.addWidget(self.response1,1,3)
        self.grid.addWidget(self.response2,2,3)
        self.grid.addWidget(self.response3,3,3)
        
        self.guess_button =  QtGui.QPushButton("guess")   # creating a guess button
        self.grid.addWidget(self.guess_button,4,3)     # positioning the guess button
        self.calling_grid = QtGui.QWidget()
        self.calling_grid.setLayout(self.grid)
        
        self.connect(self.guess_button,QtCore.SIGNAL('clicked()'), self.connect_button)      # connecting the guess button to the connect_button function  
        self.a=0                  # initialising the counter variable to track the guesses
        
        
        self.title_2 = QtGui.QLabel("Interface:")
        self.title_2.setFont(QtGui.QFont('Times',20))
        self.picture = QtGui.QLabel("Picture:")
        self.colour = QtGui.QLabel("colour:")
        self.close_button = QtGui.QPushButton("close")
        self.new_game_button = QtGui.QPushButton("New Game")
        self.combo_picture = QtGui.QComboBox()
        self.combo_picture.addItem('mickey')
        self.combo_picture.addItem('pluto')
        self.combo_colour = QtGui.QComboBox()
        self.combo_colour.addItem('red')
        self.combo_colour.addItem('blue')
        self.change_button = QtGui.QPushButton("Change")
        self.grid_2 = QtGui.QGridLayout()
        
        
        self.grid_2.addWidget(self.title_2,0,0)
        self.grid_2.addWidget(self.picture,1,0)
        self.grid_2.addWidget(self.colour,2,0)
        self.grid_2.addWidget(self.close_button,3,0)
        self.grid_2.addWidget(self.new_game_button,3,1)
        self.grid_2.addWidget(self.combo_picture,1,1)
        self.grid_2.addWidget(self.combo_colour,2,1)
        self.grid_2.addWidget(self.change_button,2,3)
        self.call_grid_2 = QtGui.QWidget()
        self.call_grid_2.setLayout(self.grid_2) # here is my second layout
        
        
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.calling_grid)
        self.vbox.addWidget(self.call_grid_2)
        self.calling_vbox = QtGui.QWidget()
        self.calling_vbox.setLayout(self.vbox)
        
        
        self.hbox = QtGui.QHBoxLayout()
        
        #self.hbox.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        #self.hbox.setAutoFillBackground(True)
        
        self.pic_label.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        self.pic_label.setAutoFillBackground(True)
        
        self.calling_vbox.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        self.calling_vbox.setAutoFillBackground(True)
        
        
        self.hbox.addWidget(self.pic_label)
        self.hbox.addStretch(0)
        self.hbox.addWidget(self.calling_vbox)
        
        self.calling_hbox = QtGui.QWidget()
        self.calling_hbox.setLayout(self.hbox)
        
        self.grid_3 = QtGui.QGridLayout()
        self.grid_3.addWidget(self.label,0,0)
        self.grid_3.addWidget(self.calling_hbox,0,0)
        self.setLayout(self.grid_3)
        #self.setLayout(self.hbox)
        
        
        self.connect(self.change_button,QtCore.SIGNAL('clicked()'), self.change_pic)
        
        #self.connect(self.close_button,QtCore.SIGNAL('clicked()'), self.change_colour)
        self.close_button.clicked.connect(self.close_button2)
        self.new_game_button.clicked.connect(self.restart)
        self.change_button.clicked.connect(self.change_colour)
    
    
    def connect_button(self):
        self.a+=1
        shost = self.edit.text()
        if self.a ==1 and int(shost) < self.secret_number:
            
            self.label1.setText(shost)
            self.label_guess2.setText("guess 2:")
            self.response1.setText("too small")
            self.edit.clear()
        elif self.a ==1 and int(shost) >self.secret_number:
                        
            self.label1.setText(shost)
            self.label_guess2.setText("guess 2:")
            self.response1.setText("too big")
            self.edit.clear()
        elif self.a ==1 and shost ==self.secret_number:
                        
            self.label1.setText(shost)
            self.response1.setText("correct")
            #self.a = 0
            self.edit.clear()
        elif self.a == 2 and int(shost) <self.secret_number:
            #shost = self.edit.text()
            
            shost = self.edit.text()
            self.label_guess3.setText("guess 3:")
            self.label2.setText(shost)
            self.response2.setText("too small")
        
        elif self.a == 2 and int(shost) >self.secret_number:
            #shost = self.edit.text()
                        
            shost = self.edit.text()
            self.label_guess3.setText("guess 3:")
            self.label2.setText(shost)
            self.response2.setText("too big")
            self.edit.clear()
        
        elif self.a ==2 and shost ==self.secret_number:
                                    
            self.label2.setText(shost)
            self.response2.setText("correct")
            #self.a = 0
            self.edit.clear()
            
        elif self.a ==3 and int(shost) < self.secret_number:           
            self.label3.setText(shost)
            self.response3.setText("too small")
            self.edit.clear()
        
        elif self.a ==3 and int(shost)>self.secret_number:
                                               
            self.label3.setText(shost)
            self.response3.setText("too big")
            self.edit.clear()
        
        elif self.a ==3 and int(shost)==self.secret_number:
                                                           
            self.label3.setText(shost)
            self.response3.setText("correct")
            #self.a = 0
            self.edit.clear()
    def change_pic(self):
        self.pic_name = self.combo_picture.currentText()
        if self.pic_name =="pluto":
            self.pixmap = QtGui.QPixmap("pluto.gif")
            self.pic_label.setPixmap(self.pixmap)
            #self.pixmap = QtGui.QPixmap('pluto.gif')
            #self.pic_label = QtGui.QLabel()
            #self.pic_label.setPixmap(self.pixmap)
        elif self.pic_name == "mickey":
            self.pixmap = QtGui.QPixmap("mickey.gif")
            self.pic_label.setPixmap(self.pixmap)
    def change_colour(self):
        self.colour_name = self.combo_colour.currentText()
        if self.colour_name == "red":
            self.label.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            self.label.setAutoFillBackground(True)            
            self.pic_label.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            self.pic_label.setAutoFillBackground(True)
                    
            self.calling_vbox.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            self.calling_vbox.setAutoFillBackground(True)
        elif self.colour_name == "blue":
            self.label.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            self.label.setAutoFillBackground(True)            
            self.pic_label.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            self.pic_label.setAutoFillBackground(True)
                    
            self.calling_vbox.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            self.calling_vbox.setAutoFillBackground(True)            
    def close_button2(self):
        sys.exit()
    def restart(self):  # function connected to when restart button clicked
        #self.close()
        self.secret_number = random.randint(1,10)
        self.label3.clear()
        self.label2.clear()
        self.label1.clear()
        self.response1.clear()
        self.response2.clear()
        self.response3.clear()
        self.edit.clear()
        self.label_guess2.clear()
        self.label_guess3.clear()
        
        self.a = 0
def main():
    app = QtGui.QApplication(sys.argv)
    calling = GuessingGame()
    calling.show()
    sys.exit(app.exec_())
    
main()   