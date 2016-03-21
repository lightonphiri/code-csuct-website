from Person import*

class Patient(Person):
    def __init__(self,name = "unknown",age = 0,Id = "unknown",Adress = "unknown", visits = 0):  # CONSTRUCTOR METHOD WHICH INITIALISES ALL THE VARIABLES
        
        self.identityNumber =  Id
        self.adress = Adress
        self.visits = visits
        
        Person.__init__(self,name,age)  # SINCE PATIENT IS ALSO A PERSON(IT INHERITS FROMPERSON).. HENCE INITIALISES THE PERSON GIVING THE PATIENT A NAME AND AGE.
        
        #self.umntu = Person(name,age)
        
    def getMedicalFee(self):
        self.fee = self.visits*200
        return self.fee
    
    def display(self):                 # DISPLAYS ALL THE INFORMATIONABOUT THE PATIENT INCLUDING THE NAME
        
        print("Name: "+self.name+"\nAge: "+str(self.age)+"\nID Number: "+self.identityNumber+" \nAdress: "+self.adress+"\nFee amount: "+str(self.getMedicalFee())+"\nNuber of visits: "+str(self.visits))
       
    def visitIncrease(self):            # ONLY INCREASES THE NUMBER OF VISITS BY ONE UNIT
        self.visits +=1
        
    def setVisits(self,visits):         # SETS THE NUMBER OF VISITS THAT THE PATIENT HAS VISITED
        self.visits =visits
        
        
    
    def __str__(self):  
        return(self.identityNumber+" , " +self.adress+" , " + str(self.visits))
    
    
    def setID(self,Id):     # SETS THE ID NUMBER OF THE PERSON, JUST INCASE IT WAS WRONGLY ENTERED
        self.identityNumber = Id
        
    def setAddress(self,add):   # SETS THE ADDRESS OF THE PERSON, JUST INCASE IT WAS WRONGLY ENTERED
        self.adress = add
        
    '''def setFee(self,fee):
        self.fee = fee'''
        
    
        
        
        