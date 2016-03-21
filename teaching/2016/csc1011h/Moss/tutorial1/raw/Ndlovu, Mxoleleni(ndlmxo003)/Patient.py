# Ndlovu Mxoleleni
# NDLMXO003

from Person import Person           # importing Person class from Person module

class Patient(Person):          # creating Patient class
    def __init__(self,n='unknown',a=0,pat_ID=0,pat_addr="unknown",no_of_vis=0):          # constructor object method for Patient
        Person.__init__(self,n,a)           # calling Person constructor
        self.ID_number = pat_ID         # initialising object variable
        self.patient_address = pat_addr            # initialising object variable 
        self.number_of_visits = no_of_vis           # initialising object variable 
        
    def total_medical_fees_owed(self):          # object method for calculating the total medical fees
        total_medical_fees_owed = self.number_of_visits*200
        
    def __str(self):            # object method converting object to string

        return(self.name + "," + str(self.age)+","+str(self.ID_number)+","+self.patient_address+","+str(self.number_of_visits))