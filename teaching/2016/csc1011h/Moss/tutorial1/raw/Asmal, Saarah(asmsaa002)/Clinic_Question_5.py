# Question 5 - Assignment 1
# ASMSAA002 - Saarah Asmal

from Person import Person
from Patient import Patient
from Doctor import Doctor
from Appointment import Appointment
import pickle

# only one element can be placed in a pickled file

patients = []
doctors = [] 
appointments = []

outFile = open ('clinic.txt', 'wb')

pickle.dump(patients, outFile)
pickle.dump(doctors, outFile)
pickle.dump(appointments. outFile)

outFile.close()