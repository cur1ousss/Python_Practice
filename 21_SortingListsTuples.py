listInt=[91,2,3,5,123,8,7,2,3,12,3,2,1]

sortedList=sorted(listInt)
sortedList=sorted(listInt,reverse=True)

print('Sorted list \t',sortedList)
print(f'Original List \t{listInt}')

# sorted(list)	 creates another sorted Temporary list , does'nt change sort the initial list
		# and returns the copy tmp sorted list copy

listInt.sort() # listX.sort() >> sorts the original list does'nt create a list
			# sorts the list In Place returns none

listInt.sort(reverse=True)
print(f'listInt.sort() is {listInt}')


# ListX.sort() >> works only for Lists
# sorted(List) >> works for Any Iterable

listT=[1,3,4,3,7]

newList=sorted(listT)
listT=newList

print(listT)

# sorted() on Tuple

tup=(9,3,123,7,3,5,45)
SortedTup=sorted(tup)
print(SortedTup)

# sorted() on Dictionary
	# sorts by key not value

di={'name':'ramlal','age':23,'address':'lawda','phone':'bhangi'}
print(sorted(di))

# sorted() on negative integers
	# sorts mathmatically negative and positive values
bums=[-5,-6,-4,1,2,3,0]
sorted(bums)
print(sorted(bums))

# sorted() based on Absolute value of integer
	# use key parameter

bums=[-5,-6,-4,1,2,3,0]
sortedBums=sorted(bums,key=abs) # runs every value through key function before sorting making comparision
print(sortedBums)

# key useful when sorting objects with named attributes

class Employee():
	def __init__(self,name,age,salary):
		self.name=name
		self.age=age
		self.salary=salary
	
	def __repr__(self): 	# repr >> how want function represented to print data on screen
		return '({},{},${})'.format(self.name,self.age,self.salary) # like F strings 

e1=Employee('Carl',37,70000)
e2=Employee('Sarah',29,80000)
e3=Employee('John',43,90000)

employeeList=[e1,e2,e3]
# sortedEmployees=sorted(employees) >> gives Error since no key passed Function confused on what basis to sort

# Key - Takes a Function as input >> inbuilt function or Custom Function

def e_sortName(emp):
	return emp.name

def e_sortAge(emp):
	return emp.age

def e_sortSal(emp):
	return emp.salary

sortedEmployees=sorted(employeeList,key=e_sortName)
sortedEmployees=sorted(employeeList,key=e_sortName,reverse=True)

	# Lambda Equivalent of above
sortedEmployees=sorted(employeeList,key=lambda e:e.name)
				# anonymous function concept
print(sortedEmployees)

# Operator module import
from operator import attrgetter
sortedEmployees=sorted(employeeList,key=attrgetter('age'))
						# Attributes of emp are - age salary name
		# custom Function input in key=func() more flexible than attrgetter and lambda etc..