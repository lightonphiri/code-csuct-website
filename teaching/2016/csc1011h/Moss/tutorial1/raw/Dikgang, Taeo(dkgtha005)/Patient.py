# Thapelo Dikgang
# Patient class
# 27-feb-2016


from Person import Person                                                       # Importing Person class 
class Patient(Person):                                                          # Creating a Patient class that inherits from Person
   
    def __init__(self,id_nmbr,address,visits,n=None,a=None):                    # Initializing object variables
        Person.__init__(self,n,a)
        self.id_number=id_nmbr
        self.address=address
        self.visits=visits
        
    def __str__(self):                                                          # Converting object to string
        return ('Name: '+self.name+','+' Age: '+str(self.age)+','+' ID Number: '+str(self.id_number)+','+' address: '+str(self.address)+','+' Number of visits: '+str(self.visits))
                
    def total_medical_fees(self):                                               # Calculating the total medical fees owed based on the standard fee of R200 per visit
        return ('Total medical fees owed: '+'R'+str(200*self.visits))               
        