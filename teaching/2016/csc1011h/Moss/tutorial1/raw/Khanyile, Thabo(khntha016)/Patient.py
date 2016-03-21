from Person import Person

class Patient(Person):
    def __init__ (self,name='uknown',age=0,ID=None,a=None,v=None,):
        self.patient_ID = ID
        self.patient_address = a
        self.visits = v
        Person.__init__(self,name,age)
        
    def __str__(self):
        return(str(self.patient_ID)+','+str(self.patient_address)+','+str(visits))
               
    def increment_number_of_visits(self):
        self.visits +=200
        
    def display(self):
        print( 'name:''\n'+'age''\n'+'ID Number:'+str(self.patient_ID)+'\n'+'Adress:'+str(self.patient_address)+'\n'+'Number of vivits:'+str(slef.visits))