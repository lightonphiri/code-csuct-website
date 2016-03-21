#creating a doctor inherited from person

from Person import Person

class Doctor(Person):  #inheriting doctor from a super class called Person
    
    def __init__(self,n='Uknkown',a=0,ID='Uknkown',AD='Uknown'):
        Person.__init__(self,n,a)  #calling the variables from person class
        self.doctor_id_number=ID
        self.doctor_adress=AD                                            #making a constructor with all the variabes
        
    def __str__(self):
        s=(self.name)+','+str(self.age)+','+(self.doctor_id_number)+','+(self.doctor_adress) # creating a string function which returns s 
        return s