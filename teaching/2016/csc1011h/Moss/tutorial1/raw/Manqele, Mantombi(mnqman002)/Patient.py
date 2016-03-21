# inheriting Person class to write Patient class
# mantombi manqele
# 21/02/2016

from Person import Person

class Patient(Person):
    def __init__(self, pidn = 'unknown', paddr = 'unknown', v = 0, n = 'unknown', a = 0):
        Person.__init__(self, n, a)
        self.patient_id = pidn            
        self.patient_address = paddr        
        self.visits = v
        
    def __str__(self):
        return 'Name: ' + str(self.name.title()) + ', Age: ' + str(self.age) + ', ID: ' + str(self.patient_id) + ', Address: ' + str(self.patient_address) + ', Visits: ' + str(self.visits)
    
    def calculate_fees(self):
        return self.visits * 200
    