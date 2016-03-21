# c mahlasela
# 28 Feb 2016

class Appointment:                          # class heading
    
    def __init__(self, pi = None, di = None, t = None, m = None):
        self.patient_id = pi
        self.doctor_id = di
        self.timestamp = t
        self.memo = m
        
    def __str__(self):                      # string conversion method
        return str(self.patient_id + " " + self.doctor_id + " " + self.timestamp + " " + self.memo)