from Patient import*
from Doctor import*

class Appointment(Patient,Doctor):
    def __int__(self,time='unknown',memo='unknown'): # constructor
        self.time_stamp=time   ####create variables
        self.memo=memo
    def __str__(self):
        return( Doctor.__str_(self) +  Patient.__str__(self) + self.time_stamp + self.memo) #string conversion method for printing
