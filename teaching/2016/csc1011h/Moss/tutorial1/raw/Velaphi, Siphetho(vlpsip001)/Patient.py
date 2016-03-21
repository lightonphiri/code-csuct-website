from Person import*

class Patient(Person):
    def __init__(self,ID='unknown',address='unknown',visits=2):   # create a constructor
        self.ID_number=ID                                         # create variables
        self.address=address
        self.number_of_visits=visits
    def __str__(self):
        return('Patient:' +Person.__str__(self)+', '+str(self.ID_number)+', '+ str(self.address)+', '+str(self.number_of_visits))   #string conversion method for printing
    def total_fees(self):
        return('Total cost: R'+str(self.number_of_visits*200)) #calulating total consultation cost
p=Patient()
p.name='asaa'
p.age=17
p.ID_number='9605295962085'
print(p)
print(p.total_fees())
        
