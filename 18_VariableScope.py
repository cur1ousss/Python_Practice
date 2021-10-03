'''
# Scope
	. determines where our variables can be accessed from within the program and what values those variables hold in different context

	# LEGB
		Local , Enclosing , Global , Built-in

		. Local
			variables defined within a function
		
		. Enclosing
			variables defined within an Enclosing Function
		
		. Global
			variables decalred at the top level of a module or explicitly declare global using Global Keyword
		
		. Built-in
			names pre assigned in Python
'''

x='global x'

def test():
	y='local y'
	print(y)
	print(x) # *** searches first in local scope of Function then searches in Enclosing Scope then to outer to Global

test()
	# print(y)  # Error Since >> y does'nt exist out of scope of test() function 
				# name not defined error
				# y does'nt live outside of test() function

print("deez gap")

x='global x'

def test():
	x='local x'
	print(x)

print(x)
test()


# global keyword for working with global variables inside function
	# don't need to have global variable with same name outside to use global inside function 
	# to overwrite values of global from inside the local function scope

x='outside x'

def func():
	global x
	x="inside x"
	print(x)

print(f"printing normal x {x}")
func()		# order of calling of function affects print()
print(x)  # since globally modified value of x now x=inside x


# can use global in local scope inside of function even if variable of same name does'nt exist outside
def tt():
	global m
	m="m inside"
	print(m)

tt()
print(m)


def run():
	n="n inside"
	print(n)

run()
print(n) 	# gives Name error since n does'nt exist outside of function


x='global x'

def modd():
	global x='lund' # Error Need to Separate lines
	print(x)

modd()

# In Real Code Practice global keyword is Not used Much


# Arguments to Function are also local and don't exist outside of function

def argFunc(z):
	x="inside x"
	print(z)

argFunc("arg Z")
print(z)	# NameError Argument z does'nt exist outside Function

# Built in Scopes
	# are names preassigned in python

# min()	- finds smalles value of the iterable
m=min([3,31,37,3])
print(m)


# dir() gets lists of the attributes of a given object
import builtins

print(dir(builtins))

# accidentaly overriding Builtins methods
	# if create global min() function >> will override build in min()

def min():
	print("Custom Min function")
	pass

min()	# works on global definition , built in min() overriden
m=min([1,3,4])	# gives error since min() now points to global

#*****************************************************************************

# Enclosing 
	# related with Nested Functions


def outer():
	x='outer x'

	def inner():
		x='inner x'
		print(x)
	
	inner()	# def declaring function isn't enough need to call it to use it activate it
	print(x)

outer()


def outer():
	x='outer x'

	def inner():
		print(x) # *** x is checked first to Local Scope then to Enclosing Scope then Global Scope
					# Enclosing Scope >> local scope of any Enclosing Function
	inner()	# def declaring function isn't enough need to call it to use it activate it
	print(x)

outer()


def outer():
	# x='outer x'

	def inner():
		x='inner x'
		print(x) # *** x is checked first to Local Scope then to Enclosing Scope then Global Scope then in builtins defintion
					
	inner()	
	print(x)	# Error

outer()

# working with outer x variable from inner x scope
	# can't use global keyword since will affect global var
	# therefore use nonlocal keyword

def outer():
	x='outer x'
	def inner():
		nonlocal x
		x='lund inner'
		print(x)
	
	inner()
	print(x)

outer()

# non local more used than global keyword
	# non local used to change state of closures , decorators

x='global x'
def outer():
	x='outer x'
	def inner():
		nonlocal x
		x='lund inner'
		print(x)
	
	inner()
	print(x)

outer() 
print(x)