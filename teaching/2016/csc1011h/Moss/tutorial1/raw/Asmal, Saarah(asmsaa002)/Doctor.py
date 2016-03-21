# Question 2 - Assignment 1
# ASMSAA002 - Saarah Asmal

from Person import Person

class Doctor:
    
    def __init__(self,n=None,a=None,doc_i=0,doc_a="unknown"): # constructor to initialise variables
        Person.__init__(self,n,a) # calling Person constructor
        self.ID_num = doc_i # variable to store doctor's ID number
        self.address = doc_a # variable to store doctor's address
        
    def __str__(self): # string conversion method
        s_doc = (self.name + "," + str(self.age) + "," + str(self.ID_num) + "," + self.address)
        return (s_doc)
        
    