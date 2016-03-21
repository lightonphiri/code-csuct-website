class Appointment: # Appointment class created
    def __init__(self,ID="Unknown",id="Ubknown",m="unknown",d="Unknown"): # initialising appointment Variables
        self.pid=id
        self.did=ID
        self.memo=m
        self.day=d
    def __str__(self): # __str__ method overrided
        return "Doctor's ID: "+self.did+" Patient's ID "+self.pid+"MEMO: "+self.memo+" When the appointment is: "+self.day
    
