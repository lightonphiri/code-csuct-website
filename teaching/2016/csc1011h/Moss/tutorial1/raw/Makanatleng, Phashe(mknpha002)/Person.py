class Person:
    
    def __init__(self,n='unknown',a=0):
        self.name = n
        self.age = a

    def increment_age(self):
        self.age += 1
        
    def __str__(self):
        return(self.name + ',' + str(self.age))

    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)

