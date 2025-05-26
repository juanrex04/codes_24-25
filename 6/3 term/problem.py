#varible that will let know if the user want to repeat the process
repeat = str("yes")

while repeat == "yes":
    numberUser = int(input("Input the number you want: "))
    
    for x in range(2,11):
        print(f"The result for {numberUser} x {x} is: {numberUser*x}")

    repeat = str(input("Do you want to repeat the process? write yes or no: "))