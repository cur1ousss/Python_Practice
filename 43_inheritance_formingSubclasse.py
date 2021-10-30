# Inheritance
	# inherit attributes and methods from parent class 
	# can further add or modify in subclasses inherited methods without affecting parent code 

class Employee:

	raise_Amount=1.04	# class variable common to all instances shared among all instances

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+'.'+last+'@gmail.com'
		

	def fullName(self):
		return f'Name: {self.first} {self.last}'

	def apply_Raise(self):
		self.pay=int(self.pay*self.raise_Amount)
		self.pay=int(self.pay*Employee.raise_Amount)
			# access class variables either using class name or an instance of the class , cannot directly access class variables inside methods
			# when we try to access an attribute through an instance it will first check if that instance contains that attribute in its NameSpace and if it does'nt then it will check if the class global Namespace or any class that it inherits from contains that attribute	


class Developer(Employee):
	pass
		# even without its own code Developer has all functionalities of Employee parent class inherited

demp1=Developer('Corey',"Schafer",150000)	
demp2=Developer('Test','User',6000)
	# when instantiate a subclass object instance
		# first looks for attributes,__init__() method,methods of subclass if not found walks up the chain of inheritance to above parent class for attributes,__init__() method,other methods
			# chain of inheritance called method resolution order


# help() function of subclass to visualise inheritance attributes parent class ...
print(help(Developer))
# Output	
	# Help on class Developer in module __main__:

	# class Developer(Employee)
	#  |  Developer(first, last, pay)
	#  |  
	#  |  Method resolution order:
	#  |      Developer
	#  |      Employee
	#  |      builtins.object
	#  |  
	#  |  Methods inherited from Employee:
	#  |  
	#  |  __init__(self, first, last, pay)
	#  |      Initialize self.  See help(type(self)) for accurate signature.
	#  |  
	#  |  apply_Raise(self)
	#  |  
	#  |  fullName(self)
	#  |  
	#  |  ----------------------------------------------------------------------
	#  |  Data descriptors inherited from Employee:
	#  |  
	#  |  __dict__
	#  |      dictionary for instance variables (if defined)
	#  |  
	#  |  __weakref__
	#  |      list of weak references to the object (if defined)
	#  |  
	#  |  ----------------------------------------------------------------------
	#  |  Data and other attributes inherited from Employee:
	#  |  
	# 	raise_Amount = 1.04


# *** Every class in Python inherits from base class object -> builtins.object

class Developer(Employee):
	raise_Amount=1.10

dev1=Developer('Corey',"scahfer",320000)
dev1.apply_Raise()	# applies raise defined in local subclass Developer() 1.10
print(dev1.pay)

dev2=Employee('Mithun','Da',25000)
dev2.apply_Raise()	# since object of Employee() above raise statement has no effect raise remains original
print(dev2.pay)

	# jiski laathi usi ki bhais
		# object of that class subclass refers to its local attributes first

#***************************************************************************** 

# initiate subclasses with more info than parent class can handle -> passing more arguments on instantiation of subclass object

	# example passing Developer specific info argument like Programming Language
		# give Developer() subclass its own __init__ method
class Employee:

	raise_Amount=1.04

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+'.'+last+'@gmail.com'
		

	def fullName(self):
		return f'Name: {self.first} {self.last}'

	def apply_Raise(self):
		self.pay=int(self.pay*self.raise_Amount)
		self.pay=int(self.pay*Employee.raise_Amount)
			# access class variables either using class name or an instance of the class , cannot directly access class variables inside methods
			# when we try to access an attribute through an instance it will first check if that instance contains that attribute in its NameSpace and if it does'nt then it will check if the class global Namespace or any class that it inherits from contains that attribute	
		

class Developer(Employee):
	def __init__(self, first, last, pay,prog_lang):
		# two approach
			# either copy and paste -> but leads to repititve and less maintable code
				# self.first=first
				# self.last=last
				# self.pay=pay
				# self.email=first+'.'+last+'@gmail.com'
		
			# smart approach let __init__() of Employee class handle basic arguments and for extra argument handle with __init__() of developer
		super().__init__(first,last,pay)
			# super will pass these arguments to Employee class __init__() method to handle
		Employee.__init__(self,first,last,pay) # equivalent to super().__init(first,last,pay)
		# super() preferred than using className.__init__()
		self.prog_lang=prog_lang
		

dev1=Developer('Mithun','Da',3000,'JavaScript TypeScript')
print(dev1.email)
print(dev1.prog_lang)
	# dev1 object is of Developer class which in turn uses part of methods of parent Employee class __init__() thus increasing reusability
	

