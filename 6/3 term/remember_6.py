#variables
name = "Juan" #string always in double quotes
age = 25 #int whole numbers
height = 1.75 #float decimal numbers
is_student = True #bool only use to values: true or false

#keywords
#keywords are reserved words in python and cannot be used as variable names

print("Hello, my name is " + name + ".") #the print function is used to display output

mail = str(input("Enter your email: ")) #input function is used to get user input, str() converts it to a string that means we use the casting function to convert the input to a string

#control structure

if age >= 18: #if statement is used to check a condition
    print("You are an adult.")
else: #else statement is used to execute a block of code if the condition is false
    print("You are a minor.")