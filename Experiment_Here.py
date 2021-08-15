# ***************************************************************************** 

# Functions >> instructions packaged together , reusablilty

	# def >> definition
	# if leave function body Empty get ERROR

def hello_func():
	pass		# cannot leave function body empty hence use "pass" keyword so can give function definition later

print(hello_func) # prints function location in Memory
print(hello_func())  # prints None since doesnt have return value


def hello_func():
	print("Hello Function!")

hello_func() 
hello_func  # gives No Ouput No Error

# DRY >> keeping code DRY >> dont repeat yourself hello print 4 times instead use function and loop

# ***************************************************************************** 
def tmp_func():
	return "returned_String tmp_func()"

print(tmp_func())
print(tmp_func().upper()) # here treat function like its Return value therefore can Chain functions usable on that datatype returned example len() upper() lower()

# Passing Arguments to Functions
	# Arguments >> real values Passed
	# Parameters >> values passed in Definition of the function

def hello_func(greeting):
	return f"this is a {greeting}"
	# parameter scope is only within local to the Function doesnt affect anything outside ie. can reuse that variable Name outside withouta side effects

print(hello_func("hello"))

## Later Contine Scope >> https://www.youtube.com/watch?v=QVdf0LgmICw

# Using Default Value for Argument if NO value passed

def hello_func(greeting,name="You"):
	return f"{greeting} {name}"

print(hello_func("HelloSoooper")) # uses default value of Parameter in function definition if not pass any parameter at runTime
print(hello_func("Mr.","Ramlal"))
print(hello_func("This is ",name="SomeName"))

# *****************************************************************************

# Out of Order Argument Passing

def temp_func(greeting,name="DefualtName"):
	return f"This is greeting {greeting} and Name : {name} "

print(temp_func(name="SomeName",greeting="GreetingExample"))

def stud_info(*args,**kwargs): # *args & **kwargs Allows us to Accept Arbitary Number of
	print(args)			# Positional Arguments {is in Tuple Form}
	print(kwargs)			# Keyword Arguments   {is in Dictionary Form}

stud_info("Math","Art",name="Corey",age=25)
		# OutPut >>
			# ('Math', 'Art')   *args is in Tuple Form
			# {'name': 'Corey', 'age': 25} **kwargs is in Dictionary Form Key Value Pair

def stud_info(*args,**kwargs): # *args & **kwargs Allows us to Accept Arbitary Number of
	print(args)			# Positional Arguments {is in Tuple Form}
	print(kwargs)			# Keyword Arguments   {is in Dictionary Form}

courses_List=["Math","Art"]
info={"Name":"Corey","Age":25}

stud_info(courses_List,info)
	# OutPut	>> byDefault assumes both as Positional Arguments *args
		# (['Math', 'Art'], {'Name': 'Corey', 'Age': 25})
		# {}
	# For correct Output use * and ** >> to unpack those values into function
stud_info(*courses_List,**info)

# *****************************************************************************

# <P> # Find Leap Year  

# Number of days per month First Value 0 is a placeholder for Indexing purposes use only 1 to 12 index not 0th index where value 0 to ingore
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
	"""Return True for Leap Years, False for Non Leap Years"""
		# """ is for DocString Documentation purposes
	return year%4==0 and (year%100!=0 or year%400==0)

def days_in_month(year,month):
	"""Return number of days in that month in that year"""
		# """ is for DocString Documentation purposes
	
	if not 1<=month<=12:
		return "Invalid Month"
	if month==2 and is_leap(year):
		return 29
	
	return month_days[month]

print(f"2017 is leap?? >> {is_leap(2017)}")
print(f"Days in Month 2 >> {days_in_month(2017,2)}")