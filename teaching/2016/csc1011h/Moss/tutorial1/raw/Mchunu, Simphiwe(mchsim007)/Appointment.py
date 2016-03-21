# Appointment class - OOP
# Simphiwe Mchunu
# 27 February 2016
import datetime

class Appointment:
    def __init__(self,id1=0,id2=0,ts=0,m='Not Available'):  # constructor which initialises parameters to be accessed throughout the programme
        self.PatientID = id1
        self.DoctorID = id2
        self.timestamp2 = ts
        self.memo = m
        
    def __str__(self): # string method to print to display the details
        s = str(self.PatientID)+';'+str(self.DoctorID)+';'+str(self.timestamp2)+';'+self.memo
        return s
    def timestamp(self):
        '''method to calculate and store time'''
        self.timestamp2 = ts
    def display(self):  # dispay method that summarises all details
        return(str(self.PatientID)+'\n'+str(self.DoctorID)+'\n'+str(self.timestamp2)+'\n'+'----------------------------------')