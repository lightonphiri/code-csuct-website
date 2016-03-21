from Person import Person
class Patient(Person):
    def __init__(self,id_number=None,address=None,number_visits=0,n="unknown",a=0):
        Person.__init__(self,n,a)
        self.id_number=id_number
        self.address=address
        self.number_visits= number_visits        
        
        
    def total_medical_fees(self):
        total_fees = self.number_visits * 200   # calculating the total amount of fees owed by the patient
        return total_fees
    def __str__(self):
        return (self.name+" "+str(self.age)+" "+str(self.id_number)+" "+self.address+" "+str(self.number_visits))
