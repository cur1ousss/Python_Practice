# print Multiple Lines String
message="""multiple lines which contain [enter] using 
3 quotes end start"""   

# Prepared to sleep through the storm 


# Using special characters like ' " conflicting with string " definition"
message="escape character single quotes using backslash(\) \" some slashed"
message2='string with single quote \' use escape character(\)'
print(message2)

print(message)
print(message[40])  # out of Range error Possible
print(len(message)) # print Length of String
print(message[0:6]) # print Range of String  | for single string print(string[0:len]) since last term after : not inclusive | second index not inclusive
print(message[:6]) # First index empty meaning from starting index
print(message[6:]) # Second index empty means till Last
print(message.upper()) # string.lower() || string.upper() for lowercase uppercase
print(message.count("ca")) # string.count("matchingString") to count occurence of char or string in parent string
print(message.find("c")) # string.find("matchingString") find the index of matching string || matchingString can be char or string || returns -1 for not found

test="hello world"
test=test.replace("world","universe")
print(test)
# string=string.replace("whattoReplace","replaceByString")


#************************************************************************************************

#concatenation
greeting="hello"
name="Micheal"
message=greeting+ " " +name # error Prone Lengthy Methods


message="{} {} , welcome bruv".format(greeting,name)
message="{} {} , welcome bruv".format(greeting,name.upper())

# F strings Py 3.6 + version only
# F Strings allow writing code and variables in placeholders

message=f"{greeting} {name.upper()} welcome Brub"

print(message)


#************************************************************************************************

# dir () shows related attributes to varibale depending on its datatype
print(dir(message))

##************************************************************************************************

# help() shows all info regarding datatype | datatype.method | cannot pass variable
print(help(str))
print(help(str.lower))
