#input information/data
number_1 = float(input("Input the first number "))
number_2= float(input("Input another number "))

#process information/data
if number_1 > number_2:
    #print result/data
    print(f"{number_1} is greather than {number_2}")
elif number_2 > number_1:
    print(f"{number_2} is greather than {number_1}")
else:
    print(f"The numbers are the same {number_1}")