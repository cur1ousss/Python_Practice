# special methods that can use inside our classes
	# allow us to implement builtin behavior in python
	# allow us for operator overloading

# operator overloading example
	# '+' symbol -> depending on type of object working with behavior is different
		# concats two string
		# adds mathematical number


# special methods will allow us to change built in behaviour
	# example -> print(object_X) # prints memory locaiton of object
		# to make readable use magic methods

# these special methods surrounded by double underscores __func__() dunders
	# example -> __init__() method
		# dunder method __init__() implicitly called when create Class objects and sets the attributes for us

	# two more special dunder methods -> __repr__() & __str__()
		# https://www.youtube.com/watch?v=5cvM-crlDvg
def __repr__(self):
	pass

def __str__(self):
	pass

# __repr__() -> an unambiguous representation of the object and should be treated for object debugging logging , used by developers

# __str__() -> more readable represenatitno of an object meant for end user

	# __repr__() vs __str__()
a=[1,2,3,4]
b='sameple string'

print(f'str(a) {str(a)}')
print(f'repr(a) {repr(a)}')

print(f'strb(b) {str(b)}')
print(f'repr(b) {repr(b)}')

# According to stackoverflow
	# goal of __repr__ is to be unambiguous
	# goal of __str__ is to be readable

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b = str(a)

print('str(a): {}'.format(str(a)))
print('str(b): {}'.format(str(b)))

print

print('repr(a): {}'.format(repr(a)))
print('repr(b): {}'.format(repr(b)))

print

# Output
	# str(a): 2021-10-31 05:53:40.766208+00:00
	# str(b): 2021-10-31 05:53:40.766208+00:00
		# str gives more readable form of both, ignoring datatype of variable/instance
	# repr(a): datetime.datetime(2021, 10, 31, 5, 53, 40, 766208, tzinfo=<UTC>)
	# repr(b): '2021-10-31 05:53:40.766208+00:00'
		# repr gives unambiguos reality of variable -> a is datetime object , b is string object hence makes clear distinction based on datatype also can use Output of repr() of particular object as command example here datetime -> datetime.datetime(2021, 10, 31, 5, 53, 40, 766208, tzinfo=pytz.UTC)
			# 'a' is not a string. It is a datetime object, while 'b' is a string. The difference isn't obvious when use str() on them, but repr() reverts their true representation. Hence, repr(b) returned a string whereas repr(a) returned a datetime object
	# repr useful for debugging

#***************************************************************************** 

# Dunder methods repr() & str()
	# bare minimum must have __repr__() method , since in case __str__() absent __repr__() will be used as fallback when str() invoked to cover up
	# when creating this methods try to display something that you can copy and paste back in the python code that would recreate that same object


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):	# self for left side on addition, other on right side of addition
        return self.pay + other.pay

    def __len__(self): 
	    # example calculate chars in name
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1) # instead of memory location like earlier now prints use __repr__() method returend string in case __str__() absent __repr__() used
	# if __str__() definition present then __str__() used __repr__() ignored

# can also explicitly called __str__() and __repr__()
print(str(emp_1))
print(repr(emp_1))

print(emp_1.__str__())
print(emp_1.__repr__())

# special dunders on arithmetics
	# integers add use their own dunder add in background
	# strings use their own dunder add method to concatenate
		# so can customise how addition works for our objects by creating that dunder add method
print(int.__add__(1,2))
print(str.__add__('Corey','Schafer'))

# so can customise how addition works for our objects by creating that dunder add method
	# dunder method to add salaries of employees using + emps
def __add__(self, other):	# self for left side on addition, other on right side of addition
	return self.pay + other.pay

print(emp_1+emp_2)	# using above dunder add 
	# cannot use + on emps without dunder definiton in class otherwise get error can't add unknown datatypes not supported
print(emp_1.__add__(emp_2))


# another dunder len method 

# len on simple string
print(len('testString'))
print('testString'.__len__())

print(emp_1.__len__())
print(len(emp_1))

	# more dunder methods on -> https://docs.python.org/3/reference/datamodel.html#special-method-names

import datetime
# real example Dunder method in DateTime module
def __add__(self, other):
        if isinstance(other, timedelta):
            # for CPython compatibility, we cannot use
            # our __class__ here, but need a real timedelta
            return timedelta(self._days + other._days,
                             self._seconds + other._seconds,
                             self._microseconds + other._microseconds)
        return NotImplemented
		# NotImplemented keyword -> used when don't want to throw an error here because the other object might know how to handle that operatoin so returning not implemented is a way to fallback to other object to see if it knows how to handle error and if none of them handles it , will eventually throw an error