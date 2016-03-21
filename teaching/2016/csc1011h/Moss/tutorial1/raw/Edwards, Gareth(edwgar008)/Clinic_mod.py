# Program to create patients doctors and appointments (using pickle)
# EDWGAR008

from Person import Person 
from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
from datetime import *
import pickle

patients = []                         # empty lists for information to appended
doctors = []
appointments = []

def add_patient():
    while True:
        cond = input("Enter Patient(y/n)? ")               # determines if function breaks or not
        if cond == 'y':
            n = input("Enter the name of the patient: ")
            a = input("Enter the age of the patient: ")
            ID = input("Patient ID number: ")
            addr = input("Patient address: ")
            numv = input("Number of visits of patient: ")
            
            P = Patient(n,a,ID,addr,numv)
            patients.append(P)
            
        elif cond == 'n':break
    
    patient_file = open('patient.txt','wb')                      # opening a file for writing
    pickle.dump(patients, patient_file)                          # dumping list of patient objects to the file opened
    patient_file.close()                                         # closing file
        
def add_doctor():
    while True:
        
        cond = input("Enter Doctor(y/n)? ")
        if cond == 'y':
            n = input("Enter the name of the doctor: ")
            a = input("Enter the age of the doctor: ")
            DID = input("Doctors ID number: ")
            addr = input("Doctor address: ")  
            
            D = Doctor(n,a,DID,addr)
            doctors.append(D)
            
        elif cond == 'n':break
    
    doctor_file = open('doctor.txt','wb')
    pickle.dump(doctors, doctor_file)
    doctor_file.close()    
    
def add_appointment():
    cond = input("Enter an appointment (y/n)? ")
    if cond == 'y':
        ID = input("Patient ID number: ")
        DID = input("Doctors ID number: ")
        timestamp = datetime.now()
        des = input("What is wrong with the patient: ")
        
        A = Appointment(ID,DID,timestamp,des)
        appointments.append(A)
        
    appointment_file = open('appointment.txt','wb')
    pickle.dump(appointments, appointment_file)
    appointment_file.close()    
        

def display_patients():
    for i in patients:
        print(i)
        
def display_doctors():
    for i in doctors:
        print(i)
        
def display_appointments():
    if len(appointments)>=1:
        for i in appointments:
            print(i)
    else:
        print('No appointments')

    
#def search_appointment():
    #pat_id = input("Patient ID: ")
    

        
def main():
    
    while True:
        
        print('1. Add Patient')
        print('2. Add Doctor')
        print('3. Add Appointment')
        print('4. Display Patients')
        print('5. Display Doctors')
        print('6. Display Appointments')
        print('7. search Appointment')
        num = input('Enter number (0 to quit): ')
        
        if num == '1':
            add_patient()
        elif num == '2':
            add_doctor()
        elif num == '3':
            add_appointment()
        elif num == '4':
            display_patients()
        elif num == '5':
            display_doctors()
        elif num == '6':
            display_appointments()
        elif num == '7':
            search_appointment()
        elif num =='0':
            break
    
main()