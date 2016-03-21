from Person import*
class Doctor(Person):
    
    def __init__(self,name = "unknown",age = 0,docId = "Unknown",docAdress = "unknown"):    #INITIALISES ALL THE VARIABLES REQUIRED FOR THE DOCTOR
        self.doctorId = docId
        self.doctorAddress = docAdress
        Person.__init__(self,name,age)
        
    def setDoctorId(self,newId):    # SETS THE DOCTOR'S ID
        self.doctorId = newId
        
    def setDoctorAddress(self,newAddress):      # SETS THE DOCTOR'D ADDRESS
        seld.doctorAddress = newAddress
        
        
    def __str__(self):
        #Person.__str__(self)
        return("Name: "+ self.name+"\nAge: "+str(self.age)+"\nDoctor Id: "+self.docId+"\nDoctor Address"+self.docAdress)
    
    def display(self):          #DISPLAYS ALL THE INORMATION ABOUUT THE DOCTOR
        print("Name: "+ self.name+"\nAge: "+str(self.age)+"\nDoctor Id: "+self.docId+"\nDoctor Address"+self.docAdress)
        
        
    