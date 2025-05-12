def diagnosisDetails(diagnosis):
    diagnosisInfo = dict (
        fever = "Temperature above 38 degrees Celsius",
        lab = "Blood test, urine test, or visual inspection",
        treatment = "Rest, hydration, and antipyretics"
    )
    #Validate if the diagnosis is in the dictionary
    if diagnosis in diagnosisInfo:
        print(f"Diagnosis is: {diagnosisInfo[diagnosis]}")
    else:
        print("Diagnosis not found")