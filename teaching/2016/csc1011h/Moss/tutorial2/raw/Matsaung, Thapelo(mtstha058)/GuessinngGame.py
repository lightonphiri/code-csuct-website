import sys
import random
from PyQt4 import QtGui,QtCore

class MySystem(QtGui.QWidget):
    def __init__(self,parent=None):             #imports objects in QWidget class
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(250,250,500,200)
        self.setWindowTitle('Guessing Game')
        
        label=QtGui.QLabel('Guesses:',self)     #this block creates labels as well as resize them
        label.setFont(QtGui.QFont('Arial',19))
        label1=QtGui.QLabel('Guess 1:',self)
        label1.setFont(QtGui.QFont('Arial',9))
        label2=QtGui.QLabel('Guess 2:',self)
        label2.setFont(QtGui.QFont('Arial',9))
        label3=QtGui.QLabel('Guess 3:',self)
        label3.setFont(QtGui.QFont('Arial',9))
        label4=QtGui.QLabel('Interface:',self)
        label4.setFont(QtGui.QFont('Arial',19))        
        label5=QtGui.QLabel('Picture:',self)
        label5.setFont(QtGui.QFont('Arial',9))
        label6=QtGui.QLabel('Colour:',self)
        label6.setFont(QtGui.QFont('Arial',9))
        
        pic_combo=QtGui.QComboBox()         #Creates drop-down Boxes         
        pic_combo.addItem('Mickey')
        pic_combo.addItem('Pluto')
        
        col_combo=QtGui.QComboBox()
        col_combo.addItem('red')
        col_combo.addItem('blue')
        
        no1=QtGui.QLabel('7',self)
        no2=QtGui.QLabel('4',self)
        no3=QtGui.QLabel('6',self)
        
        fedbac=QtGui.QLabel('Too high',self)
        fedbac1=QtGui.QLabel('Too low',self)
        fedbac2=QtGui.QLabel('correct',self)
        
        pic=QtGui.QPixmap('mickey')             #places the picture on the Widget, And characterises it
        pic_label=QtGui.QLabel('mickey',self)
        pic_label.setPixmap(pic)
        pic_label.setGeometry(0,0,200,250)        
        
        edit=QtGui.QLineEdit(self)
        text=edit.displayText()
        guess=QtGui.QPushButton('Guess')
        close=QtGui.QPushButton('Close')
        NG=QtGui.QPushButton('New Game')
        change=QtGui.QPushButton('Change')
                
        grid=QtGui.QGridLayout()                #This block sets out all the widgets to be in an orderly fashion
        grid.addWidget(pic_label,0,0,9,1)
        grid.addWidget(label,0,1,1,2)
        grid.addWidget(label1,1,1)
        grid.addWidget(label2,2,1)
        grid.addWidget(label3,3,1)
        grid.addWidget(no1,1,2)
        grid.addWidget(no2,2,2)
        grid.addWidget(no3,3,2)
        grid.addWidget(fedbac,1,3)
        grid.addWidget(fedbac1,2,3)
        grid.addWidget(fedbac2,3,3)
        grid.addWidget(edit,4,2)
        grid.addWidget(guess,4,3)
        grid.addWidget(label4,5,1,1,2)
        grid.addWidget(label5,6,1)
        grid.addWidget(label6,7,1)
        grid.addWidget(pic_combo,6,2)
        grid.addWidget(col_combo,7,2)
        grid.addWidget(close,8,1)
        grid.addWidget(NG,8,2)
        grid.addWidget(change,7,3)
        self.setLayout(grid)
        
        def closeButton():
            self.close()
        self.connect(close,QtCore.SIGNAL('clicked()'),closeButton)
        
            
        
def main():
    
    
    app=QtGui.QApplication(sys.argv)        #creates the neccessary app
    M=MySystem()
    
    
    M.setPalette(QtGui.QPalette(QtGui.QColor('red')))       #this method helps to set Background colour of the widget
    M.setAutoFillBackground(True)     
       
    M.show()
    sys.exit(app.exec_())
main()
        