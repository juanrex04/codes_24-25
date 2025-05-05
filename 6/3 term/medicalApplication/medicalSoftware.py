"""
The idea of this software is to help 
some medical professionals to manage 
information and processes. We need to create a menu to know which option the doctor wants to choose.
"""

#define the variables to use in the software
patientList = [] #list to store the patients
diagnosisDetails = dict( 
    fever = "Temperature above 38 degrees Celsius"
)

#functions to use in the software
#function to register a patient
def registerPatient():
    print("Welcome to the patient registration") 
    print("Please enter the patient's name: ")
    global patientList 
    name = str(input())
    patientList.append(name)
    for i in range(0, len(patientList)):
        print(f"Patients: {patientList[i]}")


#function to calculate BMI (Body Mass Index)
def calculateBMI():
    print("Welcome to the BMI calculator")
    weight = float(input("Enter the weight in kg: "))
    height = float(input("Enter the height in meters: "))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print(f"Your BMI is {bmi:.2f}, you are underweight")
    elif bmi >= 18.5 and bmi <= 24.9:
        print(f"Your BMI is {bmi:.2f}, you have a normal weight")
    elif bmi >= 25 and bmi <= 29.9:
        print(f"Your BMI is {bmi:.2f}, you have overweight")
    elif bmi >= 30:
        print(f"Your BMI is {bmi:.2f}, you have obesity")

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
    registerPatient()
elif userOption == 2:
    #function to calculate BMI
    print("Calculate BMI (Body Mass Index)")
    calculateBMI()