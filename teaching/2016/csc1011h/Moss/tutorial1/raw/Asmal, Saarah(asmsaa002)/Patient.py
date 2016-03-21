# Question 1 - Assignment 1
# ASMSAA002 - Saarah Asmal

from Person import Person

class Patient:
    
    def __init__(self,n=None,a=None,pat_i=0,pat_ad="unknown",v=0): # constructor to initialise variables
        Person.__init__(self,n,a) # calling Person constructor
        self.ID_num = pat_i # variable to store patients ID number
        self.address = pat_ad # variable to store patients address
        self.visits = v # variable to store number of visits to the clinic
        
    def med_fees(self): # method to calculate total fees
        m = (self.visits*200) 
        return ("R"+m)
    
    def __str__(self): # string conversion method
        s_pat = (self.name + "," + str(self.age) + "," + str(self.ID_num) + "," + self.address + "," + str(self.visits) + "," + str(self.med_fees))
        return (s_pat)
    