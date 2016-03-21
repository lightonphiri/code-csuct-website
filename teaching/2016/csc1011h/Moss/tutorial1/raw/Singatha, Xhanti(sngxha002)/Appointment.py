# A program that creates an appointment class
# Xhanti Singatha
# 28 February 2016


class Appointment:
    
    def __init__(self,patient_id_number=0,doctor_id_number=0,time_stamp=0,memo='unknown'):
        self.patient_id_number = patient_id_number
        self.doctor_id_number = doctor_id_number
        self.time_stamp = time_stamp
        self.memo = memo
        
    def __str__(self):
        s = str(self.patient_id_number)+','+str(self.doctor_id_number)+','+str(self.time_stamp)+','+self.memo
        return s
    