# Ntwanano Mazibuko
# Appointment.py

from time import *

#creates timestmp to be displayed
def timestamp():
    time=str(asctime())
    timestamp= time[0:3]+' '+time[8:10]+'/'+time[4:7]+'/'+time[20:]+' '+time[11:16]
    print(timestamp)

#definition of the Appointment class
class Appointment:
    
    def __init__(pat_id_n='unkwown',doc_id_n='unkwown',ts=timestamp(),memo='None'):        # constructor method to initialise variables
        self.pat_id_number=pat_id_n         # variable to store patient's id number
        self.doc_id_number=doc_id_n         # variable to store doctor's id number
        self.timestamp=ts                   # variable for storing the full timestamp of the appointment
        self.memo=memo                      # variable to store the description of what occured at the appointment
        
    def __str__(self):              # converts all variables from constructor into a single string
        s = self.pat_id_number+','+self.doc_id_number+','+self.timestamp+','+self.memo
        return (s) #returns string
    
    #displays all information concerning appointment
    def display(self):
        print('Patient\'s Id number:',self.pat_id_number)
        print('Doctor\'s Id number:',self.doc_id_number)
        print('Timestamp:',self.timestamp)
        print('Memo:',self.memo)