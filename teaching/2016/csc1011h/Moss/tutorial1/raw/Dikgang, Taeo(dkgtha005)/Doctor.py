# Thapelo Dikgang
# Doctor class
# 27-feb-2016


from Person import Person                                                       # Importing Person class
class Doctor(Person):                                                           # Creating a Doctor class that inherits from Person
    
    def __init__(self,id_nmbr,addrs,n=None,a=None):                             # Initializing object variables
        Person.__init__(self,n,a)
        self.id_number=id_nmbr
        self.address=addrs
        
    def __str__(self):                                                          # Converting the object to string
        return ('Name: '+self.name+','+' Age: '+str(self.age)+','+' ID Number: '+str(self.id_number)+','+' address: '+str(self.address))
    
