# Clinic programme - OOP
# Simphiwe Mchunu
# 28 february 2016

from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
from Person import Person
import datetime


patients = []
doctors = []
appointments = []
search_patient = {}
search_doctor = {}


while True:
    print("********Clinic's Menu Based System********")
    print("1.Add patient."+'\n'+'2.Add doctor.'+'\n'+'3.Add appointment.'+'\n'+'4.Display all patients.'+'\n'+'5.Display all doctors.'+'\n'+'6.Display all appointments.'+'\n'+'7.Search and display all appointments for a particular patient or doctor.'+'\n'+'9.Quit.')

    input_option = int(input('>>'))
    
    if input_option == 1:
        '''Option to add patient to list'''
        name = input('Enter name: ')
        age = input('Enter age: ')
        patient_id = input('Enter ID number: ')
        address = input('Enter address: ')
        visits = input('Enter number of visits: ')
        patient = Patient(name,age,patient_id,address,visits)
        patients.append(patient)
        
    elif input_option == 2:
        '''Option to add doctor to list'''
        name = input('Enter name: ')
        age = input('Enter age: ')
        doctor_id = input('Enter ID number: ')
        address = input('Enter address: ')
        doctor = Doctor(name,age,doctor_id,address)
        doctors.append(doctor)
        
    elif input_option == 3:
        '''Date of the appointment'''
        patient_id = eval(input("Enter Patient's ID number: "))
        doctor_id = eval(input("Enter Doctor's ID number: "))
        year = int(input('Enter year : '))
        month = int(input('Enter month: '))
        day = int(input('Enter day: '))
        '''Time of the appointment'''
        hour  = eval(input('Enter hours : '))
        minutes = eval(input('Enter minutes: '))
        seconds = eval(input('Enter seconds: '))
        memo = input('Enter appointment memo: ')
        timestamp = datetime.datetime(year,month,day,hour,minutes,seconds)
        appointment = Appointment(patient_id,doctor_id,timestamp)
        appointments.append(appointment)

    elif input_option == 4:
        '''Display all patients'''
        for i in patients:
            print(i.display())
    
    elif input_option == 5:
        '''Display all doctors'''
        for i in doctors:
            print(i.display())
        
    elif input_option == 6:
        '''Displays all appointments'''
        for k in appointments:
            print(k.display())
    elif input_option == 7:
        '''Search for and display all appointments for a particular doctor or patient'''
        print('1.Search and display all appointments for a particular patient.'+'\n'+'2.Search and display all apointments for a particular doctor.')
        option2 = int(input('>>'))
        if option2==1:
            '''Search for and display all appointments for a particular patient'''
            patient2 = int(input("Enter patient's ID number: "))
            for k in appointments:
                if k.PatientID==patient2:
                    print(k.display())
                else:
                    print('No appointment made')
        elif option2==2:
            '''Search for and display all appointments for a particular doctor'''
            doctor2 = int(input("Enter doctor's ID number: "))
            for i in appointments:
                if i.DoctorID==doctor2:
                    print(i.display())
                else:
                    print('No appointment made')
                    
    elif input_option == 9:
        '''Termination of loop'''
        break
    else:
        '''Termination of loop if option out of boundary'''
        break

        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
