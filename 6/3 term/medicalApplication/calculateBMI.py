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