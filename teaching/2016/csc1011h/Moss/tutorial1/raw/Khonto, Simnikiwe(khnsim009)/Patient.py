# make a patient object
# simnikiwe khonto
# 29 february 2016
from Person import Person

class Patient(Person):
    
    def __init__(self,n=None,a=None,pID=None,pd=None,nv=None):
        Person.__init__(self,n,a)
        self.patient_identity_no = pID
        self.patient_address = pd
        self.no_of_visits = nv
        
    def __str__(self):
        return(self.name+','+str(self.age)+','+str(self.patient_identity_no)+','+str(self.patient_address)+','+str(self.no_of_visits))
               
    def total_medical_fees(self):    
        return(str(self.no_of_visits*200))    # calculate medical fees owed
        
    def display(self):     #create object person
        print('Name:',self.name)
        print('Age:',self.age)
        print("Patient/'s identity number:",self.patient_identity_no)
        print("Patient/'s address:",self.patient_address)
        #print("Total medical fees owed:",str(int(self.no_of_visits)*200))