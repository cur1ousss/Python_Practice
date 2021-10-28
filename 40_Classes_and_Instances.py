# Classes allow to logically group data and functions in a way thats easy to reuse and build upon
	# data asscociated with class called attribute
	# function associated with class called method

class Employee:
	pass

# class is a blueprint for creating instances
emp1=Employee()
emp2=Employee()
print(emp1)
print(emp2)
	# both objects have different location in memory
		# if emp1=emp2 then both point at same memory location

# instance variables , class variables
	# instance variables contain data that is unique to each instance 

emp1.name='corey schafer'
emp1.age=25
emp1.email='corey@gmail.com'

emp2.name='mithun'
emp2.age=63
emp2.email='mithunda@gmail.com'

print(emp1.email)
print(emp2.email)

# Setting information for instances when they're created rather than doing manually like above use init() method

	# init() method -> initialise , similar to constructor

# When we create methods within a class they receive the instance as the first argument automatically and by convention we should call the instance self


# EACH METHOD INSIDE THE CLASS TAKES THE INSTANCE AS THE FIRST ARGUMENT

class Employee:
	def __init__(self,first,last,pay):
		self.first=first
			# similar to emp1.name='corey'
			# can also be self.fname=first
				# but prefer to keep same self.first=first
		self.last=last
		self.pay=pay
		self.email=first+'.'+last+'@gmail.com'

	def fullName(self):
		return f'Name: {self.first} {self.last}'

	def empty():
		print('empty Method without Self')

emp1=Employee('Corey',"Schafer",'150000')	# don't need to pass emp1 like init signature since instance passed automatically to init as self , can leave off self while passing info here at instantiation/creation

print(emp1)
print(emp1.pay)
print(emp1.fullName())
print(emp1.fullName) # fullName is a method not attribute hence use fullName() parentheses

print(emp1.empty())
	# TypeError: empty() takes 0 positional arguments but 1 was given
		# since instance gets passed automatically as self it thinks 1 arg given here but not in defintion in class
			# proof that instance passed automatically

# Running Methods directly using ClassName
	# need to manuallly pass instance as an argument
Employee.fullName(emp1)	# does'nt know for which instance called hence pass explicitly
emp1.fullName()	# automatically picks up the instance called upon

# emp1.fullName() -> background gets transformed like -> Employee.fullName(emp1)