# Dikgang Thapelo
# Appointment class
# 27-02-2016

import time
import datetime

class Appointment:                                                              # Creating an Appointment Class
        
    def __init__(self,p,d,t,m):                                                 # Initalizinng object variables
        self.patient_ID_number=p
        self.doctor_ID_number=d
        self.timestamp=time.mktime(datetime.datetime.strptime(t, "%d/%m/%Y").timetuple())
        self.memo=m
        
    def __str__(self):                                                          # Converting object to string
        return ("Patient's ID number: "+str(self.patient_ID_number)+','+"  Doctor's ID number :"+str(self.doctor_ID_number)+','+'  full timestamp: '+str(self.timestamp)+','+'  Memo: '+str(self.memo) )