# Ntwanano Mazibuko
# Patient.py

from Person import Person

class Patient(Person):
    
    def __init__(self,n='None',a=0,id_n='unkwown',add='unkwown',n_v=0):
        Person.__init__(self,n,a)       # constructor method derived from parent
        self.pat_id_number=id_n         # varible to store patient's Id number
        self.pat_address=add            # variable to store patient's address
        self.num_of_visits=n_v          # variable to store the number of visits to the clinic
        
    def __str__(self):
        s= self.name+', '+str(self.age)+', '+str(self.pat_id_number)+', '+self.pat_address+', '+str(self.num_of_visits)     # method of converting to string
        return (s)
    #displays patients info
    def display(self):
        Person.display(self)
        print('Patient\'s Id number:',self.doc_id_number)
        print('Patient\'s address:',self.doc_address)        
    #function to calculate patients medical fees
    def calculate_medical_fees(self):
        return (200*self.num_of_visits)     # calculates amount owed by patient based on the standard fee, per visit
    #inputs for patient's information
    def input(self):
        self.pat_id_number=input('Enter Patient\'s Id number: ')
        self.pat_address=input('Enter Patient\'s address: ')