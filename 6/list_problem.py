""" 
an enterprise needs to store the names of their employees 
to organize the information and manage in case that 
they need. At the moment that they need to manage the 
information we need to keep in mind:

1.the names must stored in a list
2.show a menu to manage the list and know what the user 
needs to do
3.the program must do all operations that appear in the 
menu
4.the process to manage the list must repeat until the user
wants

the menu is:
1.input a new value in last position
2.input a new value in a specific position
3.remove a value in last position
4.remove a value using the index
5.remove a value using the item
6.print the list
7.close the program (y/n)
"""

repeat = str("y")
names_enterprice = ["Juan"]

#function to add new item last position
def new_item_last_position(newValue):
    names_enterprice.append(newValue)
    print (names_enterprice)
    print("-------------------------------------")
    
#function to add a new item in a specified position
def new_item_specified_position():
    print(names_enterprice)
    newValue = str(input("Input the value that you want"))
    position = int(input("Now, write which position do you want"))
    names_enterprice.insert(position, newValue)
    print("-------------------------------------") 

while repeat == "y":
    option = str(input("What option do you want? \n1.Input a new value in the last position \n2.Input new value specific position \n3.Remove a value in last position \n4.Remove a value using the index \n5.Remove a value using the item \n6.Print the list \n7.Close the program (y/n) \n"))
    print("-------------------------------------")   
    
    if option == "1":
        newValue = str(input("Input a new value for last position ")) 
        new_item_last_position(newValue)
    elif option == "2":
        new_item_specified_position()