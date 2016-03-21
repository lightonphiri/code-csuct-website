# inheriting Person class to write Doctor class
# mantombi manqele
# 21/02/2016

from Person import Person

class Doctor(Person):
    def __init__(self, didn = 'unknown', daddr = 'unknown', v = 0, n = 'unknown', a = 0):
        Person.__init__(self, n, a)
        self.doctor_id = didn        
        self.doctor_address = daddr      

    def __str__(self):
        return 'Name: ' + str(title(self.name)) + ', Age: ' + str(self.age) + ', ID: ' + str(self.doctor_id) + ', Address: ' + str(self.doctor_address)