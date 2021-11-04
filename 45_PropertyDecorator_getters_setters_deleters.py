# objects are as an abstraction of data - concept of OOP

# property decorators helps give our class attributes -> getters,setters and deleter funtionality

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property # property decorator will allow us to access email method as an attribute from instance outside
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter  # @functionName.setter to create setter for a method
    def fullname(self,name):
	    first,last=name.split(' ')
	    self.first=first
	    self.last=last
        # self.first, self.last = name.split(' ') 
            # also works direct
	
    @fullname.deleter
    def fullname(self):
	    self.first=None
	    self.last=None
	    print('Deleted Name!')
    
emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer" # -> gives attribute error since is a method whose code does'nt change data members even tho has @property decorator hence create setters for this
	# looks for setter method to update values

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# example if first name change
emp_1.first='john'
	# email does'nt get changed since depends on __init__() which called only once at creation time
		# to solve
			# can't use email method separate since breaks code and need to call everytime
			# therefore use property decorator {which allows to treat methods like attributes and have setters getters for it} python equivalent to getters setters java
		
# Property decorator allows us to define a method in class but that we can access it like an attribute
print(emp_1.email)
print(emp_1.fullname())


# property decorators allow us to access attributes without putting getters and setters everywhere in case need those can use propery decorators


#***************************************************************************** 

class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@email.com'

    def fullname(self):
        return '{}{}'.format(self.first,self.last)

emp1=Employee('John','Smith')

print(emp1.first)
print(emp1.email)
print(emp1.fullname())
		# OP
		# John
		# John.Smith@email.com
		# JohnSmith

# email attribute depends on first and last name 

emp1.first='Jim'
print()
print(emp1.first)
print(emp1.email)
print(emp1.fullname())
		# OP
		# Jim
		# John.Smith@email.com
		# JimSmith
			# Full name and first name changed but Email did't change since gets updated only on initial object creation in __init__() method
				# to correct may think make email() method -> problem with that is will break for code for others using inheriting our class since email attribute earlier but now function() method
					# therefore other languages use getters and setters for setting values of attributes
					# this can be done using property decorator in python ez 
					# property decorator lets us define a method but we can access it like an attribute 

class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    @property # property decorator made , can now access email() method like attribute -> object.email instead of object.email()
	# but now can't access object.email() as method gives TypeError
    def email(self):
	    return f'{self.first}{self.last}@email.com'

    @property
    def fullname(self):
        return '{}{}'.format(self.first,self.last)


# now email is an method like fullname but earlier inherting classes still has attribute calls{calls as attributes not as methods()} not method calls so will need to correct whole code so now instead use property decorators 

emp1=Employee('Corey','Dada')
print(emp1.email)
print(emp1.fullname)

# if try changing property decorator assignment can't >> error Can't set attribute
	# so use setters which is another decorator with name as @FunctionName.setter

# making deleter as another property decorator

emp1.fullname='Some Name'

@property
def fullname(self):
	return '{}{}'.format(self.first,self.last)


@fullName.setter 		# @FunctionName.setter
def fullname(self,name):
	first,last=name.split(' ')
	self.first=first
	self.last=last
	# or can also direct

	self.first,self.last=name.split(' ')

emp1.fullname='Some Name' # now works 

@fullName.deleter
def fullname(self):
	print('Deleted!!!')
	self.first=None
	self.last=None

# deleter code runs whenever we delete an attribute
del emp1.fullname	
	# runs deleter

#*****************************************************************************
# Experimental self understanding 
class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property
    def email(self):
	    return f'{self.first}{self.last}@email.com'

    def fullname(self):
        return '{}{}'.format(self.first,self.last)

emp1=Employee('John','Smith')

emp1.first='Rand'
print(emp1.first)
print(emp1.email())
print(emp1.fullname())
	