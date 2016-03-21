# Ntwanano Mazibuko
# 29 February 2016

from Person import Person
from Doctor import Doctor
from Patient import Patient
from Appointment import Appointment

from pickle import *
#datatypes to store information required by the clinic
doctors = {}
patients = {}
appointments = {}
patient_appointments= {}
doctor_appointments= {}
Appointment_number=0

#options available to choose from
def intro():
    print('Clinic System:')
    print('0. Quit.')
    print('1. Input Patient')
    print('2. Input Doctor')
    print('3. Input Appointment.')
    print('4. Enrol Patient to Appoinment.')
    print('5. Assign Appointment to Doctor.')
    print('6. Find Appointment.')
    print('7. Find Doctor.')
    print('8. Find Patient.')
    print('9. Display Appointments.')
    print('10. Display Doctors.')
    print('11. Display Patients.')

#function to iterate over datatype info
def display_dictionary_values(subject):
    for i in subject:
        item=subject[i]
        item.display()
    
def main():    
    input_file=open('Outputs.txt','wb') #opens file to save input
    while True:
        intro() #calls options
        
        option=int(input('>'))
    
        if option== 0: #ceases operation
            data_files=[doctors,patients,appointments,doctor_appointments,patient_appointments]
            dump(data_files, input_file)
            input_file.close()
            break
        
        elif option== 1: #inputs patient's info
            patient=Patient()
            patient.id_input()
            patients[patient.pat_id_number]=patient
            
        elif option== 2: #inputs for doctor's info
            doctor=Doctor()
            doctor.input()
            doctors[doctor.doc_id_number]=doctor
            
        elif option== 3: #inputs appointment info
            Appointment_number+=1
            appointment=Appointment()
            appointment.input()
            appointments[Appointment_number]=appointment
            
        elif option== 4: #searchs for patient
            pat_id_number=input('Enter Patient\'s Id number: ')
            appointment=Appointment()
            appointment.input()
            
            if len(patient.pat_id_number)>0:
                for i in patients:
                    if pat_id_number == i:
                        patient_appointments[pat_id_number]=appointment
                print('Could not find a patient with that Id number.')
        
            else:
                print('Could not find a patient with that student number.')
     
        elif option== 5: #searchs for doctor
            doc_id_number=input('Enter Doctor\'s Id number: ')
            appointment=Appointment()
            appointment.input()
            
            if len(doctor.doc_id_number)>0:
                for i in doctors:
                    if doc_id_number == i:
                        doctor_appointments[doc_id_number]=appointment
                print('Could not find a doctor with that Id number.')
        
            else:
                print('Could not find a doctor with that id number.')
                
        elif option== 6: #searchs for appointment
            Appointment_number=int(input('Enter Appointment number: '))
            appointment=Appointment()
            appointment.input()
            
            if len(appintment_number)>0:
                for i in appointments:
                    if Appointment_number == i:
                        appointments[Appointment_number]=appointment
                print('Could not find an appointment with that appointment number.')
        
            else:
                print('Could not find an appointment with that appointment number.')                       
        
        elif option== 7: #finds doctor
            doc_id_number=input('Enter Doctor\'s Id number: ')
            
            if doc_id_number in doctors:
                print(doctors[doc_id_number])
                
            else:
                print('Could not find a doctor with that id number.')
            
        elif option== 8: #finds patient
            patient_id_number=input('Enter Patient\'s Id number: ')
            
            if len(patient_id_number)>0:
                for ptt in patients:
                    if patient_id_number==ptt:
                        print(patients[patient_id_number])
                print('Could not find a patient with that id number.')
            else:
                print('Could not find a patient with that id number.')
        
        elif option== 9: #displays all appointments
            display_dictionary_values(appointments)
        
        elif option== 10: #displays all doctors
            display_dictionary_values(doctors)
        
        elif option== 11: #displays all patients
            display_dictionary_values(patients)
        
        else: #printed when option is not found
            print('That selection was not recognised.')

main()