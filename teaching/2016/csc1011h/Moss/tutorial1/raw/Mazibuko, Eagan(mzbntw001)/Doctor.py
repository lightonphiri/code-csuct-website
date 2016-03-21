# Ntwanano Mazibuko
# Doctor.py

from Person import Person

class Doctor(Person):
    
    def __init__(self,n='None',a=0,id_n='unkwown',add='unkwown'):
        Person.__init__(self,n,a)       # constructor method from parent class
        self.doc_id_number=id_n         # variable to store doctor's id number
        self.doc_address=add            # variable to store doctor's address
        
    def __str__(self):          # converting all variables into a single string
        s= self.name+', '+str(self.age)+', '+str(self.doc_ID_Number)+', '+self.doc_address      
        return (s)
    #displays doctor's information
    def dispaly(self):
        Person.display(self)
        print('Doctor\'s Id number:',self.doc_ID_Number)
        print('Doctor\'s address:',self.doc_address)
    #inputs for doctor's info
    def input(self):
        self.doc_id_number=input('Enter Doctor\'s Id number: ')
        self.doc_address=input('Enter Doctor\'s address: ')