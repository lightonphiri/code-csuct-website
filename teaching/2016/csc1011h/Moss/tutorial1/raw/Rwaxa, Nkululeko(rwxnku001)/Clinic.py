from Appointment import Appointment
from Doctor import Doctor
from Patient import Patient
import pickle

patient_details=[]  #List of all the patients.
patient_dict={}     # Store information accoding to the ID number.
patient_appmnt_dict={}
doctor_details=[]   #List of all the doctors.
doctor_dict={}
doctor_appmnt_dict={}
appointment_details=[]#List of all the appointments.
appointment_dict={}
pickle_file_list=[] #List of all the information to be pickled.
def main():
    while True:
        print()
        print("*****Clinic Administration System*****")
        print()
        print("Option 1: Add patient.")
        print("Option 2: Add doctor.")
        print("Option 3: Add appointment.")
        print("Option 4: Display all the patients.")
        print("Option 5: Display all the doctors.")
        print("Option 6: Display all the appointments.")
        print("Option 7: Search and display patient's appointments.")
        print("Option 8: Search and display doctor's appointments.")
        print("Option 9: Quit.")
    
        option = int(input("Enter your option: "))
        
        if option==1:
            try:
                name=input("Enter the patient's name: ")
                age=int(input("Enter the patient's age: "))
                Id=int(input("Enter the patient's ID number: "))
                address=""
                for i in range(5):
                    ad=input("Enter line "+str(i+1)+" of the address: ")
                    address+=ad+" "
            except ValueError:
                print("ERROR:Enter the correct required information.")
            else:
                if len(str(Id))==13:
                    patient=Patient(name,age,Id,address)
                    patient=str(patient)                
                    patient_details.append(patient)
                    pickle_file_list.append(patient)    #Add the entered info for pickling    
                    patient_dict[Id]=patient
                else:
                    print("Invalid ID Number.")
                    break
                
        elif option==2:
            try:
                name=input("Enter the doctor's name: ")
                age=int(input("Enter the doctor's age: "))
                Id=int(input("Enter the doctor's ID number: "))
                address=""
                for i in range(5):
                    ad=input("Enter line "+str(i+1)+" of the address: ")
                    address+=ad+" "
            except ValueError:
                print("ERROR:Enter the correct required information.")
            else:
                if len(str(Id))==13:
                    doctor=Doctor(name,age,Id,address)
                    doctor=str(doctor)
                    doctor_details.append(doctor)
                    pickle_file_list.append(doctor) #Add the entered info for pickling
                    doctor_dict[Id]=doctor
                else:
                    print("Invalid ID Number.")
                    break
                
        elif option==3:
            try:
                patient_id=int(input("Enter the patient's ID number: "))
                doctor_id=int(input("Enter the doctor's ID number: "))
                appmnt_descpt=input("What was the appointment for: ")
            except:
                print("ERROR:Enter the correct required information.")
            else:
                if len(str(patient_id))==13 and len(str(doctor_id))==13:
                    ans=Appointment(patient_id,doctor_id,appmnt_descpt)
                    ans=str(ans)
                    appointment_details.append(ans)
                    pickle_file_list.append(ans)    #Add the entered info for pickling
                    patient_appmnt_dict[patient_id]=appointment_details
                    doctor_appmnt_dict[doctor_id]=appointment_details
                else:
                    print("Make sure your ID Numbers are 13 digits.")
            
            
        elif option==4:
            for i in patient_details:
                print(i)
        
        elif option==5:            
            for i in doctor_details:
                print(i)
                
        elif option==6:
            for i in appointment_details:
                print(i)
                
        elif option==7:
            Id_number=int(input("Enter the patient's ID number: "))
            if len(str(Id_number))==13:
                if Id_number in patient_appmnt_dict:
                    print(patient_appmnt_dict[Id_number])
                else:
                    print("This patient has no appointment.")
            else:
                print("Invalid ID Number.")
                break
        
        elif option==8:
            Id_number=int(input("Enter the doctor's ID number: "))
            if len(str(Id_number))==13:
                if Id_number in doctor_appmnt_dict:
                    print(doctor_appmnt_dict[Id_number])
                else:
                    print("This doctor has no appointment.")
            else:
                print("Invalid ID Number.")
                break
        else:
            pickle_out=open("dict.pickle","wb")
            pickle.dump(pickle_file_list,pickle_out)    #Pickle everything.
            pickle_out.close()
            break
main()
            
        