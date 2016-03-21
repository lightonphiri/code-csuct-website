import sys
from PyQt4 import QtGui, QtCore
import random


class GuessingGame(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(250,250,200,150)
        self.setWindowTitle('Guessing Game')
        
        #background colour
        a=self.setPalette(QtGui.QPalette(QtGui.QColor('white'))) #made the default white so that the user can see if they changed the colour or not
        self.setAutoFillBackground(True)
        
        
        
        #label construction
        guess_label=QtGui.QLabel('Guesses :',self)
        guess_label.setFont(QtGui.QFont('Times',20,3))
        label1=QtGui.QLabel('Guess 1:',self)
        label2=QtGui.QLabel('Guess 2:',self)
        label3=QtGui.QLabel('Guess 3:',self)
        
            #empyt strings for the label
            
        self.str1=QtGui.QLabel('',self)
        self.str2=QtGui.QLabel("",self)
        self.str3=QtGui.QLabel("",self)
        self.info1=QtGui.QLabel('',self)
        self.info2=QtGui.QLabel('',self)
        self.info3=QtGui.QLabel('',self)
        
        
        interface_label=QtGui.QLabel('Interface :',self)
        interface_label.setFont(QtGui.QFont('Time',20,3))
        self.pic_label=QtGui.QLabel('Picture:',self)
        colour_label=QtGui.QLabel('Colour:',self)
        
        
        #edit construction
        
        self.guess_edit=QtGui.QLineEdit()
         
        
        self.picture_edit=QtGui.QComboBox()
        self.colour_edit=QtGui.QComboBox()
        self.picture_edit.addItem('Mickey')
        self.picture_edit.addItem('Pluto')
        
        
        self.colour_edit.addItem('red')
        self.colour_edit.addItem('blue')
   
        
        self.thing=0
        
        #construct botton
        
        guess_button=QtGui.QPushButton('Guess')
        guess_button.clicked.connect(self.guess)
        
        change_button=QtGui.QPushButton('Change')
        change_button.clicked.connect(self.change)
    
        close_button=QtGui.QPushButton('Close')
        close_button.clicked.connect(self.close)
        
        new_game_button=QtGui.QPushButton('New Game')
        new_game_button.clicked.connect(self.newgame)
        
        
        #picture
        self.pixmap = QtGui.QPixmap('mickey.gif') # constructor
        self.picture_label = QtGui.QLabel(self) 
        self.picture_label.setPixmap(self.pixmap) 
    
        
        
        #creating the grid
        
        grid=QtGui.QGridLayout()
        grid.addWidget(self.picture_label,0,0,8,1)         
        grid.addWidget(guess_label,0,2)
        grid.addWidget(label1,1,2)
        grid.addWidget(self.str1,1,3)
        grid.addWidget(self.info1,1,4)
        grid.addWidget(label2,2,2)
        grid.addWidget(self.str2,2,3)
        grid.addWidget(self.info2,2,4)
        grid.addWidget(label3,3,2)
        grid.addWidget(self.str3,3,3)
        grid.addWidget(self.info3,3,4)
        grid.addWidget(self.guess_edit,4,3)
        grid.addWidget(guess_button,4,4)
        grid.addWidget(interface_label,5,2)
        grid.addWidget(self.pic_label,6,2)
        grid.addWidget(self.picture_edit,6,3)
        grid.addWidget(change_button,6,4)
        grid.addWidget(colour_label,7,2)
        grid.addWidget(self.colour_edit,7,3)
        grid.addWidget(close_button,8,2)
        grid.addWidget(new_game_button,8,3)
        self.setLayout(grid)
    def close(self):
        sys.exit()
        
    def change(self):
        self.col_current= self.colour_edit.currentText()
        self.pic_current = self.picture_edit.currentText()
        
        if  self.pic_current =='Mickey' and self.col_current=='blue':
            self.pixmap = QtGui.QPixmap('mickey.gif')
            self.picture_label.setPixmap(self.pixmap)  
            a=self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            
        elif  self.pic_current =='Mickey' and self.col_current=='red':
            pixmap = QtGui.QPixmap('mickey.gif')
            self.picture_label.setPixmap(pixmap) 
            a=self.setPalette(QtGui.QPalette(QtGui.QColor('red')))     
            
        elif  self.pic_current =='Pluto' and self.col_current=='blue':
            self.pixmap = QtGui.QPixmap('pluto.gif')
            self.picture_label.setPixmap(self.pixmap) 
            a=self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            
        elif  self.pic_current =='Pluto' and self.col_current=='red':
            self.pixmap = QtGui.QPixmap('pluto.gif')
            self.picture_label.setPixmap(self.pixmap) 
            a=self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        
    def guess(self):
        self.random_number=random.randint(0,10)
        self.text=self.guess_edit.displayText()
        
        if int(self.text)==self.random_number and self.thing == 0:
            self.str1.setText(self.text)
            self.thing += 1
            self.guess_edit.clear()
            self.info1.setText('correct!')
        elif int(self.text)==self.random_number and self.thing == 1:
            self.str2.setText(self.text)
            self.thing += 1
            self.guess_edit.clear()            
            self.info2.setText('correct') 
        elif int(self.text)==self.random_number and self.thing == 2:
            self.str3.setText(self.text)
            self.thing += 1
            self.guess_edit.clear()            
            self.info3.setText('correct') 
        if int(self.text)<self.random_number and self.thing == 0:
            self.str1.setText(self.text)
            self.thing += 1
            self.guess_edit.clear()            
            self.info1.setText('To small') 
        elif int(self.text)<self.random_number and self.thing == 1:
            self.str2.setText(self.text)
            self.thing += 1
            self.guess_edit.clear()            
            self.info2.setText('To small') 
        elif int(self.text)<self.random_number and self.thing == 2:
            self.str3.setText(self.text)
            self.thing += 1
            self.guess_edit.clear()            
            self.info3.setText('To small')
        if int(self.text)>self.random_number and self.thing == 0:
            self.str1.setText(self.text)
            self.thing += 1
            self.guess_edit.clear()            
            self.info1.setText('To big')             
        elif int(self.text)>self.random_number and self.thing == 1:
            self.str2.setText(self.text)
            self.thing += 1
            self.guess_edit.clear()            
            self.info.setText('To big') 
        elif int(self.text)>self.random_number and self.thing == 2:
            self.str3.setText(self.text)
            self.thing += 1
            self.guess_edit.clear()            
            self.info3.setText('To big') 
            
            
    def newgame(self):
        self.str1.clear()         #this is to clear everything in the user has entered
        self.str2.clear()
        self.str2.clear()
        self.str3.clear()
        self.info1.clear()
        self.info2.clear()
        self.info3.clear()
        a=self.setPalette(QtGui.QPalette(QtGui.QColor('white'))) #made the default white so that the user can see if they changed the colour or not
        self.setAutoFillBackground(True)
               


                        
def main():
    app=QtGui.QApplication(sys.argv)
    my_game=GuessingGame()
    my_game.show()
    sys.exit(app.exec_())
main()