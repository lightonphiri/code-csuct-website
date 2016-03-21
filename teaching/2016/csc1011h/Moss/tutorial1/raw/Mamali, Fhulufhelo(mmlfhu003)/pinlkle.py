import pickle
from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
c=open("c.txt","wb") # c=Clinic file. Opening the list to save clinic information from question 4
patient=[]
doctor=[]
appointment=[]
while True:
    l=["1: Add patient","2: Add doctor","3: Add appointment","4: Display Patients","5: Display Doctors","6: Display appointments","7: Search","8: QUIT"]
    for i in l:
        print(i)
    option=eval(input("Enter the option: "))
    if option==0:
        pickle.dump(patient,c) # Dumping the patient's list in to the clinic file
        pickle.dump(doctor,c) # Dumping the Doctor's list into the clinic file
        pickle.dump(appointment,c) # writing the appointment's list into the clinic file
        break
    elif option==1:
        patnt=Patient()
        patnt.name=input("Enter the patient name:")
        patnt.age=eval(input("Enter the age of a pateint:"))
        patnt.idnumber=input("Enter the id number of the patient:")
        patnt.adress=input("Enter the address of a patient:")
        patnt.visit=input("Enter the number of visit:")
        patient.append(str(patnt))
    elif option==2:
        doc=Doctor()
        doc.name=input("Enter the doctor's name:")
        doc.address=input("Enter the address of the doctor:")
        doc.Id=input("Enter the Doctor's ID:")
        doctor.append(str(doc))
    elif option==3:
        appoint=Appointment()
        appoint.pid=input("Enter the patient's ID:")
        appoint.did=input("Enter the Doctor's ID:")
        appoint.memo=input("Enter the memo:")
        appoint.day=input("Enter the day of the appointment:")
        appointment.append(str(appoint))
    elif option==4:
        for i in patient:
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
            if i[15:26]==doc_id:
                if i[41:55]==p_id:
                    print(i)  

c.close() # closing clinic file