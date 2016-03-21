class Appointment:
    def __init__(self,docId = "unknown",patId = "Unknown",timeStsmp = "unknown",memo = "unknown"):      # INITIALISES ALL THE VARIEBLES FOR THE APPOINTMENT FOR A DOCTOR AND
                                                                                                        #THEPATIENT
        self.patientId = patId
        self.doctorId = docId
        self.timeStamp = timeStamp
        self.memo = memo
        
    def setPatientId(self,ID):      # SETS THE ID OF THE PATIENT
        self.patientId = ID
        
    def setDoctorId(self,doctorId):
        self.doctorId = doctorId
        
    def setMemo(self,memo):
        self.memo = memo
    
    def setTimeStamp(self,timeStamp):
        self.timeStam = timeStamp
        
    def __str__(self):
        
        return("Patient Id: "+self.patientId+" , Doctor Id: "+self.doctorId+" , \nTime Stamp"+self.timeStamp+"\nMemo: "+self.memo)
    
    def display(self):
        
        print("Patient Id: "+self.patientId+" , Doctor Id: "+self.doctorId+" , \nTime Stamp"+self.timeStamp+"\nMemo: "+self.memo)
        
        
        
    