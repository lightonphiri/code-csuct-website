# Person subclass called Doctor - OOP(Inheritance)
# Simphiwe Mchunu
# 23 February 2016

from Person import Person
class Doctor(Person):
    def __init__(self,ide=0,adr=None,nm=None,ag=0):  # constructor which initialises parameters to be accessed throughout the programme
        Person.__init__(self,nm,ag)
        self.address= adr
        self.identitynumber=ide
        
    def __str__(self): # string method to print to display the details
        return(self.name+','+str(self.age)+','+str(self.identitynumber)+','+self.address)
    def display(self):  # dispay method that summarises all details
        return(self.name+'\n'+str(self.age)+'\n'+str(self.identitynumber)+'\n'+self.address+'\n'+'---------------'+'\n')
        
    