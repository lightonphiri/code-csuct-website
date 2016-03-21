# c mahlasela
# 27 Feb 2016


from Person import Person

class Doctor (Person):                         #Patient inherits from Person
    
    def __init__(self, n = None, a = 0, id = None, add = None):
        Person.__init__(self, n, a)             #calling Person class
        self.ID_number = id
        self.address = add
        
    def __str__(self):                          #string convesion method
        return (self.name + " " + str(self.age) + " " + self.ID_number + " " + self.address)
    