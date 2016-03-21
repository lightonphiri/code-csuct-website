# Ndlovu Mxoleleni
# NDLMXO003

from Person import Person            # importing Person class from Person module

class Doctor(Person):           # creating Doctor class
    def __init__(self,n='unknown',a=0,doc_ID=0,doc_addr="unknown"):        # constructor object method for Doctor class
        Person.__init__(self,n,a)           # calling Person constructor
        self.ID_number = doc_ID            # initialising object variable
        self.doctors_address = doc_addr         # initialising object variable
    
    def __str__(self):          # object method converting object to string
        return(self.name+","+str(self.age)+","+str(self.Doctors_ID)+","+self.Doctors_address)