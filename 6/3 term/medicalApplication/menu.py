#import the functions to use in the software
from registerPatient import registerPatient
from calculateBMI import calculateBMI
from diagnosis import diagnosisDetails

#software menu
print("Welcome, doctor!")
print("Please choose an option:")
print("1. Register a patient")
print("2. Calculate BMI (Body Mass Index)")
print("3. Generate a diagnosis")
#create a variable to store the option chosen by the doctor
userOption = int(input("Enter the option number: "))

if userOption == 1:
    #function to register a patient
    print("Register a patient")
    registerPatient()
elif userOption == 2:
    #function to calculate BMI
    print("Calculate BMI (Body Mass Index)")
    calculateBMI()
elif userOption == 3:
    #Give a diagnosis to a patient
    print("Give a diagnosis to a patient")
    diagnosis = str(input("Choose a diagnosis: fever, lab, treatment: "))
    diagnosisDetails(diagnosis)
else: 
    print("Invalid option")
