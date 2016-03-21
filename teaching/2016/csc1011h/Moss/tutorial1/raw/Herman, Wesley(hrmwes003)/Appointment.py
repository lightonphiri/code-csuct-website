# Appointment class
# Wesley Herman
# HRMWES003

from Patient import Patient
from Doctor import Doctor

class Appointment(Patient, Doctor):
    
    # constructor
    def __init__ (self, pid=None, did=None, ts=None, m=None):
        self.patient_id = pid
        self.doctor_id = did
        self.timestamp = ts
        self.memo = m
    
    # string conversion    
    def __str__ (self):
        return ("Patient ID: " + self.patient_id + ", " + "Doctor ID: " + self.doctor_id + ", " + "Time of Appointment: " + str(self.timestamp) + ", " + "Memo: " + self.memo)
    
    # display override
    def display(self):
        print("Patient's ID: ", self.patient_id)
        print("Doctor's ID: ", self.doctor_id)
        print("Time of appointment:", self.timestamp)
        print("Memo:", self.memo)