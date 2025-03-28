list_names = ["Juan","Salome","Santiago"]

#print all the item
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
    
#append a new item in the last position
list_names.append("Luciana")
print(list_names)

#insert a new item in a specified position
list_names.insert(2, "Samuel")
print(list_names)

#remove a specifed item (value)
list_names.remove("Juan")
print(list_names)