# A program that creates a doctor class
# Xhanti Sinagtha
# 28 February 2016

from Person import Person

class Doctor(Person):
    
    def __init__(self,n='unknown',a=0,id_number=0,address='unknown'):
        Person.__init__(self,n,a)
        self.id_number = id_number
        self.address = address
        
    def __str__(self):
        s = self.name+','+str(self.age)+','+str(self.id_number)+','+self.address
        return s
    