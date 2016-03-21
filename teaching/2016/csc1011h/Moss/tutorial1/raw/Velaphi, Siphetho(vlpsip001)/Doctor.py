from Person import*

class Doctor(Person):
    def __init__(self,ID='unknown',address='unknown'): # create a constructor
        self.ID_number=ID                              # create variables
        self.address=address 
    def __str__(self):
        return('Doctor: '+self.name+ ', '+str(self.age)+', '+str(self.ID_number)+', '+ str(self.address)) #string conversion method for printing
p=Doctor()
p.name='asa'
p.age=17
p.ID_number='9605295962085'
print(p)
   