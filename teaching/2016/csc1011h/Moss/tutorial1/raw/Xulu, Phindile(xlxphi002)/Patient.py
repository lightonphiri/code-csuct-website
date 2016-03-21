# Program to create a Patient class
# Phindile Xulu
# 28/02/2016

from Person import Person

class Patient(Person):
    def __init__(self,id2="Unknown", add2="Unknown", no_of_vi="Unknown",n="Unknown",a="Unknown"):                            #initialisor
        Person.__init__(self,n,a)
        self.patient_id_no=id2
        self.patient_address=add2
        self.no_of_visits=no_of_vi
        
        
    def __str__(self):                                                                              #string conversion method                 
        return (self.name+","+self.age+","+self.patient_id_no+","+self.patient_address+","+self.no_of_visits)
    
    def patient_id_number(self):
        return self.patient_id_no
    
    def patient_address(self):
        return self.patient_address
    
    def no_of_visits(self):
        return self.no_of_visits
    
    def fees_owed(self):
        self.fees_owed=200*int(self.no_of_visits)
        return ("R"+str(self.fees_owed))
    
    def display(self):
        return("Name: "+self.name+"\n"+"Age: "+str(self.age)+"\n"+"I.D number: "+str(self.patient_id_no)+"\n"+"Address: "+self.patient_address+"\n"+"Number of visits: "+str(self.no_of_visits)+"\n"+"Fees Owed: "+"R"+str(self.fees_owed)+"\n"+"______________________")
       
    
