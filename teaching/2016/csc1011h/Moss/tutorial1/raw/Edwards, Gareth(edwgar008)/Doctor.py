# creating a person class
#EDWGAR008

from Person import Person

class Doctor(Person):
    
    def __init__(self,n='unknown',a=0,DID='unknown',addr='unknown'):
        Person.__init__(self,n,a)
        self.doc_ID = DID
        self.address = addr
        
    def __str__(self):
        return str(self.name)+', '+str(self.age)+', '+str(self.doc_ID)+', '+str(self.address)
    
    