from Patient import*
from Doctor import*
from Appointment import*

class Clinic:
    
    def __init__(self):
        self.patientList = []
        self.doctorList = []
        self.appointmentList = []
        
    def addPatient(self,patient):
        self.patientList.append(patient)
        
    def addDoctor(self,doctor):
        self.doctorList.append(doctor)
        
    def addAppointment(self,appointment):
        self.appointmentList.append(appointment)
        
    def displayAllDoctor(self):
        for doctor in self.doctorList:
            doctor.display()
            print()
            
    def displayAllPatient(self):
        for patient in self.patientList():
            patient.display()
            print()
        
    def displayAllAppointment(self):
        for appointment in appointmentList:
            appointment.display()
            print()
            
    def findPatientAppointments(self,patientId):
        for appointment in appointmentList:
            if appoint.patientId == patientId:
                appointment.display()
            else:
                pass
            
    def findDoctorAppointments(self,doctorId):
        for appointment in appointmentList:
            if appoint.doctorId == doctorId:
                appointment.display()
            else:
                pass    
    def defaultDisplay():
        print("0. Quit")
        print("1. Display All Patients admitted to the clinic")
        print("2. Display All Doctors working in the clinic")
        print("3. Display All Appointments in the clinic")
        print("4. Add Patient")
        print("5. Add Doctor")
        print("6. Add Appointment")
        print("7. Find and Display Appointments for a Particular Patient")
        print("8. Find and Display Appointments for a Particular Doctor")
        
    def patientDetails(self):
        patientInputName = input("Enter name: ")
        patientInputAge = int(input("Enter age: "))
        patientInputId =input("Enter patient Id: ")
        patientInputAddress = input("Enter address: ")
        patientInputVisits = int(input("Enter number of visits: "))
        patientObject = Patient(atientInputName,patientInputAge,patientInputId,patientInputAddress,patientInputVisits)
        self.patientList.append(patientObject)
        
    def doctorDetails(self):
            doctorInputName = input("Enter name: ")
            doctorInputAge = int(input("Enter age: "))
            doctorInputId =input("Enter patient Id: ")
            doctorInputAddress = input("Enter address: ")
           
            doctorObject = Patient(doctorInputName,doctorInputAge,doctorInputId,doctorInputAddress)
            self.doctorList.append(doctorObject)
            
    def addAppointment(self):
        doctorInputId = input("Enter patient Id: ")
        patientInputId =input("Enter patient Id: ")
        timeStampInput = input("Enter date and time of the appointment: ")
        memoInput = input("Enter details of the appointment: ")
        appointmentObject = Appointment(doctorInputId,patientInputId,timeStampInput,memoInput)
        self.appointmentList.append(appointmentObject)
        
def main():
    theClinic = Clinic()
    while True:
        theClinnic.defaultDisplay()
        option = input()
        if option == "0":
            print("You have exited the system!")
            break
        elif option == "1":
            theClinic.displayAllPatient()
        elif option =="2":
            theClinic.displayAllDoctor()
        elif option == "3":
            theClinic.displayAllAppointment()
        elif option =="4":
            theClinic.patientDetails()
        elif option == "5":
            doctorDetails
        elif option =="6":
            theClinic.addAppointment()
        elif option =="7":
            patientIdentity = input("Enter Id for the patient: ")
            theClinic.findPatientAppointments(patientIdentity)
        elif option == "8":
            doctorIdentity = input("Enter Id for the doctor: ")
            theClinic.findDoctorAppointments(doctorIdentity)
        else:
            print("No option selected")
            break
            
            
            
            
            
        
        
        
        