#creating a menu-based program

from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment

import datetime
import time

p=Patient()
d=Doctor()
a=Appointment()

patient_list=[]
doctor_list=[]
appointment_list=[]


info=input('doctor, patient, appointment:\n') #say whether you want patient, doctor or appointments
print('choose any of the  options')
option1=input('(1)To add a patient, doctor or appointment enter 1\n(2)To display a patient,doctor or appointment press 2 \n(3)To search and display all the appointments for a particular patient or doctor press 3 \n(4) To quit press 4 \n')
   
while True:
    if info=='doctor' and option1==1:
        self.name=input('Enter name:')
        self.age=input('Enter age:')
        self.doctor_adress=input('Enter the doctors address:')
        self.doctor_id_number=input('Enter the doctors id')
         
        doctor_list.append([self.name,self.age,self.doctor_adress,self.doctor_id_number])
        
    elif info=='patient' and option1==1:
        self.name=input('Enter the patient name:')
        self.age=input('Enter patient age:')                                                                #this is the adding option
        self.ID_number=input('Enter the ID number:')
        self.patient_adress=input('Enter the address:')
        self.number_of_visits=input('Enter the number visits')
        
        patient_list.append([self.name,self.age,self.ID_number,self.patient_adress,self.number_of_visits])
        
    elif info=='appointment' and option1==1:
        patient_number=input('Enter the patient number:')
        patient_id=input('Enter the patient ID:')
        time_stamp=input('Enter the time stamp:')
        memo=input('Enter the memo:')
        
        appointment_list.append([patient_number,patient_id,time_stamp,memo])
    

    elif info=='doctor' and option1==2:
        print(doctor_list)
    elif info=='patient' and option1==2:    
        print(patient_list)                           #this is the option to display
    elif info=='appointment' and option1==2:
        print(appointment_list)

    elif option1==3:
        refrence=input('Enter the patient id:\n')   
        if refrence==appointment_list:
            print(apppointment_list)
    elif info==4:        #this is the quit option
        break
                