class Person:
    
    def __init__(self,n='unknown',a=0):
        self.name = n
        self.age = a

    def increment_age(self):
        self.age += 1
        
    def setName(self,name): # AN ADDITIONAL METHOD TO SET THE NAME OF THE PERSON
        self.name = name
        
    def setAge(self,age):   # AN ADDITIONALMETHOD TO SET THE AGE OF THE PERSON
        self.age = age
        
    def __str__(self):
        return(self.name + ',' + str(self.age))

    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)

