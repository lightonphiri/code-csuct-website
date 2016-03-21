# A program to handle a clinic database
# Wesley Herman
# HRMWES003

from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
from datetime import datetime



def main():
    # store data
    patient_lst = []
    doctor_lst = []
    app_lst = []
    print("Welcome to the clinic database.")
    while True:
        # user choice
        user = input("Choose an option:\n1. Add info.\n2. Display all info.\n3. Search for info.\n[q to quit]\n")
        if user=="q":
            break
        # adding data
        
        elif user == "1":
            user_add = input("Choose a catagory to add:\n1. Add patient info.\n2. Add Doctor's info.\n3. Add an appointment.\n")
            # patient data
            if user_add =="1":
                patient_name = input("Enter patient's name: ")
                patient_age = input("Enter patient's age: ")
                patient_id = input("Enter patient's ID: ")
                patient_address = input("Enter patient's address: ")
                patient_visits = input("Enter number of patient visits: ")
                a = Patient(patient_name, patient_age, patient_id, patient_address, patient_visits)
                patient_lst.append(a)  
                
            # doctor data
            elif user_add == "2":
                doctor_name = input("Enter doctor's name: ")
                doctor_age = input("Enter doctor's age: ")
                doctor_id = input("Enter doctor's ID: ")
                doctor_address = input("Enter doctor's address: ")
                b = Doctor(doctor_name, doctor_age, doctor_id, doctor_address)
                doctor_lst.append(b)
                
            # appointment data
            elif user_add == "3":
                p_id = input("Enter patient's ID: ")
                d_id = input("Enter doctor's ID: ") 
                x = input("Enter date [MMM DD YYYY  hh:mm(12h)]: ")
                # timestamp
                app_time = datetime.strptime(x , '%b %d %Y %I:%M%p')
                memo = input("Enter any notes: ")
                c = Appointment(p_id, d_id, app_time, memo)
                app_lst.append(c)
                
        # display data
        if user == "2":
            user_display = input("Choose info to display:\n1. Patient info.\n2. Doctor's info.\n3. Appointments.\n")
            # display patients
            if user_display == "1":
                for i in patient_lst:
                    i.display()
            # display doctors
            elif user_display =="2":
                for i in doctor_lst:
                    i.display()
            # display appointments
            elif user_display =="3":
                for i in app_lst:
                    i.display()
        
        # search option            
        if user =="3":
            search = input("Enter Patient or Doctor's ID: ")
            #app_lst(search))
            
main()