#Makanatleng Phashe Junior
#2016/02/22
#Appointment

from Person import Person

class Appointment(Person):
    
    def __init__(self, a= '', b = '', c = '', d = ''):
        
        self.PatientID = a
        
        self.DoctorID = b
        
        self.time = c
        
        self.memo = d #Describes what happened at the appointment
        
    def __str__(self):
        
        theString = self.PatientID  +','+ self.DoctorID  +','+ self.time +','+ self.memo 

        return theString
    
    