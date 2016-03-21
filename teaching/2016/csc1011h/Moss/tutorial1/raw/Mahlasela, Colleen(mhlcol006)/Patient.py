# c mahlasela
# 27 Feb 2016

from Person import Person

class Patient (Person):                         #Patient inherits from Person
    
    def __init__(self, n = None, a = 0, id = None, add = None, v = 0):
        Person.__init__(self, n, a)             #calling Person class
        self.ID_number = id
        self.address = add
        self.VisitNum = v
        
    def __str__(self):                          # string conversion method
        return (self.name + " " + str(self.age) + " " + self.ID_number + " " + self.address + " " + str(self.VisitNum))
    
    def total_fees(self):                       # calculate the total medical fees owed
        f = self.VisitNum * 200                 # standard fee 200 bucks per visit
        f = "R "+str(f)
        return f
    