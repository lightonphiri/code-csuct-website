# make doctor object
# simnikiwe khonto
# 29 february 2016

from Person import Person

class Doctor(Person):
    
    def __init__(self,n=None,a=None,drID=None,da=None):
        Person.__init__(self,n,a)
        self.doctor_identity_no = drID
        self.doctor_address = da
        
    def __str__(self):
        return(str(self.doctor_identity_no)+','+str(self.doctor_address))
    
    def display(self):     #create object doctor
        print('Name:',self.name)
        print('Age:',self.age)
        print("Doctor/'s identity number:",self.doctor_identity_no)
        print("Doctor/'s address:",self.doctor_address)
        