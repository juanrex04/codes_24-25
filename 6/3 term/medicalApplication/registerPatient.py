def registerPatient():
    print("Welcome to the patient registration")
    continueRegister = "yes"
    patientList = ['Carlos'] 
    while continueRegister.lower() =="yes" or continueRegister.lower() == "y":
        print("-----------------------------------------") 
        print("Please enter the patient's name: ")
        name = str(input())
        patientList.append(name)
        for i in range(0, len(patientList)):
            print(f"Patient #{i + 1}: {patientList[i]}")
        continueRegister = str(input("Do you want to register a patient? (yes/no): "))