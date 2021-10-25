# Aspects of being Pythonic mean that you're following conventions and coding styles of the python language in order to write clean and readable code

# basic 2 and more aspects of being Pythonic
	# Duck Typing
	# concept that it is easier to ask forgiveness than permission

# Summary:
# Duck Typing and EAFP are the fundamentals for a code to be 'Pythonic'


# Duck Typing is when programmers do not care about exactly what an object is, but only care about whether an object can do the operations that we need it to be. In Corey's example where he created classes 'human' and 'duck' and instance for each,  both had the method 'quack' and 'fly'. Therefore, a programmer who does duck typing makes functions that can make use of objects that are of any classes, as long as they support the operations used in the function.
# (I believe this is partly caused by python's feature that we don't have to set the data type for the input and output of function. For example, Golang, or simply 'GO' is an programming language created by Google, and it requires the programmer to specifically set the input and output data type for function.)


# This leads to occasional errors, that occur when some objects do not support the operations.


# To avoid an error, programmers have 2 choices.
# 1. Avoid it in the first place
# 2. handle the error


# The first choice necessitates using an if block. Corey displays an example where he checks whether certain objects have certain attributes, to prevent errors such as 'class ~~~ does not support attribute ~~~'.  He also shows an example where a file might could not be open even after chekcingthat is is accessible using an 'isaccessible' method, which could lead to an error. This is called 'Look before you leap', abbreviated as 'LBYL', and 'Asking Permission' from 'Easier to Ask Forgiveness than to ask Permission'.


# The second choice leads the coder to use 'try' and 'except' block, which handles the error after it has been found.


# There are reasons that the second method is favored over the first.
# 1. It is faster. The first method, 'LBYL' is checking whether an object supports an operation. That means the computer has to access and interpret what kind of class or type the object is. Executing the operations after that 'check', will make the computer having to interpret what the object is 'twice'. 'Asking forgiveness' method only has to access the object once, using the if block. This makes the runtime for 'asking forgiveness' faster, becuase it has less workload for the computer to do.


# 2. It is more readable compared to the first. In the video, Corey shows an example where he had to check whether a dictionary had a number of keys in it.  That was indeed lengthy, which made it harder to read. In another example he showed, he had to be sure that a list had more than 6 arguments in order to print an item at index 5. He used an len() method and >= conditional, which was obviously  lengthy . Using Try and Except blocks was a relatively concise and clear about what the code was all about.


# 3. It gives more control over 'unexpected' error. In the last example that Corey showed, 'LBYL' method did take account of instance where the file might not be accessible. However, Corey points out that a file could be closed right away and raise an error. 'LBYL' method has no way of handling this situation, since it is only designed to 'prevent' an error and does not has the ability to confront it. Try and Except blocks on the other hand, has the ability to resolve errors of any kind.


# Thank you Corey, you are changing the world for what you have done. I believe that your such actions of uploading free education videos are creating a difference in the world. Anyone in the world, whether they have money or not, can educate themselves as long as they have internet. That is the first step towards reaching general rights to education. Thank you!!! I will support you soon when I get a job!

# https://www.youtube.com/watch?v=x3v9zMX1s4s&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=32

# Duck Typing 
	# we don't care what type of object we are working with we only care if our object can do what we ask it to do
	# if an object walks like a duck and acts like a duck then it is a duck
class Duck:
	def quack(self):
		print('Quack,quack')
	def fly(self):
		print('Flap,flap!')

class Person:
	def quack(self):
		print('Im quacking like a duck')
	def fly(self):
		print('Im flapping my arms')
	
def quack_and_fly(thing):
	# Not Duck-Typed (Non-Pythonic)
	if isinstance(thing,Duck):
		thing.quack()
		thing.fly()
	else:
		print('This has to be a Duck!')

	print()

d=Duck()
quack_and_fly(d)

p=Person()
quack_and_fly(p)

# Output
# Quack,quack		 	for object d
# Flap,flap!

# This has to be a Duck! 	for object p
				# since check failed isintance(thing,Duck) 

#***************************************************************************** 
# EAFP Pythonic way
class Duck:
	def quack(self):
		print('Quack,quack')
	def fly(self):
		print('Flap,flap!')

