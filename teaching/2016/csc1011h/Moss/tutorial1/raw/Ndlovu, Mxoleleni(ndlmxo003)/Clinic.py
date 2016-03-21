# Ndlovu Mxoleleni
# NDLMXO003

from Person import Person           # importing Person class
from Doctor import Doctor           # importing Doctor class
from Patient import Patient         # importing Patient class
from Appointment import Appointment         # importing Appointment class
import datetime                     # importing datetime
from time import gmtime, strftime           # importing gmtime, strftime from time
import pickle           # importing pickle

def main():         #defining main function
    
    '''lists to store patients,doctors and appointments'''
    patients = []
    doctors = []
    appointments = []
    
    print("*_*_*_*_*_CLINIC_*_*_*_*_*\n")
    print("__OPTIONS TO SELECT__\n""1: Add patient.\n""2: Add doctor.\n""3: Add appointment.\n""4: Display all the patients, doctors or appointments.\n""5: search for and display all the appointments for a particular patient.\n""6: Quit.\n")            # menu to choose from
    
    while True:
        option = int(input("Enter option: "))           # prompting the user to enter their option
        '''adding a patient'''
        if option == 1:
            Patient.name = input("Enter name: ")
            patients.append(Patient.name)
            Patient.age = int(input("Enter age: "))
            patients.append(Patient.age)
            Patient.ID_number = int(input("Enter ID: "))
            Patient.patient_address = input("Enter address: ")
            patients.append(Patient.ID_number)
            Patient.number_of_visits = int(input("Enter no. of visits: "))
            patients.append(Patient.number_of_visits)
            Appointment.memo = input("Enter memo: ")
            appointments.append(Appointment.memo)            
                       
        elif option == 2:
            '''adding a doctor'''
            Doctor.name = input("Enter name: ")
            doctors.append(Doctor.name)
            Doctor.age = int(input("Enter age: "))
            doctors.append(Doctor.age)
            Doctor.ID_number = int(input("Enter ID: "))
            doctors.append(Doctor.ID_number)
            Doctor.doctors_address = input("Enter address: ")
            doctors.append(Doctor.doctors_address)
        
        elif option == 3: 
            '''adding an appointment''' 
            Appointment.name = input("Enter name: ")
            appointments.append(Appointment.name)
            Appointment.age = int(input("Enter age: "))
            appointments.append(Appointment.age)
            Appointment.ID_number = int(input("Enter ID: "))
            appointments.append(Appointment.ID_number)
            Appointment.patient_address = input("Enter address: ")
            appointments.append(Appointment.patient_address)
            Appointment.time_stamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            appointments.append(Appointment.time_stamp)
            Patient.number_of_visits = int(input("Enter no. of visits: "))
            patients.append(Patient.number_of_visits)            
            Appointment.memo = input("Enter memo: ")
            appointments.append(Appointment.memo)
            
        elif option == 4:
            '''displaying all the patients,doctors and appointments'''
            print("Patients:",str(patients))
            print("Doctors:",str(doctors))
            print("Appointments:",str(appointments)+"\n")
        
            '''search for and display all the appointments for a particular patient'''
        elif option ==5:
            ID = input("Enter ID of patient or doctor: ")
            if ID in (patients or doctors):
                print(appointments)
            
        else:           # option to Quit
            break
        
        '''putting patients,doctors and appointments in one list'''
        combo_Lists = []            # empty list
        combo_Lists.append(patients)
        combo_Lists.append(doctors)
        combo_Lists.append(appointments)
        
        '''pickling the code'''
        outFile = open("pickle.txt", "wb")
        pickle.dump(combo_Lists, outFile)
        outFile.close()
        
        inFile = open("pickle.txt", "rb")
        newlist = pickle.load(inFile)
        inFile.close()
            
main()          # calling the main function