from Person import Person
class Patient(Person):  # Patient inherits from person
    def __init__(self,i="Unknown",ad="Unknown",nu=0,n=None,a=None):
        Person.__init__(self,n,a) # calling Person's constructor
        self.idnumber=i
        self.adress=ad
        self.visit=nu
    def __str__(self):
        return "Name:, "+self.name+"age: ,"+str(self.age)+"ID number: ,"+self.idnumber+"Adress: ,"+self.adress+"Number of visit"+str(self.visit)
    def fees(self): # fees method overrided
        return "R "+str(self.visit*200)


    