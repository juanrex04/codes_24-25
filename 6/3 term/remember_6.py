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

#the conditional statement modify the flow of the programn
if age >= 18: #if statement is used to check a condition
    print("You are an adult.")
else: #else statement is used to execute a block of code if the condition is false
    print("You are a minor.")

#loops structure
#the loops are used to repeat a block of code multiple times
for i in range(5): #for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string)
    print("This is loop iteration number " + str(i) + ".")
    
#comparison operators and logical operators
#comparison operators are used to compare two values and return a boolean result
#logical operators are used to combine multiple conditions
#comparison operators: == (equals to), !=(diffent to), > (greater than), < (less than), >= (greather than or equal to), <=(less than or equal to)
#logical operators: and, or, not

if age >= 18 and is_student == True: #and operator is used to check if both conditions are true
    print("You are an adult student.")
elif age >= 18 or is_student == True: #or operator is used to check if at least one condition is true
    print("You are either an adult or a student.")
else: #not operator is used to negate a condition 
    print("You are neither an adult nor a student.")