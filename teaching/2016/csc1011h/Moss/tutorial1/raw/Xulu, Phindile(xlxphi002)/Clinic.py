# Program to search, add or display patient, doctor or appointment
#Phndile Xulu
#28/02/2016

from Person import Person
from Doctor import Doctor
from Patient import Patient
from Appointment import Appointment
import datetime

def main():
    patients,doctors,appointments=[],[],[]
    while True:
        print("Welcome to the Clinic. Please select an option:\n")
        option=int(input("1.Add a doctor, patient or create an appointment.\n2.Search and dispay all patients, doctors or appointments.\n3.Search all appointments for a patient or a doctor.\n0.Quit.\n"))
        if option==0:break
        
        elif option==1:                                                                 
            option1=int(input("1.Add a doctor.\n2.Add Patient.\n3.Create appointment.\n"))
            if option1==1:                                                              #Adding a doctor
                d=Doctor()
                d.name=input("Please enter doctor's name.\n")
                d.age=input("Please enter doctor's age.\n")
                d.doctor_id_no=input("Please enter doctor's I.D number.\n")
                d.doctor_address=input("Please enter doctor's address.\n")
                doctors.append(d)
            elif option1==2:                                                            #Adding patient
                p=Patient()
                p.name=input("Please enter patient's name.\n")
                p.age=input("Please enter patient's age.\n")
                p.patient_id_no=input("Please enter patient's I.D number.\n")
                p.patient_address=input("Please enter patient's address.\n")
                patients.append(p)
            elif option1==3:                                                            #creating an appointment
                a=Appointment()
                a.doc_id=input("Please enter doctor's I.D number.\n")
                a.pat_id=input("Please enter patient's I.D number.\n")
                a.time=input("Please enter date and time for the appointment(yyyy/mm/dd hh:mm)\n")
                a.memo()
                appointments.append(a)
        elif option==2:
            option2=int(input("1.Display doctors.\n2.Display patients.\n3.Display appointments.\n"))
            if option2==1:
                for i in doctors:
                    print(i.display())
            elif option2==2:
                for i in patients:
                    print(i.display())
            elif option2==3:
                for i in appointments:
                    print(i.display())
        elif option==3:
            option3=int(input("1.Search for doctor's appointments.\n2.Search for patient's appointments"))
            if option3==1:
                doctor_id=input("Enter doctor's I.D number")
                for i in doctors:
                    if i.doctor_id_no==doctor_id:
                        print(i.name)
                        break
                for j in doctors:
                    for k in appointments:
                        if j.doctor_id_no==k.doc_id:
                            print(k.display())
                
            elif option3==2:
                patient_id=input("Enter patient's I.D number")
                for i in doctors:
                    if i.patient_id_no==patient_id:
                        print(i.name)
                        break
                    for j in patients:
                        for k in appointments:
                            if j.patient_id_no==k.pat_id:
                                print(k.display())  
                                
main()        