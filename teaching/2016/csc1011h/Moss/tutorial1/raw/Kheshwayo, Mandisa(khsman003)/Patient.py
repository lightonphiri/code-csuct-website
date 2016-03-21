#creating a patient class which inhetrits the person class

from Person import Person #importing the super class

class Patient(Person): #inheriting patient from person class
    
    def __init__(self,n='Unknown',a=0,ID='Uknown',PA='Uknown',NV=0):
        Person.__init__(self,n,a)     #calling the variable from the super class
        self.ID_number=ID
        self.patient_adress=PA               #making a constructor
        self.number_of_visits=NV
        
        
    def medical_fee(self):  #creating a medical fee function
        fee=(self.number_of_visits)*200     #calculating the fee by multiplying R200 by the number of visits
        return fee
    
    
    def __str__(self): #creating a string returning s
        s=(self.name)+','+str(self.age)+','+(self.ID_number)+','+(self.patient_adress)+','+str(self.number_of_visits)
        return s
    
    def patient_name(self): #this is only created so i can store the names 
        names=self.name      #that i would be using in the clinic.py program
        return names           #not part of the question