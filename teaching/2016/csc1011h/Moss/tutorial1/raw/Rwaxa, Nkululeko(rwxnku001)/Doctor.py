from Person import Person

class Doctor(Person):
    
    def __init__(self,n="Unknown",a=0,Id=0,ad="Unknown"):
        Person.__init__(self,n,a)
        self.id_number=Id
        self.address=ad
        
    def __str__(self):
        return self.name+" | "+str(self.age)+" | "+str(self.id_number)+" | "+self.address+"."
    
    def display(self):
        Person.display(self)
        print("ID Number:",self.id_number)
        print("Address:",self.address)
        
