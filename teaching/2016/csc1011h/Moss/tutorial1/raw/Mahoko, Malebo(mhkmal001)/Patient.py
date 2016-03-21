# mahoko malebo
# 22 february 2016
# class for storing information of patients

from Person import Person                                               # import class Person 

class Patient(Person):                                                  # creating class Patient and inheriting Person                                       
    
    def __init__(self, n="unknown", a=None, i_d=None, ad=None, v=None):                      # constracter for the class, calling Person constructor and initialising viriables
        Person.__init__(self,n,a)
        self.identity_number = i_d
        self.address = ad
        self.number_of_visits = v

    def __str__(self):                                                                       #creating a string conversion
        return (self.name+", "+str(self.age)+", "+str(self.identity_number)+", "+str(self.address)+", "+str(self.number_of_visits))       
    
    def calculate_medical_fees(self):                                                        # creating a module which calculates medical fees based on number of visits
        fees = self.number_of_visits * 200
        return ("R"+str(fees))
    
    def display(self):                                      # display method from person being overrided
        Person.display(self)
        print("ID number:", self.identity)
        print("Address:", self.address)
        print("Number of visits:", self.number_of_visits)
    

    
