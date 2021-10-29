# Class variables
	# variables shared among all instance of class
# Instance variables
	# variables unique to each instance of class

# access class variables either using class name or an instance of the class (self) , cannot directly access class variables inside methods


class Employee:

	raise_Amount=1.04	# class variable common to all instances shared among all instances
	num_of_emps=0

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+'.'+last+'@gmail.com'
		
		Employee.num_of_emps+=1
			# since init executed everytime an instance is created


	def fullName(self):
		return f'Name: {self.first} {self.last}'

	def apply_Raise(self):
		self.pay=int(self.pay*self.raise_Amount)
		self.pay=int(self.pay*Employee.raise_Amount)
			# access class variables either using class name or an instance of the class , cannot directly access class variables inside methods
			# when we try to access an attribute through an instance it will first check if that instance contains that attribute in its NameSpace and if it does'nt then it will check if the class global Namespace or any class that it inherits from contains that attribute	

print(Employee.num_of_emps)

emp1=Employee('Corey',"Schafer",150000)	
emp2=Employee('Test','User',6000)

print(f'Original pay emp1 {emp1.pay}')
emp1.apply_Raise()
print(f'Raise all emp1 now {emp1.pay}')

# since raise might differ better to use it as  class variable

# how can access class variables through instance -> 
	# when we try to access an attribute through an instance it will first check if that instance contains that attribute and if it does'nt then it will check if the class or any class that it inherits from contains that attribute
Employee.raise_Amount
emp1.raise_Amount
emp2.raise_Amount

# print namespace of emp1 instance to find what it has access to
print(emp1.__dict__)
print(Employee.__dict__)

Employee.raise_Amount=1.2	# changes raise Amount for all instances as well
emp1.raise_Amount
emp2.raise_Amount

emp1.raise_Amount=1.7 # changes raise amount only for the spefic instance
Employee.raise_Amount # remains unaffected
emp2.raise_Amount # remains unaffected
	# because on emp1.raise_Amount=1.7 assignment New attribute called Raise amount created for emp1 in its NameSpace which does'nt affect global NameSpace
	# therefore use above self.raise_Amount instead of EmployeeClass.raise_Amount to custom fit each instance if raise amount changed for that instance


print(Employee.num_of_emps)