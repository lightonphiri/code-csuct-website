# Progam to create an appointment class
# Phndile Xulu
# 28/02/2016


import datetime 

class Appointment():
    def __init__(self,id1="Unknown",id2="Unknown",t="Unknown"):
        self.doc_id=id1
        self.pat_id=id2
        self.time=t
        
    def __str__(self):
        return (str(self.doc_id)+","+str(self.pat_id)+","+str(self.time))
    
    def memo(self):
        self.memo=input("Enter discription for the appointment:\n")
        return ("Description: "+self.memo)
    
    def appointment_time(self):
        self.appointment_time=datetime.datetime(int(self.time[0:4]),int(self.time[5:7]),int(self.time[8:10]),int(self.time[11:13]),int(self.time[14:16]))
        return (self.appointment_time)
    def display(self):
        return ("Doctors I.D number: "+self.doc_id+"\n"+"Patient's I.D number: "+self.pat_id+"\n"+"Time: "+str(self.appointment_time())+"\n"+"Memo: "+self.memo+"\n"+"________________________")
