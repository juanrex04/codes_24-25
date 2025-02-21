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

while repeat == "y":
    option = int(input("What option do you want?"))