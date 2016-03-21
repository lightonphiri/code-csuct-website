import time
class Appointment:
    
    date=""
    
    def __init__(self,pId=0,dId=0,memo="Unknown"):
        self.patient_id=pId
        self.doctor_id=dId
        Appointment.date=str(time.asctime( time.localtime(time.time()) ))  #str(datetime.now())
        self.appmnt_description=memo
        
    def __str__(self):
        return str(self.patient_id)+" | "+str(self.doctor_id)+" | "+str(Appointment.date)+": "+self.appmnt_description+"."
    
    def display(self):
        print("Patient's ID:",self.patient_id)
        print("Doctor's ID:",self.doctor_id)
        print("Appointment date:",Appointment.date)
        print("Memo:",self.appmnt_description)
        