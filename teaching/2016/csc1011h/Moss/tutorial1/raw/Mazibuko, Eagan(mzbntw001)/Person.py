class Person:
    
    def __init__(self,n='unknown',a=0): #constructor for Person class
        self.name = n
        self.age = a
    #function for increasing person's age
    def increment_age(self):
        self.age += 1
    #string convertor
    def __str__(self):
        return(self.name + ',' + str(self.age))
    #displays person's information
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)

