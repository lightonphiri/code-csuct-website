# malebo mahoko
# 27 february 2016
# clinic of a certain community

""" Import all classes I am going to use """
from Person import Person
from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment

def main():
    """ three lists to store patients, doctors and appointments """
    patients = []    
    doctors = []
    appointments = []
    
    while True:
        print()
        """ options choose from """
        print("*****Clinic******")
        print("1. To add a patient")
        print("2. To add a doctor")
        print("3. To make an appointment")
        print("4. To display all patients")
        print("5. To display all doctors")
        print("6. To display all appointments")
        print("7. To display appointments for a specific individual (doctor or patient)")
        print("0. To quit")
        
        print()
        
        response = input()                                                              # getting an input from the user
        
        if response == "0": break
        elif response == "1":
            patient = Patient()
            patient.name = input("Enter the name of the patient? \n")
            patient.age = input("Enter age of the patient? \n")
            patient.identity = input("The patients ID number? \n")
            patient.address = input("The patients address? \n")
            patient.number_of_visits = input("The patients number of visits? \n")
            
            patients.append(patient)
            
        elif response == "2":                                           
            doctor = Doctor()                                                           # creating an object variable doctor
            """ getting object variables """
            doctor.name = input("Enter the name of the doctor? \n")
            doctor.age = input("Enter age of the doctor? \n")
            doctor.identity = input("The doctors ID number? \n")
            doctor.address = input("The doctors address? \n")  
            
            doctors.append(doctor)                                                      # appending the object doctor to a list doctors  
            
        elif response == "3":
            appointment = Appointment()
            
            appointment.patients_identity = input("Enter patient's ID number? \n")
            appointment.doctors_identity = input("Enter doctor's ID number? \n")
            appointment.timestamp = input("Enter date and time? \n")
            appointment.memo = input("Enter memorundum of the appointment? \n")
            
            appointments.append(appointment)                                            # adding the oject appointment to list appointments
            
        elif response == "4":
            control = 1
            for item in patients:
                print("Patient No.", control)
                item.display()
                control +=1
                print()
                
        elif response == "5":
            control = 1
            for item in doctors:
                print("Doctor No.", control)
                item.display()
                control +=1
                print()       
                
        elif response == "6":
            for item in appointments:
                print(item)
                print()
            
        
        elif response == "7":
            user_id = input("Enter ID number for which you want to check appointments scheduled? \n ")
            print("Scheduled appointment(s) for", user_id, "are as follows: ")
            """ looping through the list appointment and comparing id's"""
            for item in appointments:
                if user_id == item.patients_identity:
                    print(item.timestamp)
                
                elif user_id == item.doctors_identity:
                    print(item)
                    
        else:
            print("The value entered is not in the option manu.")
            print("Please enter value available in the menu")
            
main()
        