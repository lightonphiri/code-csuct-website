from Person import Person
from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
patient=[]
doctor=[]
appointment=[]
while True:
    print("1: Add patient")
    print("2: Add doctor")
    print("3: Add appointment")
    print("4: Display Patients")
    print("5: Display Doctors")
    print("6: Display appointments")
    print("7: Search")
    print("8: QUIT")
    option=eval(input("Enter the option:"))
    if option==1:
        patnt=Patient()
        patnt.name=input("Enter the patient name:") # name iherited from person
        patnt.age=eval(input("Enter the age of a pateint:")) # age inherited from person
        patnt.idnumber=input("Enter the id number of the patient:") # the patient is given the id number
        patnt.adress=input("Enter the address of a patient:")
        patnt.visit=input("Enter the number of visit:") 
        patient.append(str(patnt)) # The whole patient class is appended into the list
    elif option==2:
        doc=Doctor()
        doc.name=input("Enter the doctor's name:") #The doctor is given the name,address and Id number
        doc.address=input("Enter the address of the doctor:")
        doc.Id=input("Enter the Doctor's ID:")
        doctor.append(str(doc)) # The whole doctor class is aasigned into the list
    elif option==3:
        appoint=Appointment()
        appoint.pid=input("Enter the patient's ID:") #The appointment is assigned doctor's id, when the appointment is and is also assigne the discription of the appointment
        appoint.did=input("Enter the Doctor's ID:") # did=Doctor's id
        appoint.memo=input("Enter the memo:")
        appoint.day=input("Enter the day of the appointment:")
        appointment.append(str(appoint)) # The whole appointment class is assigned to the list
    elif option==4:
        for i in patient: # Going throught Patient list
            print(i)
    elif option==5:
        for i in doctor:
            print(i)
    elif option==6:
        for i in appointment:
            print(i)
    elif option==7:
        doc_id=input("Enter the doctor's ID:")
        p_id=input("Enter your patient's ID:")
        for i in appointment:
            if i[15:26]==doc_id: #Searching for the doctor id and also for the patient id if it is the same then appointment found
                if i[41:55]==p_id:
                    print(i)
                    
    elif option==8:
        break

        
        
        
     