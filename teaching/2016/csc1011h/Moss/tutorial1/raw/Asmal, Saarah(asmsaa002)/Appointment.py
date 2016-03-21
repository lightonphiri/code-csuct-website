# Question 3 - Assignment 1
# ASMSAA002 - Saarah Asmal

import datetime

class Appointment:
    def __init__(self,pat_i=0,doc_i=0,m=None): # constructor to initialise variables
        self.Pat_ID = pat_i # variable to store patient's ID number
        self.Doc_ID = doc_i # varible to store doctor's ID number
        self.memo = m # variable to store memo notes
        
    def time(self,year=0,month=0,day=0):
        datetime.time()
        
    def __str__(self): #string conversion method
        s =("patient ID:" + str(self.Pat_ID) + "," + "doctor ID:" + str(self.Doc_ID) + "," + "time:" + str(self.time) + "," + "memo" + str(self.memo))
        return (s)
        