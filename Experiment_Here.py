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

# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print('Memory (After) : {}Mb'.format(Mem_Profile.memory_usage_psutil()))
print('Took {} Seconds'.format(t2-t1))