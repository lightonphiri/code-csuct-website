# Question 1
# Wanga Mulaudzi
# 22 February 2016

from Person import Person

class Patient(Person):
    
    def __init__(self, n = None, a = 0, PID = None, padd = None, nv = 0):
        Person.__init__(self, n, a)
        self.patient_number = PID
        self.patient_address = padd
        self.number_visits = nv
    
    def fees_owed(self):
        total = self.number_visits * 200
        return total
    
    def __str__(self):
        return ('Name: ' + self.name + ', ' + 'Patient ID: ' + self.patient_number + ', ' + 'Age: ' + str(self.age) + ', ' + 'Address: ' + self.patient_address + ', ' + 'Number of visits: ' + str(self.number_visits))