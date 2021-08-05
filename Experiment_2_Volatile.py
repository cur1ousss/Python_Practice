# ***************************************************************************** 
student={"name":"Ramlal","age":52,"courses":["Hindi","Math"]}

# Keys can be Strings and Integers and more ..
print(student)
print(student["name"]) # Prints the Value Associated with Key

dict1={1:"one",2:"two"}	# Keys can also be Integers
print(dict1)
print(dict1[1])

# If Key does'nt exist we get KeyError and prints Stack To Avoid this Stack Error use get() Method

print(dict1.get(3)) # Prints "None" if key does'nt exist instead of Error Stack
print(dict1.get(3,"Custom Not Found Message"))


# Modifying Dict

student={"name":"Ramlal","age":52,"courses":["Hindi","Math"]}

student={"phone":"8198-19283"}	# Adding New Key to dict

student={"name":"Updated Name"} # Updating KeyValue

# using Update() method for updating Multiple things in 1 shot
# update() can update current KeyValues and Add more Key and Values

student.update({"name":"Updated Name","age":100,"newKey":"value vakye"})
print(student)

# Delete Key
del student["newKey"]

# Pop() value out of dict
	# Pop Removes Element from dict and Returns it
age=student.pop("age")
print(age)	
dict1={"name":"ramasnd","age":23}
print(dict1)
