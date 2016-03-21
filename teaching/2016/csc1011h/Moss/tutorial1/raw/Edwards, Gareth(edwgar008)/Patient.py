# creating a patient class
# EDWGAR008

from Person import Person

class Patient(Person):
    
    def __init__(self,n='unknown',a=0,ID='unknown',addr='unknown',numv='unknown'):
        Person.__init__(self,n,a)
        self.ID_num = ID
        self.address = addr
        self.num_vis = numv
        
    def fees(self):
        return int(self.num_vis) * 200
    
    def __str__(self):
        return str(self.name) +', '+ str(self.age) + ', ' + str(self.ID_num) + ', ' + str(self.address) + ', ' + str(self.num_vis)


    