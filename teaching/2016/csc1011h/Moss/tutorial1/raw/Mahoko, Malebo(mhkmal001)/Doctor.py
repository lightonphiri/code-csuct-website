# malebo mahoko
# 22 february 2015
# class for storing details of doctors

from Person import Person                                           # importing the class person

class Doctor(Person):
    
    def __init__(self, n=None, a=None, i_d=None, ad=None,):
        Person.__init__(self,n,a)
        self.identity_number = i_d
        self.address = ad
        
    def __str__(self):                                              # string convertor
        return (str(self.name)+", "+str(self.age)+" ,"+str(self.identity_number)+" ,"+str(self.address))
    
    def display(self):                                      # display method from person being overrided
        Person.display(self)
        print("ID number:", self.identity)
        print("Address:", self.address)    
    
