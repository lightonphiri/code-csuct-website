# make appointment
# simnikiwe khonto
# 29 february 2016
import datetime
class Appointment:
    
    def __init__(self,pID='unknown',drID='unknown',tm='unknown',d='unknown'):
        self.patient_identity_no = pID
        self.doctor_identity_no = drID
        self.timestamp = tm
        self.description = d
        
    def __str__(self):
        return(str(self.patient_identity_no)+','+str(self.doctor_identity_no)+','+str(self.timestamp)+','+self.description)
    
    def appointment(self):
        self.appointment = datetime.datetime(int(self.timestamp[0:4]),int(self.timestamp[5:7]),int(self.timestamp[8:10]),int(self.timestamp[11:13]),int(self.timestamp[14:16]))  # time for the appointment
        return(self.appointment)
       
    def display(self):  #create object appointment
        print("Patient/'s identity number:",self.patient_identity_no)
        print("Doctor/'s identity number:",self.doctor_identity_no)
        print("Appointment date and time:",self.appointment())
        print("Discription of the appointment:",self.description)