class Person:
	def quack(self):
		print('Im quacking like a duck')
	def fly(self):
		print('Im flapping my arms')
	
def quack_and_fly(thing):
	thing.quack()
	thing.fly()
	
	print()

d=Duck()
quack_and_fly(d)

p=Person()
quack_and_fly(p)

# Output
# Quack,quack
# Flap,flap!

# Im quacking like a duck
# Im flapping my arms


# Look Before you Leap approach LBYL (Non-Pythonic) needs permission checks at every step
class Duck:
	def quack(self):
		print('Quack,quack')
	def fly(self):
		print('Flap,flap!')

class Person:
	def quack(self):
		print('Im quacking like a duck')
	def fly(self):
		print('Im flapping my arms')
	
def quack_and_fly(thing):
	# LBYL look before you leap non-pythonic 
	# permission check at steps non-forgiving
	if hasattr(thing,'quack'):
		if callable(thing.quack):
			thing.quack()

	if hasattr(thing,'fly'):
		if callable(thing.fly):
			thing.fly()		

d=Duck()
quack_and_fly(d)

p=Person()
quack_and_fly(p)

#***************************************************************************** 

# EAFP Easier to ask for forgiveness than permission approach Pythonic approach
	# try something if it works great and if not then handle that error

class Duck:
	def quack(self):
		print('Quack,quack')
	def fly(self):
		print('Flap,flap!')

class Person:
	def quack(self):
		print('Im quacking like a duck')
	def fly(self):
		print('Im flapping my arms')

# EAFP approach
def quack_and_fly(thing):
	try:
		thing.quack()
		thing.fly()
		thing.bark()
	except AttributeError as e:
		print(e)

	print()

d=Duck()
quack_and_fly(d)

p=Person()
quack_and_fly(p)

# Output

# Quack,quack
# Flap,flap!
# 'Duck' object has no attribute 'bark' >>   statements which can be run are run and exception reported on exceptions

# Im quacking like a duck
# Im flapping my arms
# 'Person' object has no attribute 'bark'

#***************************************************************************** 

# EAFP {Pythonic} vs LBYL {Non-Pythonic} Approach:

person={'name':'Jess','age':23,'job':'hekoor'}

# LBYL {Non-Pythonic} Look before you leap Permission checking
if 'name' in person and 'age' in person and 'job' in person:
	print(f'My name iz {person["name"]} age iz {person["age"]} kbljob is {person["job"]}')
	print('Name is {name} age is {age} and job is {job}'.format(**person))
else:
	print('Missing Keys')
		# checking every key if it exists aka asking for permission
	
# EAFP {Pythonic} Easier to ask for forgiveness than permission

try:
	print('Name is {name} age is {age} and job is {job}'.format(**person))
except KeyError as e:
	print(f'Missing key {e}')

		# works for keys that exist and at the end reports key that doesnt exist


person={'name':'Jess','age':23}

 # Missing Key Exception in between case
try:
	print(f'{person["name"]}')
	print('Name is {name} job is {job} age is {age}'.format(**person))
	print(f'{person["age"]}') # not executed stack trace broken above due missing key
except KeyError as e:
	print(f'Missing key {e}')

#*****************************************************************************

myList=[1,2,3,4,5,6]

# LBYL Non pythonic
if len(myList)>=6:
	print(myList[5])
else:
	print('Index doesnt exist')

# EAFP Pythonic
try:
	print(myList[5])
except IndexError as e:
	print('Index error'+e)

#***************************************************************************** 

# EAFP is generally used more than asking for permissions everytime LBYL approach
# EAFP used since Faster - since don't need to access object multiple time for permission checking unlike LBYL approach
# generally less code

#***************************************************************************** 

# RACE Condition avoid using EAFP 
	# from python docs example

import os

myFile='/tmp/test.txt'

# Race Condition
if os.access(myFile,os.R_OK):
	with open(myFile,'r') as f:
		print(f.read())
else:
	print('File cannot be accessed')
	# This is Race Condition cuz-
		# in first os.access() line maybe file not avaialable anymore when reach second line with open() and we are likely to Not catch that error so use EAFP
	
# No Race Condition
try:
	f=open(myFile)
except IOError as e:
	print('File cannot be accessed')
else:
	with f:
		print(f.read())