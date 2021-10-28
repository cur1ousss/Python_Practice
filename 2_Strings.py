# print Multiple Lines String
message="""multiple lines which contain [enter] using 
3 quotes end start"""   

# Prepared to sleep through the storm 

# Strings are immutable in Python

a='corey'
print(a)
print(f'Address of a is {id(a)}')

a='john'
print(a)
print(f'Address of a is {id(a)}')

	# Address of both A is Different

	# here comparision means nothing since 'a' now is john , corey no longer exists by 'a' name ,exists only by its memory address hex
if a==a:
	print('true a==a')
else:
	print('false')

print('Comparing id of a')
if id(a)==id(a):
	print(id(a))
	print(id(a))
	print('id same')
else:
	print('id different')

a='corey'
print(a)
print(f'Address of a is {id(a)}')

a[0]='C'
print(a)	# Error TypeError TypeError: 'str' object does not support item assignment, string immutable can't change/modify string


# lists are mutable objects can modify lists
listX=[1,2,3,4,5]
listX[1]=31

print(listX)

	# again addresses of both a are different after appending a+x original a does'nt exist
a='corey'
print(f'original add of a {id(a)}')

a=a+'x'
print(f'a+x add {id(a)}')

print(a)

# Immutable and Mutable affect Memory and Performance
	# since while modifying immutable string everytime new object memory created
employees=['corey','john','rick','steve','carl','adam']
output='<ul>\n'

for employee in employees:
	output+='\t<li>{}</li>\n'.format(employee)
	print(f'Mem Address of output {id(output)}') # everytime new Object created in memory

output+='</ul>'
print(output)
	# to improve performance either use list.append() or .....

#***************************************************************************** 

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

# Also String Form Study More Later

initial=('first\n'
'second\n'
'third\n')

print(initial)


inout=('first''second''third')
print(inout)


thirra=('first'
'second'
'third'
)

print(thirra)

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

##************************************************************************************************
# printing in same line elements of list
	# by default print() prints next element in new line {\n}
a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in a:
	print(i,end=' * ')

print() # since last lines keep pointer in same line need to shift to next like java nextInt() input after String input eats line 1
# java int x=sc.nextInt();
# 	sc.nextLine(); or 
# String stringaa=sc.nextLine();
	
for i in a:
	print(i,end=' xd ')

for i in a:
	print(i,end='\n')

for i in a:
	print(i,end=' ')

		 # sep= ' xd ' , sep - separator does'nt work


print(*i) # to print elements of list in single line without , 