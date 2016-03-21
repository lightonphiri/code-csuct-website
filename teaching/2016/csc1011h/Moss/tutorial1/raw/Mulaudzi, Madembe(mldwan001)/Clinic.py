# Question 4 and 5
# Wanga Mulaudzi
# 22 February 2016

from Person import Person
from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
import datetime
import pickle

# Create menu for the clinic
def menu():
    print("======== Clinic ========")
    print("Enter number: ")
    print("1. Add patient")
    print("2. Add doctor")
    print("3. Add appointment")
    print("4. Display patients")
    print("5. Display doctors")
    print("6. Display appointments")
    print("7. Search")
    print("8. Quit")

def main():
    # Initialise lists that are needed
    patients = []
    doctors = []
    appointments = []
    
    while True:
        menu()
        
        # Obtain input from user
        option = int(input(""))
        
        if option == 8:
            break
        
        # Collect information from user and store as a patient object
        elif option == 1:
            patient_name = input("Enter the patient's name: ")
            patient_age = input("Enter the patient's age: ")
            patient_ID = input("Enter the patient's ID: " )
            patient_address = input("Enter the patient's address: ")
            patient_visits = int(input("Enter the patient's number of visits: "))
            
            patient = Patient(patient_name, patient_age, patient_ID, patient_address, patient_visits)
            patients.append(patient)
        
        # Collect information from user and store as a doctor object    
        elif option == 2:
            doctor_name = input("Enter the doctor's name: ")
            doctor_age = input("Enter the doctor's age: ")
            doctor_ID = input("Enter the doctor's ID: ")
            doctor_address = input("Enter the doctor's address: ")
            
            doctor = Doctor(doctor_name, doctor_age, doctor_ID, doctor_address)
            doctors.append(doctor)
        
        # Collect information from user and store as an appointment object    
        elif option == 3:
            patient_ID = input("Enter the patient's ID: ")
            doctor_ID = input("Enter the doctor's ID: ")
            time_stamp = datetime.datetime.now()
            memo = input("Enter the memo: ")
            
            appointment = Appointment(patient_ID, doctor_ID, time_stamp, memo)
            appointments.append(appointment)
        
        # Display patients    
        elif option == 4:
            for i in patients:
                print(i)
        
        # Display doctors        
        elif option == 5:
            for i in doctors:
                print(i)
        
        # Display appointments        
        elif option == 6:
            for i in appointments:
                print(i)
        
        # Search for a doctor or a patient        
        elif option == 7:
            opt = input("Enter 'd' to search for a doctor or 'p' to search for a patient: ")
            
            if opt == 'd':
                ID = input("Enter the doctor's ID: ")
                for i in doctors:
                    if i.doctor_number == ID:
                        for n in appointments:
                            if n.doctor_ID == ID:
                                print(n)
                        
            elif opt == 'p':
                ID = input("Enter the patient's ID: ")
                for i in patients:
                    if i.patient_number == ID:
                        for z in appointments:
                            if z.patient_ID == ID:
                                print(z)
    
    # Pickle all the data that was obtained                     
    PatientsFile = open('PicklePatients.txt', 'wb')
    pickle.dump(patients, PatientsFile)
    PatientsFile.close()
    
    DoctorsFile = open('PickleDoctors.txt', 'wb')
    pickle.dump(doctors, DoctorsFile)
    DoctorsFile.close()
    
    AppointmentsFile = open('PickleAppointments.txt', 'wb')
    pickle.dump(appointments, AppointmentsFile)
    AppointmentsFile.close()    
    
main()