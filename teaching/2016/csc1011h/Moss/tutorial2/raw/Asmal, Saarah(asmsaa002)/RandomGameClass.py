import random

class RandomGameClass:
    
    def __init__(self,x=None,y=None,z=None,b="Too big",s="Too small",c="Correct"):
        guess = random.randrange(1,11,1)
        
        # x is the first guess   
        if x > guess:
            print (b)
        elif x < guess:
            print (s)
        elif x == guess:
            print (c)

        # y is the second guess        
        if y > guess:
            print (b)    
        elif y < guess:
            print (s)            
        elif y == guess:
            print (c)
        
        # z is the third guess        
        if z > guess:
            print (b)   
        elif z < guess:
            print (s)           
        elif z == guess:
            print (c)
            
        print (guess)     