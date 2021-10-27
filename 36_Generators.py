# advantage of generator over lists

def square_numbers(nums):
	result=[]
	for i in nums:
		result.append(i*i)
	return result


my_nums=square_numbers([1,2,3,4,5])

print(my_nums)

# Conversion to Generator
def square_numbers(nums):
	for i in nums:
		yield(i*i)
			# yield keyword makes it a generator

my_nums=square_numbers([1,2,3,4,5])		
	# generators don't hold the entire result{example here the squares of list} in memory , it yields one result at a time
print(next(my_nums)) # 1
print(next(my_nums)) # 4

# if run next() after last element square gives StopIteration Exception
# can use for loop on generators
for num in my_nums:
	print(num) # for loop automatically stops at last element

# list comprehension of above for loop initial
my_nums=[x*x for x in [1,2,3,4,5]]	
print(my_nums)

# using generator
my_nums=(x*x for x in [1,2,3,4,5])
print(my_nums) # prints generator object memory location need to iterate using for loop

for num in my_nums:
	print(num)

# converting generator to list
	# gain short time printing advantage 
	# lose performance
my_nums=(x*x for x in [1,2,3,4,5])
print(list(my_nums))

# generators are better with performance than list since don't hold all the values/computations in memory

#***************************************************************************** 

import Mem_Profile # custom package see above list folder
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (Before): {}Mb'.format(Mem_Profile.memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in xrange(num_people):
            # https://www.geeksforgeeks.org/range-vs-xrange-python/
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()
print(f'Memory for Normal List')
print('Memory (After) : {}Mb'.format(Mem_Profile.memory_usage_psutil()))
print('Took {} Seconds'.format(t2-t1))



t1 = time.clock()
# Note: This method is deprecated since Python version 3.3 and will be removed in Python version 3.8. The behaviour of this method is platform dependent.
people = people_generator(1000000)
t2 = time.clock()
print(f'Memory for Generators')
print('Memory (After) : {}Mb'.format(Mem_Profile.memory_usage_psutil()))
print('Took {} Seconds'.format(t2-t1))


people=list(people_generator(1000000)) # list conversion takes time between generator and complete list
    # generator 15 Mb mem
    # converted generator 319 Mb mem
    # List 331 Mb mem

#***************************************************************************** 