"""
The idea of this software is to help 
some medical professionals to manage 
information and processes. We need to create a menu to know which option the doctor wants to choose.
"""

#define the variables to use in the software
patientList = [] #list to store the patients


#functions to use in the software
#function to register a patient
def registerPatient():
    print("Welcome to the patient registration") 
    print("Please enter the patient's name: ")
    patientList = str(input())
    for i in range(0, len(patientList)):
        print(f"Patient: {patientList[i]}")
    
#function to calculate BMI (Body Mass Index)
def calculateBMI():
    print("Welcome to the BMI calculator")
    weight = float(input("Enter the weight in kg: "))
    height = float(input("Enter the height in meters: "))
    bmi = weight / (height ** 2)

#software menu
print("Welcome, doctor!")
print("Please choose an option:")
print("1. Register a patient")
print("2. Calculate BMI (Body Mass Index)")

#create a variable to store the option chosen by the doctor
userOption = int(input("Enter the option number: "))

if userOption == 1:
    #function to register a patient
    print("Register a patient")
elif userOption == 2:
    #function to calculate BMI
    print("Calculate BMI (Body Mass Index)")