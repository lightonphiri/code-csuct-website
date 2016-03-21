# clinic appointment system
# simnikiwe khonto
# 29 February 2016

import pickle
import datetime
import time
from Person import Person
from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment

Patients_1 = {}
Doctors_1 = {}
Appointments_1 = {}
PatientFile = open('pickled.txt','wb')
DoctorFile = open('pickled.txt','wb')
AppointmentFile = open('pickled.txt','wb')
PFile = open('pickled.txt','rb')
DFile = open('pickled.txt','rb')
AFile =  open('pickled.txt','rb')
dr = []
p = []
pp =[]
drr =[]
app =[]
r = 0
counter = 0
n = {}
x = {}

while True:
    print("Clinic appiontment System: ")
    my_dictionary = {0:'Quit',1:'Input Patients',2:'Input Doctors',3:'Input Appointments',4:'Place patients appointment',5:'Place doctors appointment',6:'Find Patient',7:'Find doctor',8:'Display appointments',9:'Display patients',10:'Display doctors'}
    
    for k in my_dictionary:
        print(str(k)+".",my_dictionary[k])
    user_input = eval(input(">"))
    if user_input == 0:     #option to quit
        break
    elif user_input > k or user_input < 0:
        print("That selection was invalid.")
    else:
        if user_input == 1:   #option to input patients into the system
            patient_name = input("Enter patient/'s name: ")
            ID_number = input("Enter patient/'s identity number: ")
            age = input("Enter patient/'s age:" )
            address = input("Enter patient/'s address:")
            Patients_1[ID_number] = patient_name   
        elif user_input == 2:    #option to input doctors into the system
            doctor_name = input("Enter doctor/'s name: ")
            dr_ID_number = input("Enter doctor/'s identity number: ")
            age = input("Enter doctor/'s age:" )
            address = input("Enter doctor/'s address:")            
            Doctors_1[dr_ID_number] = doctor_name   
        elif user_input == 3:     #option to input appointments into the system
            e = Appointment()
            e.patient_identity_no= (input("Enter patient/'s identity number: "))
            e.doctor_identity_no= (input("Enter doctor/'s identity number: "))
            e.timestamp= (str(input('Enter appointment date (yy,mm,dd,hours,minutes,00): ')))
            e.description = (input("Type the discription:"))
            appointment = datetime.datetime(int(e.timestamp[0:4]),int(e.timestamp[5:7]),int(e.timestamp[8:10]),int(e.timestamp[11:13]),int(e.timestamp[14:16]))            
            Appointments_1[appointment] = e
        if user_input == 4:      #option to place a patient for an appointment
            if r == 0:
                for i in Appointments_1:
                    n[i] = []
            r += 1
            patient_ID = input("Enter patient/'s identity number: ")
            app_time = str(input('Enter appointment date (yy,mm,dd,hours,minutes,00): '))
            appointment = datetime.datetime(int(app_time[0:4]),int(app_time[5:7]),int(app_time[8:10]),int(app_time[11:13]),int(app_time[14:16]))              
            if patient_ID in Patients_1:
                if appointment in Appointments_1:
                    p.append(Appointments_1[appointment])
                    n[patient_ID]=n[patient_ID] + p
                    p = []
                else:
                    print("Appointment date fully booked.")
            else:
                print("Could not find a patient with that identity number.")
                
        elif user_input == 5:         #option to place a doctor for an appointment
            if counter == 0:
                for i in Doctors_1:
                    x[i] =[]
            counter += 1            
            dr_ID_number = input("Enter doctor/'s identity number: ")
            app_time = str(input('Enter appointment date (yy,mm,dd,hours,minutes,00): '))
            appointment = datetime.datetime(int(app_time[0:4]),int(app_time[5:7]),int(app_time[8:10]),int(app_time[11:13]),int(app_time[14:16]))              
            if dr_ID_number in Doctors_1:
                if appointment in Appointments_1:
                    dr.append(Appointments_1[appointment])
                    x[dr_ID_number]=x[dr_ID_number] + dr
                    dr = []
                else:
                    print("Appointment date fully booked.")
            else:
                print("Could not find a doctor with that identity number.")
                
        elif user_input == 6:       #option to find if the patient exists at the clinic
            patient_ID = input("Enter patient/'s identity number: ")
            if patient_ID in Patients_1 and patient_ID not in n:
                try:
                    print(patient_ID+",",Patients_1[patient_ID])
                except:
                    print("Could not find a patient with that identity number.")
                    
        elif user_input == 7:           #option to find if the doctor exists at the clinic
            dr_ID_number = input("Enter doctor/'s identity number: ")
            if dr_ID_number in Doctors_1 and dr_ID_number not in x:
                try:
                    print(Doctors_1[dr_ID_number]+", "+ dr_ID_number +".")
                except:
                    print("Could not find a doctor with that identity number.")
                    
        elif user_input == 8:          # option to find appointments
            app = input("Enter the date of the appointment (yy-mm-dd hours:minutes:00): ")
            for s in Appointments_1:
                if s ==appointment:
                    app.append(s)
            pickle.dump(app,AppointmentFile)     
        elif user_input == 9:
            a = Patient()    # create object
            a.name = patient_name
            a.age = age
            a.patient_address = address
            a.patient_identity_no = ID_number            
            a.display()
            for i in Patients_1:  # take dictionary keys to make them one list
                pp.append(i)
            pickle.dump(pp,PatientFile) 
        elif user_input == 10:
            b = Doctor()         # create object
            b.name = doctor_name
            b.age = age
            b.doctor_address = address
            b.doctor_identity_no = dr_ID_number           
            b.display()
            for k in Doctors_1:
                drr.append(k)
            pickle.dump(drr,DoctorFile)
PatientFile.close() 
DoctorFile.close() 
AppointmentFile.close()