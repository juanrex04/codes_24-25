"""
Calculate the age of a person storing the birth date, but separating 
the year according to the current year.

The program will ask to the user for the birth date, for separate but when print the message must concatenate the day, month and year.
"""

import datetime #library to work with dates

date = datetime.datetime.now().year #get the current year

print(f"Current date: {date}")

userDate = str(input("Enter your birth date (dd/mm/yyyy): ")) #ask the user for the birth date

day, month, year = userDate.split("/")

if int(year) > date: #check if the year is greater than the current year
    print("The year that you enter is greater than the current year")
elif len(userDate) < 8 or len(userDate) >= 9: #check if the length of the date is less than 8 or greater than 9, we use the method len() to check the length of the string
    print("The date that you enter has a length less than 8 or greater than 9")
    
calculatedAge = date - int(year) #calculate the age by subtracting the year pass for the user of the current year

print(f"Your birth date is {userDate} and your age is {calculatedAge} years") 
#print the date and the age of the user
