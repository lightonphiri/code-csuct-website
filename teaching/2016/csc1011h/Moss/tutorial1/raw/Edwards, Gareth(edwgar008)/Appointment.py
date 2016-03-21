# creating an appointment class
# EDWGAR008

from Person import Person
from Patient import Patient
from Doctor import Doctor


class Appointment:
    def __init__(self,ID='unknown',DID='unknown', time='unknown',des='No description'):
        self.ID_num = ID
        self.doc_ID = DID
        self.timestamp = time
        self.description = des
        
    def __str__(self):
        return str(self.ID_num)+', '+str(self.doc_ID)+', '+str(self.timestamp)+', '+str(self.description)
    
    def ID(self):                             # returning patient ID for search function in Clinic program
        return self.ID_num
    
    def DID(self):                            # returning doctor ID for search function in clinic program
        return self.doc_ID
    
    
        
    
    