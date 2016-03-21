# malebo mahoko
# 25 february 2016
# class for details of appointments


class Appointment:
    def __init__(self, p_id=None, d_id=None, t=None, m="No memorandum"):
        self.patients_identity = p_id
        self.doctors_identity = d_id
        self.timestamp = t
        self.memo = m
        
    def __str__(self):
        s = str(self.patients_identity)+", "+str(self.doctors_identity)+", "+str(self.timestamp)+", "+self.memo
        return s
    