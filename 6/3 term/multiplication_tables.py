""" 
The next code will help us to print a multiplication table for a given number; according to the number that the user enters, the program must print the multiplication table from 1 to 10.
"""

#Get the user input (number to use for the multiplication table)
user_number = int(input("Enter a number to print its multiplication table: "))

#Print the multiplication table according to the number of the user to use from 1 to 10
for i in range(1, 11): #the range function will manage the operation from 1 to 10
    result = user_number * i #the result of the multiplication will be stored in the variable result
    print(f"{user_number} x {i} = {result}")#the print function will display the result of the multiplication in a formatted way using f-string