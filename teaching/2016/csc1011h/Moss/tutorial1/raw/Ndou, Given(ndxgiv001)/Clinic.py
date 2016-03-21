from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
from Person import Person
import pickle
def main():
    
    patients_list=[] # empty list for saving patients
    doctors_list=[]   # empty list for saving doctors
    appointment_list=[] # empty list for saving appointments
    
    
   
    while True:              #display menu option so that the user can make a choice
        print("0 - to quit")
        print("1 - to add a patient")
        print("2 - to add a Doctor")
        print("3 - to add an appointment.")
        print("4 - display all the patients")
        print("5 - display all the doctors")
        print("6 - display all the appointments")
        print("7 - seach for an appointment of a doctor")
        print("8 - search for an appointment of a patient")
        
        option=int(input("")) # take the option entered by the user
        
        def add_patient(): # add the patient to the system
            patient_name= input("Enter the name of the patient: ")
            id_number=input("Enter the id number of the patient: ") # take the id number as a string in order to slice if to get the age
            number_of_visits=int(input("Enter the number of the visits: "))
            address= input("Enter the address of thr patient: ")
            age= 2016-int('19'+id_number[0:2]) # calculate the age by using the id number of the patient
            patients_list.append(str(Patient(id_number,address,number_of_visits,patient_name,age))) # save the object to the list
            pickle.dump(patients_list,patients_pickle_file) # save the object to the pickle file
        
        
            
    
        def add_doctor(): #add the doctor to the system
            doc_name = input("Enter the name of the Doctor: ")
            doc_address=input("Enter the address of the Doctor: ")
            doc_id=input("Enter the id number of the Doctor: ")
            doc_age=2016-int('19'+doc_id[0:2]) # calculate the age by using the id number of the doctor
            doctors_list.append(str(Doctor(doc_id,doc_address,doc_name,doc_age))) # save the object to the list
            pickle.dump(doctors_list,doctors_pickle_file) # save the object to the pickle file

            
        def add_appointment():  # add the appointments to the system
            pat_id_number= input("Enter the patient's id number: ") # get patient id number
            doc_id_number = input("Enter the Doctor's id number: ")  # doctor id number
            timestamp= input("Enter the appointment time : ")
            memo = input("write what happened at the appointment:\n") # discussed issues in the appointment
            
            
            appointment_list.append(str(Appointment(doc_id_number,pat_id_number,timestamp,memo))) # save the object to the list
            pickle.dump(appointment_list,appointments_pickle_file) # save the object to the pickle file
        
            
        if option ==0:break
        elif option==1:
            patients_pickle_file=open('patients.txt','wb') # create the pickle file
            add_patient()
            patients_pickle_file.close() # close the created pickle file
        elif option==2:
            doctors_pickle_file=open('doctors.txt','wb')
            add_doctor()
            doctors_pickle_file.close() 
           
            
        elif option==3:
            appointments_pickle_file=open('appointments.txt','wb') # create the pickle file
            add_appointment()
            appointments_pickle_file.close() # close the created pickle file
        elif option == 4:
            pickled_patients=open('patients.txt','rb')    # opening the pickled file
            patients=pickle.load(pickled_patients) # loading the contents of the pickled file to a variable
            
            for i in patients:
                print("---------------------------")
                print(i,end='')
                print()
                print("---------------------------")
            
            
            pickled_patients.close() # close the opened pickle file
        elif option == 5:
            pickled_doctors=open('doctors.txt','rb') # opening the pickled file
            doctors=pickle.load(pickled_doctors) # loading the contents of the pickled file to a variable
            for i in doctors:
                print("--------------------------------")
                print(i,end='')
                print()
                print("--------------------------------")
           
            pickled_doctors.close()
                
        elif option == 6:
            pickled_appointments=open('appointments.txt','rb')
            appointments= pickle.load(pickled_appointments)
            for i in appointment:# go to the appointment list and print out the appointments available for a specific Doctor
                print("---------------------------")
                print(i,end='')
                print()
                print("---------------------------")
            
            pickled_appointments.close()
        elif option == 7: # the program is going to print out the appointment details of the doctor but its gng to print out the id instead of the names of the patient and  the doctor
            doc_id = input("Enter the id of the doctor: ") # requesting the user to enter the id of the doctor in order to search for all the available appointments
            for i in appointment_list:
                if i[0:13]==doc_id:
                    print("---------------------------")
                    print(i)
                    print()
                    print("---------------------------")
        elif option == 8:  # the program is going to print out the appointment details of the patient but its gng to print out the id instead of the names of the patient and  the doctor
            pat_id = input("Enter patient ID: ") # requesting the user to enter the id of the patient in order to search for all the available appointments
            for i in appointment_list:
                if i[14:27]==pat_id:
                    print("---------------------------")
                    print(i)
                    print()
                    print("---------------------------")
        else:
            print("Invalid option entered.")
        print()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print()
    
       
       
   
    
    
        
main()