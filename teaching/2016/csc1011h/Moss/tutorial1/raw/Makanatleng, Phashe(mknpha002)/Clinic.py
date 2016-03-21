#Makanatleng Phashe Junior
#2016/02/22
#Clinic

from Person import Person
from Doctor import Doctor
from Patient import Patient
from Appointment import Appointment
import pickle
import time
import binascii


#menu = {'1','2','3','4','5','6','7','8'}
menu = {}
menu[1] = 'Add patient.'

menu[2] = "Add Doctor."

menu[3] = "Add Appointment."

menu[4] = "Display all Patients."

menu[5] = "Display all Doctors."

menu[6] = "Display all Appointments."

menu[7] = "Search for appointments for a particular patient."

menu[8] = "Search for appointments for a particular Doctor."

menu[9] = "Quit"

#Variables
Patient_Name = ''
Patient_Age = 0
Patient_Address = ''
Patient_NrofVisits = 0
Doctor_Name = ''
Doctor_Age = 0
Appointment_time = ''
Appointment_Memo = ''
getfilename_ = ''
getfilename_2 = ''
getstring_ = ''



        

def pickle_to_file(filename,string_,filename2):
    try:
        file = open(filename,'ab')
        pickle.dump(string_,file)
        
        file2 = open(filename2,'a')
        file2.write(string_+"\n")
    finally:
        file.close()
        file2.close()
        time.sleep(3)
        
        
def display_list(filename,NameofList):
    try:
        file = open(filename,'r')
        fRead = file.readlines()
        
        for line in fRead:
            print(line)
            
    finally:
        file.close()
        time.sleep(3)
        
def search_list(string_,filename,Person):
    try:
        file = open(filename, 'r')
        
        fRead = file.readlines()
        
        for line in fRead:
            if string_ in line:
                print(line)
        else:
            print(Person,"does not exist")
    finally:
        file.close()
        time.sleep(3)
        
while True:
    Options = menu.keys()
    for entry in Options:
        print(entry,menu[entry])
        
    selection = eval(input("Choose an option i.e choose a number: "))
    
    if selection == 1:
        #Create Person Object:
        
        Patient_Name = input("Enter Patient Name : ")
        Patient_Age = eval(input("Enter Patient Age : "))
        
        Person_ = Person(Patient_Name,Patient_Age)
        
        #Create Patient:
        Patient_ID = input("Enter Patient ID Number : ")
        Patient_Address = input("Enter the Patient's Address : ")
        Patient_NrofVisits = eval(input("Enter the Patient's Number of Visits : "))
        
        Patient_ = Patient(Patient_ID,Patient_Address,Patient_NrofVisits)
        
        #pickle to file:
        getfilename_ = "patient.txt"
        getfilename_2 = "patient_unpickled.txt"
        getstring_ = Person_.__str__()+','+Patient_.__str__()      

        pickle_to_file(getfilename_,getstring_,getfilename_2)
        

    elif selection == 2:
        #Create Person Object:
        Doctor_Name = input("Enter Doctor Name : ")
        Doctor_Age = eval(input("Enter Doctor Age : "))
        
        Person_ = Person(Doctor_Name,Doctor_Age)
        
        #Create Doctor
        Doctor_ID = input("Enter Doctor ID Number : ")
        Doctor_Address = input("Enter the Doctor's Address : ")
        
        Doctor_ = Doctor(Doctor_ID,Doctor_Address)
        
        #pickle to file:
        getfilename_ = "doctor.txt"
        getfilename_2 = "doctor_unpickled.txt"
        getstring_ = Person_.__str__()+','+Doctor_.__str__()
        pickle_to_file(getfilename_,getstring_,getfilename_2)
        
    elif selection == 3:
        #Create Appointment Object:
        Patient_ID = input("Enter Patient ID Number : ")
        Doctor_ID = input("Enter Doctor ID Number : ")
        Appointment_time = input("Enter Appointment time dd/mm/yyyy: ")
        Appointment_Memo = input("Enter Appointment Memo : ")
        
        Appointment_ = Appointment(Patient_ID, Doctor_ID, Appointment_time, Appointment_Memo)
        
        #pickle to file:
        getfilename_ = "appointment.txt"
        getfilename_2 = "appointment_unpickled.txt"
        getstring_ = Appointment_.__str__()
        pickle_to_file(getfilename_,getstring_,getfilename_2)
        
    elif selection == 4:
        #def display_list(filename,NameofList):
        getfilename_ = "patient_unpickled.txt"
        display_list(getfilename_,"Patients")
        
    elif selection == 5:
        getfilename_ = "doctor_unpickled.txt"
        display_list(getfilename_,"Doctors") 
    
    elif selection == 6:
        getfilename_ = "appointment_unpickled.txt"
        display_list(getfilename_,"Appointments")
    
    elif selection == 7:
        #def search_list(string_,filename,Person):
        
        getstring_ = input("Enter Patient's name : ")
        getfilename_ = "appointment_unpickled.txt"
        search_list(getstring_,getfilename_, "Patient")
    
    elif selection == 8:
        
        getstring_ = input("Enter Patient's name : ")  
        getfilename_ = "appointment_unpickled.txt"
        search_list(doctor_list,"Doctor")
        
    elif selection == 9:
        print("Saved")
        print("You have succesfully Quit the program")
        break
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        