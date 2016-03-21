# Menu based program 
# Xhanti Singatha
# 28 February 2016


import datetime
from Person import Person
from Patient import Patient
from Doctor import Doctor
import pickle
from Appointment import Appointment

patients = []
doctors = []
appointments = []
x = open('pickled.txt','wb')   

while True:
    print('***** Clinic System *****')

    options = {0:'1. Add a Patient',1:'2. Add a Doctor',2:'3. Add an Appointment',3:'4. Display Patients',4:'5. Display Doctors',5:'6. Display Appointments',6:'7. Search for and display appoinments for a particular patient or doctor',7:'8. Quit'}
    
    for key in options:
        print(options[key])
        
    option = int(input())
    
    if option == 1:
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        id_number= int(input('Enter ID number: '))
        address = input('Enter address: ')
        num_of_visits = int(input('Enter number of visits: '))
        p = Patient(name,age,id_number,address,num_of_visits)      # creating the patient object
        patients.append(p)                                       # this adds the patient object to the list 
        
    elif option == 2:
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        id_number= int(input('Enter ID number:'))
        address = input('Enter address: ')
        d = Doctor(name,age,id_number,address)                  # creating the doctor object 
        doctors.append(d)                                    # this adds the doctor object to the list 
    
    elif option == 3:
        patient_id_number= int(input('Enter patient\'s ID number: '))
        doctor_id_number= int(input('Enter doctor\'s ID number: '))
        
        year = int(input('Enter year: '))
        month = int(input('Enter month: '))
        date = int(input('Enter date: '))
        
        hour = int(input('Enter hour: '))
        minutes  =int(input('Enter minutes: '))
        
        time_stamp = datetime.datetime(year,month,date,hour,minutes)    # creating the datetime object (time stamp) 
        
        memo = input('Enter description of the appointment: ') 
        
        a = Appointment(patient_id_number,doctor_id_number,time_stamp,memo)   #creating the appointment object 
        appointments.append(a)                                              # this adds the appointment object to the list 
        
    elif option == 4:
        for i in patients:          # this displays all the patient objects in the patient list   
            print(i)
    
    elif option == 5:
        for i in doctors:           #  this displays all the doctor objects in the doctor list  
            print(i)
            
    elif option == 6:
        for i in appointments:      # this displays all the appointment objects in the appointment list  
            print(i)
            
    elif option == 7:
        b = int(input('Enter patient\'s ID number: '))
        k = int(input('Enter doctor\'s ID number: '))
        for i in appointments:
            if i.patient_id_number == b:        # this checks if the patient's ID number corresponds with the patient's ID number in the appointment object 
                if i.doctor_id_number == k:     # this checks if the doctor's ID number corresponds with the doctor's ID number in the appointment object 
                    print(i)                  # this displays the appointment that is checked in the above code
                else:
                    print('No appointment made')
            else:
                print('No appointment made')
                        

    else:
        break
    pickle.dump(patients,x)    # saves all the patient objects in the list to the file 
    pickle.dump(doctors,x)       # saves all the doctor objects in the list to the file 
    pickle.dump(appointments,x) # saves all the appointment objects in the list to the file        
    
x.close()
