# Doctor class
# Wesley Herman
# HRMWES003

from Person import Person

class Doctor(Person):
    
    # constructor
    def __init__ (self, n=None, a=None, did=None, dad=None):
        Person.__init__(self, n, a)
        self.doctor_id = did
        self.doctor_address = dad
    
    # string conversion    
    def __str__ (self):
        return ( "Doctor's name: " + self.name + ", " + "Doctor's age: " + str(self.age) + ", " + "Doctor's ID number: " + self.doctor_id + ", " + "Doctor's address: " + self.doctor_address )
    
    # display override
    def display(self):	    
        Person.display(self)
        print("Doctor ID: ",self.doctor_id) 
        print("Doctor address: ", self.doctor_address)    