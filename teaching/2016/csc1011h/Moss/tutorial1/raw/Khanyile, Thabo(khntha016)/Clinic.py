from Person import Person
from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
from datetime import datetime, date, time

lst = [1,2,3]
a = int(input('Enter option:'))
patient =[]
doctor = []
appointment =[]

while True:
    #a = int(input('Enter option:'))
    for i in lst:
        if a == 1:
            n = input('Enter name:')
            age = input('Enter age:')
            ID = input('Enter ID:')
            ad = input('Enter address:')
            v = input('Enter number of visits:')
            P = Patient(n,age,ID,ad,v)
            patient.append(P)
            print(lst)
    
        elif a == 2:
            n = input('Enter name:')
            ID = input('Enter ID:')
            ad = input('Enter address:')
            D = Doctor(n,ID,ad)
            doctor.append(D)
            print(doctor)
            
        elif a == 3:
            p_id = input('Enter patient id:')
            d_id = input('Enter doctor id:')
            d =input('Enter date:')
            t = input('Enter time:')
            memo = str(input('description of what happened at the appointment:'))
            c = datetime.combine(d, t)
            date = datetime.datetime(c)
            app = Appointment(p_id,d_id,date,memo)
            appointment.append(app)
            print(appointment)
          
        elif a > 3:break
             