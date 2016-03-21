# Question 3
# Wanga Mulaudzi
# 22 February 2016

from Person import Person
from Patient import Person
from Doctor import Doctor
import time

class Appointment:
    
    def __init__(self, PID = None, DID = None, ts = None, m = None):
        self.patient_ID = PID
        self.doctor_ID = DID
        self.time_stamp = ts
        self.memo = m
        
    def __str__(self):
        return ('Patient ID: ' + self.patient_ID + ', ' + 'Doctor ID: ' + self.doctor_ID + ', ' + 'Timestamp: ' + str(self.time_stamp) + ', ' + 'Memo: ' + self.memo)