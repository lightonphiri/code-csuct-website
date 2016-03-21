# Clinic.py (question 4)
# mantombi manqele
# 21/02/2016

from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
from datetime import datetime


patients = []
doctors = []
appointments = []

def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    patient_id = int(input("Enter patient ID number: "))
    patient_address = input("Enter patient address: ")
    visits = int(input("Enter patient visits: "))
    p = Patient(name, age, patient_id, patient_address, visits)
    patients.append(p)
    
def add_doctor():
    name = input("Enter doctor name: ")
    age = int(input("Enter doctor age: "))
    doctor_id = int(input("Enter doctor ID number: "))
    doctor_address = input("Enter doctor address: ")
    d = Doctor(name, age, doctor_id, doctor_address)
    doctors.append(d)
    
def add_appointment():
    timestamp = datetime.now()
    patient_id = int(input('Enter patient ID: '))
    doctor_id = int(input('Enter doctor ID: '))
    memo = input('Enter memo: ')
    a = Appointment(patient_id, doctor_id, timestamp, memo)
    appointments.append(a)

def main():
    while True:
        print('***************** Clinic System *****************')
        print('0. Add a patient.')
        print('1. Add a doctor.')
        print('2. Add an appointment.')
        print('3. Display all patients.')
        print('4. Display all doctors.')
        print('5. Display all appointments.')
        print('6. Display appointment for a particular patient.')
        print('7. Display appointment for a particular doctor.')
        print('8. Quit.')
        option = int(input('Enter number of chosen option (0 to 8): '))
        
        if option == 0:
            add_patient()
        elif option == 1:
            add_doctor()
        elif option == 2:
            add_appointment()
        elif option == 3:
            for i in patients:
                print(i)
        elif option == 4:
            for i in doctors:
                print(i)
        elif option == 5:
            for i in appointments:
                print(i)
        elif option == 6:
            patient = int(input('Enter patient ID: '))
            for i in appointments:
                if patient == i.patient_id:
                    print(i)
        elif option == 7:
            doctor = int(input('Enter doctor ID: '))
            for i in appointments:
                if doctor == i.doctor_id:
                    print(i)
        elif option == 8:
            break
        
main()

# pickled program (question 5)
# mantombi manqele 
# 25/02/2016

import pickle

def main():
    while True:
        print('***************** Clinic System *****************')
        print('0. Add a patient.')
        print('1. Add a doctor.')
        print('2. Add an appointment.')
        print('3. Display all patients.')
        print('4. Display all doctors.')
        print('5. Display all appointments.')
        print('6. Display appointment for a particular patient.')
        print('7. Display appointment for a particular doctor.')
        print('8. Quit.')
        option = int(input('Enter number of chosen option (0 to 8): '))
        
        if option == 0:
            add_patient()
        elif option == 1:
            add_doctor()
        elif option == 2:
            add_appointment()
        elif option == 3:
            for i in patients:
                print(i)
        elif option == 4:
            for i in doctors:
                print(i)
        elif option == 5:
            for i in appointments:
                print(i)
        elif option == 6:
            patient = int(input('Enter patient ID: '))
            for i in appointments:
                if patient == i.patient_id:
                    print(i)
        elif option == 7:
            doctor = int(input('Enter doctor ID: '))
            for i in appointments:
                if doctor == i.doctor_id:
                    print(i)
        elif option == 8:
            break
        
f1 = open('patients.txt', 'wb')
f2 = open('doctors.txt', 'wb')
f3 = open('appointments.txt', 'wb')

pickle.dump(f1, patients)
pickle.dump(f2, doctors)
pickle.dump(f3, appointments)

f1.close()
f2.close()
f3.close()
