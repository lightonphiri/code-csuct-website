# Program to create patients doctors and appointments
# EDWGAR008

from Person import Person 
from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
from datetime import *
import pickle

patients = []
doctors = []
appointments = []

def add_patient():
    while True:
        cond = input("Enter Patient(y/n)? ")
        if cond == 'y':
            n = input("Enter the name of the patient: ")
            a = input("Enter the age of the patient: ")
            ID = input("Patient ID number: ")
            addr = input("Patient address: ")
            numv = input("Number of visits of patient: ")
            
            P = Patient(n,a,ID,addr,numv)
            patients.append(P)
            
        elif cond == 'n':break
        
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
    
def add_appointment():
    while True:
        cond = input("Enter an appointment (y/n)? ")
        if cond == 'y':
            ID = input("Patient ID number: ")
            DID = input("Doctors ID number: ")
            timestamp = datetime.now()
            des = input("What is wrong with the patient: ")
        elif cond=='n':break
        
        A = Appointment(ID,DID,timestamp,des)
        appointments.append(A)
        

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

    
def search_patients():                     # search for an appointment given the patient ID
    pat_id = input("Patient ID: ")
    for i in appointments:
        if pat_id == i.ID():
            print(i)
            
def search_doctors():                     # search for an appointment given the doctor ID
    doc_id = input("Doctor ID: ")
    for i in appointments:
        if doc_id == i.DID():
            print(i)
    

        
def main():
    
    while True:
        
        print('1. Add Patient')
        print('2. Add Doctor')
        print('3. Add Appointment')
        print('4. Display Patients')
        print('5. Display Doctors')
        print('6. Display Appointments')
        print('7. search Appointments (patient ID)')
        print('8. Search Appointments (doctors ID)')
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
            search_patients()
        elif num == '8':
            search_doctors()
        elif num =='0':
            break
    
main()