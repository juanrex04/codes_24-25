list_names = ["Juan","Salome","Santiago"]

#print all the info
print(list_names)

#selection an item and print
print(list_names[1])

#change a item
list_names[2] = "Maria Gabriela"
print(list_names)

#checking if the list has a value
if "juan" in list_names:
    print("the value is present in the list")
else:
    print("the value is not in the list")
    
#append a new item
list_names.append("Luciana")
print(list_names)