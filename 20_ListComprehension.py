# Comprehension
	# more readable easier way to create a list
	# "List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list"


nums=[1,2,3,4,5,6,7,8,9,10]

#*****************************************************************************

# n for each n items in nums into new list
myList=[]
for n in nums:
	myList.append(n)
print(myList)
	
	# list comprehension of above 
myList=[n for n in nums]
print(myList)

#*****************************************************************************

# i want n*n for each n in nums
myList=[]
for n in nums:
	myList.append(n*n)
print(myList)

	# list comprehension
myList=[n*n for n in nums]
print(myList)
	# using map+lambda for n*n
myList=map(lambda n:n*n,nums)
print(myList)

#*****************************************************************************

# i want n for each n in nums if n is even
myList=[]
for n in nums:
	if n%2==0:
		myList.append(n)
print(myList)

	# using List Comprehension
myList=[n for n in nums if n%2==0]
print(myList)

	# using filter + lambda
myList=filter(lambda n: n%2==0, nums)
myList=list(filter(lambda n: n%2==0, nums)) # typecase to list?
print(myList)

tmplist=list[myList]
print(tmplist) # TypeError: 'type' object is not subscriptable

#*****************************************************************************

# i want a (letter,num) pair for each letter in abcd and each number in 0123
myList=[]
for letter in 'abcd':
	for num in range(4):
		myList.append((letter,num))
			# since append takes 1 argument pass (letter,num) as tuple
print(myList)

	# nested For loops in List Comprehension
myList=[(letter,num) for letter in 'abcd' for num in range(4)]
print(myList)

#*****************************************************************************

# Dictionary Comprehension
names=['Bruce','Clark','Peter','Logan','Wade']
heros=['Batman','Superman','Spiderman','Wolverine','Deadpool']

# zip() function creates list of tuples of matching index
	# use zip() function for list comprehension

# i want a dict{'name':'hero'} for each name,hero in zip(names,heros)
myDict={}
for name,hero in zip(names,heros):
	myDict[name]=hero
print(myDict)

	# Dictionary Comprehension of above
myDict={name:hero for name,hero in zip(names,heros)}
print(myDict)

	# adding restrictions constraints to Dictionary Comprehension
myDict={name:hero for name,hero in zip(names,heros) if name!='Peter'}
print(myDict)

#*****************************************************************************

# Set Comprehension

nums=[1,1,1,2,1,3,4,2,3,1,5,2,7,8,8,6,6,9,2,1,9,6]
mySet=set()	# empty Set
for n in nums:
	mySet.add(n)
print(mySet)

	# set comprehension of above

mySet={n for n in nums}
print(f"lawda {mySet}")

#*****************************************************************************

# Generator Expressions - https://www.youtube.com/watch?v=bD05uGo_sVI
	# similar to list Comprehension

# i want to yield n*n for each n in nums

# regular Generator >>

nums=[1,2,3,4,5,6,7,8,9,10]

def gen_fun(nums):
	for n in nums:
		yield n*n

my_gen=gen_fun(nums)

for i in my_gen:
	print(i)

	# Generator Expression of Above
my_gen=(n*n for n in nums) # tuple like parentheses

for i in my_gen:
	print(i)

print(my_gen) # prints Address

print(list(my_gen))