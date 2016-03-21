
#Makanatleng Phashe Junior
#2016/02/22
#Patient 

from Person import Person

class Patient(Person): #Paitent inherits all the attributes of Person
    
    def __init__(self, a = '',b = '' ,c = 0):
        
        self.ID = a
        
        self.Address = b
        
        self.NrofVisits = c
        
        
        
    def totalfees(self):
        
        Value = NrofVisits*200

        return Value
    
    
    def __str__(self):    
        
        theString = self.ID +','+ self.Address +','+ str(self.NrofVisits)
        
        return theString
       
    
    
    
    