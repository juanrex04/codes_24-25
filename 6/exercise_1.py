"""A restaurant needs to validate when a user is an adult or a child
for that reason they decide to hire you to create the software;
create a software that validate when an user is adult or child when 
this input them age; in case that user show an invitation will has a
discount of 20% when is an adult"""

age = int(input("What is your age: "))
invitation = input("Do you have an inventation? ")

if age >= 21 and invitation == "yes":
    print("You are an adult and have a 20 porcentage discount")
elif age >= 21:
    print("You are an adult")
else:
    print("You are a child")