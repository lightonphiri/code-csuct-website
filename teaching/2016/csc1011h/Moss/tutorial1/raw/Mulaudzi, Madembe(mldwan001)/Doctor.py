# Question 2
# Wanga Mulaudzi
# 22 February 2016

from Person import Person

class Doctor:
    
    def __init__(self, n = None, a = 0, DID = None, dadd = None):
        Person.__init__(self, n, a)
        self.doctor_number = DID
        self.doctor_address = dadd
        
    def __str__(self):
        return ('Name: ' + self.name + ', ' + 'Age: ' + str(self.age) + ', ' + 'Doctor ID: ' + self.doctor_number + ', ' + 'Address: ' + self.doctor_address)
    