#Makanatleng Phashe Junior
#2016/02/22
#Doctor

from Person import Person

class Doctor(Person):
    
    def __init__(self, a='', b = ''):
        
        self.IDNr = a
        
        self.Address = b
        
    def __str__(self):
        
        theString = self.IDNr +','+self.Address
        
        return theString
    
    
        
        
        
        
    
    
    