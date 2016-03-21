# A program that creates a patient class
# Xhanti Singatha
# 28 February 2016


from Person import Person 

class Patient(Person):
    
    def __init__(self,n='unknown',a=0,id_number=0,address='unknown',num_of_visits=0):
        Person.__init__(self,n,a)
        self.id_number = id_number 
        self.address = address
        self.num_of_visits = num_of_visits
        
    def total_med_fee(self):
        t = self.num_of_visits*200
        return t
    
    def __str__(self):
        s = self.name+','+str(self.age)+','+str(self.id_number)+','+self.address+','+str(self.num_of_visits)+','+'R '+str(self.num_of_visits*200)
        return s
    
    