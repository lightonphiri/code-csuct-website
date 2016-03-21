from Person import Person

class Doctor(Person):
    def __init__ (self,name='uknown',age=0,ID=None,a=None):
            self.doctor_ID = ID
            self.doctor_address = a
            Person.__init__(self,name,age) 
            
    def __str__(self):
        return(str(self.doctor_ID)+','+str(self.doctor_address))
    
    #def display(self):
            

