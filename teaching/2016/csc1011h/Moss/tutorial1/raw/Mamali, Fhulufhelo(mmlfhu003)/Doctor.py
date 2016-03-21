from Person import Person

class Doctor(Person): # Doctor inherits from person
    def __init__(self,n=None,Id="Unknown",ad="Unknown"):
        Person.__init__(self,n) # calling person's Contructor
        self.ID=Id
        self.address=ad
    def __str__(self): # __str__ method overrided 
        return "Name: "+self.name+" Address: "+self.address+" ID number: "+self.ID
