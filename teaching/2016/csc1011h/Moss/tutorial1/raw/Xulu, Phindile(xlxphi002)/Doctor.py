# Program to create a Doctor class
# Phndile Xulu
# 28/02/2016

from Person import Person

class Doctor(Person):
    def __init__(self,id1="Unknown", add1="Unknown",n="Unknown",a="Unknown"):                            #initialisor
            Person.__init__(self,n,a)
            self.doctor_id_no=id1
            self.doctor_address=add1
            
    def __str__(self):                                                                              #string conversion method                 
        return (self.name+","+self.age+","+self.doctor_id_no+","+self.doctor_address)
       
    def doctor_id_number(self):
        return self.id_no
    
    def doctor_address(self):
        return self.address    
    
    def display(self):
        return("Name: "+self.name+"\n"+"Age: "+str(self.age)+"\n"+"I.D number: "+ str(self.doctor_id_no)+"\n"+"Address: "+self.doctor_address+"\n"+"___________________")
               
