# Guessing Game
# 29 February 2016
# Wanga Mulaudzi

# import all necessary modules
import sys
from PyQt4 import QtGui, QtCore
import random

# create widget app class
class MyWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(250,250,350,300)
        self.setWindowTitle('Guessing Game')
        
        # intial image as variable
        self.pic_label = QtGui.QLabel()      
        
        # labels
        label1 = QtGui.QLabel('Guesses:',self)
        label1.setFont(QtGui.QFont('Times',16,3))        
        label2 = QtGui.QLabel('Interface:',self)
        label2.setFont(QtGui.QFont('Times',16,3))
        label3 = QtGui.QLabel('Picture:',self)
        label4 = QtGui.QLabel('Colour:',self)
        label5 = QtGui.QLabel('Guess 1:',self)
        label6 = QtGui.QLabel('Guess 2:',self)
        label7 = QtGui.QLabel('Guess 3:',self)
        self.label8 = QtGui.QLabel()
        self.label9 = QtGui.QLabel()
        self.label10 = QtGui.QLabel()
        self.label11 = QtGui.QLabel()
        self.label12 = QtGui.QLabel()
        self.label13 = QtGui.QLabel()
        
        # variables for the guessing part
        self.count = 0
        self.value = random.randint(1,10)
        
        # edit box
        self.edit = QtGui.QLineEdit(self)
        
        # buttons
        button1 = QtGui.QPushButton('Guess')
        button2 = QtGui.QPushButton('Change')
        button3 = QtGui.QPushButton('Close')
        button4 = QtGui.QPushButton('New Game')
        
        # combo box for the picture
        self.combo1 = QtGui.QComboBox()
        self.combo1.addItem('mickey')
        self.combo1.addItem('pluto')
        self.combo1_text = self.combo1.currentText()        
        
        # combo box for the colour
        self.combo2 = QtGui.QComboBox()
        self.combo2.addItem('red')
        self.combo2.addItem('blue')
        self.combo2_text = self.combo2.currentText()
        
        # initial window state
        pixmap = QtGui.QPixmap(self.combo1_text+'.gif')
        self.pic_label.setPixmap(pixmap)
        self.setPalette(QtGui.QPalette(QtGui.QColor(self.combo2_text)))        
        
        # add everything to a grid
        grid = QtGui.QGridLayout()
        grid.addWidget(self.pic_label,0,0,10,2)
        grid.addWidget(label1,0,3)
        grid.addWidget(label2,5,3)
        grid.addWidget(self.edit,4,4)
        grid.addWidget(button1,4,5)
        grid.addWidget(self.combo1,6,4)
        grid.addWidget(label3,6,3)
        grid.addWidget(button2,7,5)
        grid.addWidget(button3,8,3)
        grid.addWidget(button4,8,4)
        grid.addWidget(label4,7,3)
        grid.addWidget(self.combo2,7,4)
        grid.addWidget(label5,1,3)
        grid.addWidget(label6,2,3)
        grid.addWidget(label7,3,3)
        grid.addWidget(self.label8,1,4)
        grid.addWidget(self.label9,1,5)
        grid.addWidget(self.label10,2,4)
        grid.addWidget(self.label11,2,5)
        grid.addWidget(self.label12,3,4)
        grid.addWidget(self.label13,3,5)
        
        # set the grid's layout
        self.setLayout(grid)
        
        # signals
        self.connect(button3, QtCore.SIGNAL('clicked()'), self.closeButtonClicked)
        self.connect(button2, QtCore.SIGNAL('clicked()'), self.changeButtonClicked)
        self.connect(button1, QtCore.SIGNAL('clicked()'), self.guessButtonClicked)
        self.connect(button4, QtCore.SIGNAL('clicked()'), self.newButtonClicked)
    
    # function for when close button is clicked    
    def closeButtonClicked(self):
        self.close()
    
    # function for when change button is clicked    
    def changeButtonClicked(self):         
        pixmap = QtGui.QPixmap(self.combo1.currentText() + '.gif')
        self.pic_label.setPixmap(pixmap) # change picture
        self.setPalette(QtGui.QPalette(QtGui.QColor(self.combo2.currentText()))) # change background colour
    
    # function for when guess button is clicked    
    def guessButtonClicked(self):
        if self.count == 0: # update first rown
            number = int(self.edit.text())
            if number < self.value:
                self.label8.setText(str(number))
                self.label9.setText('To small')
            elif number > self.value:
                self.label8.setText(str(number))
                self.label9.setText('To big')
            elif number == self.value:
                self.label8.setText(str(number))
                self.label9.setText('Correct!')
            
        if self.count == 1: # update second row
            number = int(self.edit.text())
            if number < self.value:
                self.label10.setText(str(number))
                self.label11.setText('To small')
            elif number > self.value:
                self.label10.setText(str(number))
                self.label11.setText('To big')
            elif number == self.value:
                self.label10.setText(str(number))
                self.label11.setText('Correct!')
            
        if self.count == 2: # update third row
            number = int(self.edit.text())
            if number < self.value:
                self.label12.setText(str(number))
                self.label13.setText('To small')
            elif number > self.value:
                self.label12.setText(str(number))
                self.label13.setText('To big')
            elif number == self.value:
                self.label12.setText(str(number))
                self.label13.setText('Correct!')

        self.count = self.count + 1

    # function for when new game is clicked    
    def newButtonClicked(self):
        self.label8.setText('')
        self.label9.setText('')
        self.label10.setText('')
        self.label11.setText('')
        self.label12.setText('')
        self.label13.setText('')
        
def main():
    app = QtGui.QApplication(sys.argv)
    my_widget = MyWidget()
    my_widget.show()
    sys.exit(app.exec_())
        
main()