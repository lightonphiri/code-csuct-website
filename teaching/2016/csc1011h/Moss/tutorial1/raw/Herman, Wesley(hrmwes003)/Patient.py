# Patient class
# Wesley Herman
# HRMWES003

from Person import Person

class Patient(Person):
    
    # constructor
    def __init__(self, n=None, a=None, id=None, ad=None, v=None):
        Person.__init__(self, n, a)
        self.patient_id = id
        self.patient_address = ad
        self.patient_visits = v
    
    # string    
    def __str__(self):
        return ("Patient name: "+ self.name + ", " + "Patient age: " + str(self.age) + ", " + "Patient ID number: " + str(self.patient_id) + ", " + "Patient Address: " + str(self.patient_address) + ", " + "Patient Visits: " + str(self.patient_visits) )
    
    # display override
    def display(self):	    
        Person.display(self)
        print("Patient ID: ",self.patient_id) 
        print("Patient address: ", self.patient_address)
        print("Patient visits: ", self.patient_visits)
    
    # fees owed
    def medical_fees_owed(self):
        mfo = self.patient_visits * 200
        return mfo