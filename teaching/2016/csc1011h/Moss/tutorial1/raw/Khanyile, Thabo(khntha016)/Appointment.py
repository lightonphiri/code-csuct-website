class Appointment:
    def __init__(self,P_ID=None,D_ID=None,timestamp=None,memo=None):
        self.patient_ID = P_ID
        self.doctor_ID = D_ID
        self.timestamp = timestamp
        slef.memo = memo
        
    def changepatient_ID(self,ID):
        self.patient_ID = ID
            
    def changedoctor_ID(self,ID):
        self.doctor_ID = ID
        
    def changetimestamp(self,timestamp):
        self.timestamp = timestamp
            
    def chnagememo(self,memo):
        self.memo = memo
            
    def __str__(self): 
        return(str(self.patient_ID)+''+str(self.doctor_ID)+''+str(self.timestamp)+''+str(self.memo))
        