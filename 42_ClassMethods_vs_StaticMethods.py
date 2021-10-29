# regular methods
# class methods
# static methods

# regular methods in a class automatically take the instance as the first argument by convention calling self at declaration in param parameter

# class methods
	# to change to take automatically Class as the first argument use class methods
	# to change regular method to class method add decorator to regular method

class Employee:

	raise_Amount=1.04
	num_of_emps=0

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+'.'+last+'@gmail.com'
		
		Employee.num_of_emps+=1


	def fullName(self):
		return f'Name: {self.first} {self.last}'

	def apply_Raise(self):
		self.pay=int(self.pay*self.raise_Amount)
		self.pay=int(self.pay*Employee.raise_Amount)

	@classmethod
	def set_raise_amount(cls,amount):
			# cls is common convetion for class argument in class methods like self in regular methods in class , can't use class since special meaning keyword
		cls.raise_Amount=amount

	@classmethod # classmethod as alternative constructor
	def from_string(cls,emp_str):	# by convention class method constructors starting with name from		
		first,last,pay=emp_str.split('-')
		return cls(first,last,pay)
			# *** cls(first,last,pay) equivalent to EmployeeClass(first,last,pay)
			# need to return created object since not implicit automatic like init() method

	@staticmethod
	def is_workday(day): # don't take instance or class as first argument hence can pass custom argument directly that need to work with
		
		# monday is 0 sunday is 6
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True
		

emp1=Employee('Corey',"Schafer",150000)	
emp2=Employee('Test','User',6000)
		# class method arguments not passed here while instantiating

Employee.set_raise_amount(1.37)	# automatically accepts class as the first argument like how object creation automatically takes self as first args
	# can run class methods from instances as well but not used makes no sense
emp1.set_raise_amount(1.97)
	# changes for all since it is class method , different from class variable where changes only in local namespace of instance

print(Employee.raise_Amount)
print(emp1.raise_Amount)


# using class methods as alternative constructors
	# using class methods to provide multiple ways of creating object

# example passing string to create instance
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

new_emp1=Employee(first,last,pay)

print(new_emp1.email)
print(new_emp1.pay)

# better to use alternative constructor class method for creating objects from string instead of parsing and splitting string

new_emp2=Employee.from_string(emp_str_2)

print(new_emp2.email)
print(new_emp2.pay)


# practical example of @classmethod  as constructors in datetime module
import datetime

@classmethod
def fromtimestamp(cls,t):
	'construct a datetime from POSIX timestamp like time.time()'
	y,m,d,hh,mm,ss,weekday,jday,dst=_time.localtime(t)
	return cls(y,m,d)

# Additional constructors
class Temp:
    @classmethod
    def fromtimestamp(cls, t):
        "Construct a date from a POSIX timestamp (like time.time())."
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y, m, d)

    @classmethod
    def today(cls):
        "Construct a date from time.time()."
        t = _time.time()
        return cls.fromtimestamp(t)

    @classmethod
    def fromordinal(cls, n):
        """Construct a date from a proleptic Gregorian ordinal.
        January 1 of year 1 is day 1.  Only the year, month and day are
        non-zero in the result.
        """
        y, m, d = _ord2ymd(n)
        return cls(y, m, d)


#*****************************************************************************

# Static Methods 

	# regular method pass instance as the first argument self
	# class methods pass class as the first argument cls
	# static methods don't pass anything they behave like normal functions, included because they have some logical connection with the class

# example find if a date was a work day related to employees but not specific instances

# if we don't access instance of class or the class variables in a method then can make that method static

import datetime
mydate=datetime.date(2016,7,10)

print(Employee.is_workday(mydate))
	# call static method by ClassName