class Manager(Employee):
	def __init__(self, first, last, pay,employeesList=None):	# must use keyword None for List , since can't pass mutable datatypes like list , dicts normally as default arguments employessList=[] can't pass more on this future video	-> https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
		# -> https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
		super().__init__(first,last,pay)
		if employeesList is None:
			self.employeesList=[]
		else:
			self.employeesList=employeesList
	
	def add_emp(self,emp):
		if emp not in self.employeesList:
			self.employeesList.append(emp)

	def remove_emp(self,emp):
		if emp in self.employeesList:
			self.employeesList.remove(emp)

	def print_emps(self):
		for emp in self.employeesList:
			print(emp.fullName())
		

dev1=Developer('Mithun','Da',3000,'Javascript')
mgr1=Manager('Sue','SMirth',150,[dev1])

print(mgr1.email)
print(f'Manages {mgr1.print_emps()}')

#***************************************************************************** 

# My practice example of subclass emp list print without add
	# addEmp() is used to add emp to manager after instantiatoin if needed since basic ones are added in constructor
class Employee():
	def __init__(self,name,pay):
		self.name=name
		self.pay=pay
	
	def printEmpDetails(self):
		print(f'Details EMP : {self.name} {self.pay}')


class Developer(Employee):
	def __init__(self, name, pay,prog_lang):
		super().__init__(name,pay)
		self.prog_lang=prog_lang
	
	def printDevDetails(self):
		self.printEmpDetails()
		print('more Dev details')
		print(f'dev Det {self.prog_lang}')


class Managerlodu(Employee):
	def __init__(self, name, pay,ListEmp=None):	# must use keyword None for List , since can't pass mutable datatypes like list , dicts normally as default arguments employessList=[] can't pass more on this future video	-> https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
		# -> https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
		super().__init__(name,pay)
		if ListEmp is None:
			self.ListEmp=[]
		else:
			self.ListEmp=ListEmp
		
	def print_listUnderloda(self):
		for x in self.ListEmp:
			print(f'Manages: {x}')	# prints x object mem location need to add attribute
			print(f'Manages : {x.name}')
	
devam1=Developer('Ramlal Sharma',2500,'Kotlin')
devam2=Developer('Benaj Slwaly',50,'Randi')

mangu1=Managerlodu('Obsasas Rokda',150,[devam1,devam2])

print(mangu1.__dict__)
print(mangu1.name)
mangu1.print_listUnderloda()



#*****************************************************************************
#  below prints None in Manages list why?
	# statement was wrong since stacked print(print() of function) look more
# 
class Employee:

	raise_Amount=1.04	# class variable common to all instances shared among all instances

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+'.'+last+'@gmail.com'
		

	def fullName(self):
		return f'Name: {self.first} {self.last}'

	def apply_Raise(self):
		self.pay=int(self.pay*self.raise_Amount)
		self.pay=int(self.pay*Employee.raise_Amount)
			# access class variables either using class name or an instance of the class , cannot directly access class variables inside methods
			# when we try to access an attribute through an instance it will first check if that instance contains that attribute in its NameSpace and if it does'nt then it will check if the class global Namespace or any class that it inherits from contains that attribute	

class Developer(Employee):
	def __init__(self, first, last, pay,prog_lang):
		super().__init__(first,last,pay)
		self.prog_lang=prog_lang
		
class Manager(Employee):
	def __init__(self, first, last, pay,employeesList=None):# must use keyword None for List , since can't pass mutable datatypes like list , dicts normally as default arguments employessList=[] can't pass more on this future video	-> https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
		# -> https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
		super().__init__(first,last,pay)
		if employeesList is None:
			self.employeesList=[]
		else:
			self.employeesList=employeesList
	
	def add_emp(self,emp):
		if emp not in self.employeesList:
			self.employeesList.append(emp)

	def remove_emp(self,emp):
		if emp in self.employeesList:
			self.employeesList.remove(emp)

	def print_emps(self):
		for emp in self.employeesList:
			print('Printing Manager\'s under empp')
			print(emp.fullName())
		
dev1=Developer('Mithun','Da',3000,'JavaScript TypeScript')
print(dev1.email)
print(dev1.prog_lang)
	# dev1 object is of Developer class which in turn uses part of methods of parent Employee class __init__() thus increasing reusability

print(f'PRINTING MANAGER DETAILS ____')	
mgr1=Manager('Sue','SMirth',150,[dev1])

# need to use add function?
 	# addEmp() is used to add emp to manager after instantiatoin if needed since basic ones are added in constructor
print(mgr1.fullName())
mgr1.print_emps()
# print(f'Manages {mgr1.print_emps()}') # *** statement wrong?

#***************************************************************************** 

# isinstance() isubclass() methods builtins

# isinstance() will tell if an object is an instance of a class
print(isinstance(mgr1,Manager)) # true
print(isinstance(mgr1,Employee)) # true
print(isinstance(mgr1,Developer)) # false

# issubclass() will tell if a class is subclass of another
print(issubclass(Developer,Employee)) #true
print(issubclass(Manager,Developer)) #false

# practical example of subclassing
	# Exception module in inbuilt whisky library for web exceptions requests