# Ndlovu Mxoleleni
# NDLMXO003

class Appointment:          # creating Appointment class
    def __init__(self,pat_ID=0,Doc_ID=0,timestamp=0,memo="empty"):            # constructor object method for Appointment class
        self.patient_ID = pat_ID            # initialising object variable
        self.Doctor_ID = Doc_ID             # initialising object variable
        self.time_stamp = time_stamp            # initialising object variable
        self.memo = memo            # initialising object variable
        
    def __str__(self):          # object method converting object to string
        return(str(self.patient_ID)+","+str(self.Doctor_ID)+","+str(self.time_stamp)+","+self.memo)