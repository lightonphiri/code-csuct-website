# appointment class
# mantombi manqele
# 21/02/2016

from Patient import Patient
from Doctor import Doctor

class Appointment(Patient, Doctor):
    def __init__(self, pidn = "unknown", didn = "unknown", ts = "unknown", m = "unknown"):
        Patient.__init__(self, pidn)
        Doctor.__init__(self, didn)
        self.timestamp = ts
        self.memo = m
        
    def __str__(self):
        return 'Patient ID: ' + str(self.patient_id) + ', ' + 'Doctor ID: ' + str(self.doctor_id) + ', ' + 'Timestamp: ' + str(self.timestamp) + ', ' + 'Memo: ' + str(self.memo)