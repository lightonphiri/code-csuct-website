#creating appointment class

class Appointment:
    
    def __init__(self,n='unknown',ID='unknown',t="",m=""): #making a constructor with all the variables
        self.patient_number=n
        self.patient_id=ID
        self.time_stamp=t
        self.memo=m
        
    def __str__(self):
        s=str(self.patient_number)+','+str(self.patient_id)+','+str(self.time_stamp)+","+(self.memo)  #creating a string variable that will return a sring s
        return s