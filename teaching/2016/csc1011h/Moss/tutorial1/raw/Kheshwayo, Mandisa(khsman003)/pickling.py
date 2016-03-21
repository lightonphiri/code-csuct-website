import pickle #importing pickle

from Patient import Patient
from Doctor import Doctor               #importing all the other classes
from Appointment import Appointment

p=Patient()
d=Doctor()
a=Appointment()     #assigning the classes so i can use them in the file

outfile=open('Pickle.txt','wb') #creating a pickle file 

pickle.dump([p,d,a],outfile)
#pickle.dump(d,outfile)     #putting the classes in the file
#pickle.dump(a,outfile)        

outfile.close() #closing the file

#part 2 of the program 

infile=open('pickle.txt','rb')  #opening the pickle inorder to read it
new_file=pickle.load(infile)    #getting objects from the file
infile.close()
