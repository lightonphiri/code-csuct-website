# Question 4 - Assignment 1
# ASMSAA002 - Saarah Asmal

from Person import Person
from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment

class Clinic:

    print ("1. add patient")
    print ("2. add doctor")
    print ("3. add appointment")
    print ("4. display all patients")
    print ("5. display all doctors")
    print ("6. display all appointments") 
    print ("7. search for an appointment for a particular patient")
    print ("8. search for an appointment for a particular patient")
    print ("9. Quit")
    option = eval( input("Choose an option from 1-9:")) # menu of options

    patients = [] # empty list to store patients
    doctors = [] # empty list to store doctors
    appointments = [] # empty list to store appointments
    
    display = print (patients,doctors,appointments) #

