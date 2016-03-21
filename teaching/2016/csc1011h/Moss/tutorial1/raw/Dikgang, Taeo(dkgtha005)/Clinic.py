# Dikgang Thapelo
# Clinic records
# 27-02-2016
 
 
# Importing necessary classes                                                                                
from Patient import Patient                                                     
from Doctor import Doctor
from Appointment import Appointment
import pickle                                                                   

# Creating datastrutures to store patients,Doctors and appointments
patients={}
doctors={}
patient_appointments={'initialKey':[]}   # The appointment datastructure is splited into two and has a list to group multiple appointments that a person might have
doctor_appointments={'initialKey':[]}    # First appointment dictionary item created (later will be deleted) to enable the key and value-of-list pair to exist

# A function to display the menu options
def menu():
    print('1) Patient')
    print('2) Doctor')
    print('3) Appointment')
    print('4) Continue')   
 
# The loop statement asking for user input after the menu has been shown  
while True:
    print('Add a person by entering the value 1,2,3 or Press 4 to continue:')
    menu()
    add=input()     
     
    # Creating and storing a patient object into a patient datastruture 
    if add=='1':
        name=input('Name: ')
        age=input('Age: ')
        ID_number=input('ID number: ')
        address=input('Address: ')        
        number_of_visits=input('Number of visits: ')             
        patients[name]=str(Patient(ID_number,address,number_of_visits,name,age)) 
        print()
        
    # Creating and storing a Doctor object into a Doctor datastruture  
    elif add=='2':
        name=input('Name: ')
        age=input('Age: ')
        ID_number=input('ID number: ')
        address=input('Address: ')              
        doctors[name]=str(Doctor(ID_number,address,name,age))
        print()
        
    # Creating and storing appointments objects into one of the appointments datastruture    
    elif add=='3':
        patient_ID_number=input("Patient's ID number: ")
        doctor_ID_number=input("Doctor's ID number: ")
        timestamp=input('Full timestamp (use a / as a separator): ')
        memo=input('Memo: ') 
        
        # Used a patient or doctor's unique ID number as a key for an object
        # and checking if the Key already exist in the datastructure,and if true, do not replace the Key value but apppend the information, else add the Key
        if patient_ID_number in patient_appointments:       
            patient_appointments[patient_ID_number].append(str(Appointment(patient_ID_number,doctor_ID_number,timestamp,memo))) 
        else:
            patient_appointments[patient_ID_number]=[]
            patient_appointments[patient_ID_number].append(str(Appointment(patient_ID_number,doctor_ID_number,timestamp,memo)))
            
        if doctor_ID_number in doctor_appointments:       
            doctor_appointments[doctor_ID_number].append(str(Appointment(patient_ID_number,doctor_ID_number,timestamp,memo)))                   
        else:
            doctor_appointments[doctor_ID_number]=[]
            doctor_appointments[doctor_ID_number].append(str(Appointment(patient_ID_number,doctor_ID_number,timestamp,memo)))
        print()    
    
    # Writing all datastrutures created into external files before exiting the loop 
    elif add=='4':       
        outFile1=open('Patients.txt','wb')
        pickle.dump(patients,outFile1)
        outFile1.close()
               
        outFile2=open('Doctors.txt','wb')
        pickle.dump(doctors,outFile2)
        outFile2.close()       
        
        outFile3=open('Patient appointments.txt','wb')
        pickle.dump(patient_appointments,outFile3)
        outFile3.close()
               
        outFile4=open('Doctor appointments.txt','wb')
        pickle.dump(doctor_appointments,outFile4)
        outFile4.close()        
      
        break  
    
# Opening all created external files to read the data 
inFile1=open('Patients.txt','rb')   
newPatients_dict=pickle.load(inFile1)

inFile2=open('Doctors.txt','rb')   
newDoctors_dict=pickle.load(inFile2)

inFile3=open('Patient appointments.txt','rb')   
newPatient_appointments_dict=pickle.load(inFile3)

inFile4=open('Doctor appointments.txt','rb')   
newDoctor_appointments_dict=pickle.load(inFile4)

# The loop statement to print all objects in a particular file datastructure  
while True:         
    print('Select 1,2 or 3 to display all members in the category or press 4 to continue ')
    menu()
    display=input()
      
    # printing objects written in a Patient file
    if display=='1':
        for patient in newPatients_dict:               
            print(newPatients_dict[patient])
        print()
        
    # printing objects written in a Doctor file
    elif display=='2':
        for doctor in newDoctors_dict:           
            print(newDoctors_dict[doctor])
        print()
        
     # printing objets written in Appointments files  
    elif display=='3':
        del newPatient_appointments_dict['initialKey'] # Deleting the first Key,which its purpose was to enable the Key-list pair format exist
        for alist in newPatient_appointments_dict:
            for patient_appointment in range(len(newPatient_appointments_dict[alist])):
                print(newPatient_appointments_dict[alist][patient_appointment])                           
        print()
        
    #exiting the loop 
    elif display=='4':
        break      
  
 
# The loop to search and display all appointments for a particular patient or doctor
# Patients or Doctors are identified by their ID numbers
while True:
    search=input("Enter the Patient or doctor ID number to search and display all of his/her appointments or enter the word Quit to exit:"+'\n')
    if search=='Quit':
        break
    
    elif search in newPatient_appointments_dict:                           
        for k in range(len(newPatient_appointments_dict[search])):
            print(newPatient_appointments_dict[search][k]) 
        print()   
        
    elif search in doctor_appointments:
        for p in range(len(newDoctor_appointments_dict[search])):
            print(newDoctor_appointments_dict[search][p])         
        print()  
        
    else:
        print('The Patient or Doctor not found.')

# Closing all opened files
inFile1.close()
inFile2.close()
inFile3.close()
inFile4.close()


    
        