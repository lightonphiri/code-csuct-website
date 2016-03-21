# Person subclass named Patient - OOP(Inheritance)
# Simphiwe Mchunu
# 23 February 2016

from Person import Person
class Patient(Person):
    def __init__(self,ide=0,adr=None,vst=0,n=None,a=0): # constructor which initialises parameters to be accessed throughout the programme
        Person.__init__(self,n,a)
        self.identitynumber= ide
        self.address=adr
        self.visits=vst
    def medical_fees_owed(self): # method that calculates amount owed
        self.c = int(self.visits)*200
        print('R'+str(self.c))
        return  self.c
    def __str__(self): # string method to print to display the details
        m = self.name+';'+str(self.age)+';'+str(self.identitynumber)+';'+self.address+';'+str(self.visits)
        return m
    def display(self): # dispay method that summarises all details
        return(self.address+'\n'+str(self.visits)+'\n'+str(self.name)+'\n'+str(self.identitynumber))
        
        
        

