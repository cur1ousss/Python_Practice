# normal method longer and placeholders when many confusing
firstName='corey'
lastName='schafer'

sentence='My name is {} {}'.format(firstName,lastName)
print(sentence)

# can run functions and methods directly in f strings
sentence=f'My name is {firstName} {lastName.upper()}'
print(sentence)

#***************************************************************************** 

# Dictionaries and F strings
person={'name':'jenn','age':23}

# normal format() method
sentence='My name is {} age {}'.format(person['name'],person['age'])

# f string
sentence=f'My name is {person["name"]} age is {person["age"]}'
	# must use vice versa quotes of outer quotes to access dictionary keys , cannot use same quotes outer and inner since interpreter thinks string terminated when same singe quotes '''
		# gives invalid syntax error
print(sentence)

#***************************************************************************** 
# can also do calculations in f strings
print(f'4 times 11 is {4*11}')


#***************************************************************************** 
# Advanced formatting in F strings
for n in range(1,1001):
	print(f'n value is {n:02}')
			# :02 >> 0 padding limited to 2 digits
			# :2 >> restraint to 2 digits print ??


pi=3.1459265
print(f'pi value is {pi:.4f}')
	# :.4f >> round up to 4 digit floating point

#***************************************************************************** 

from datetime import datetime

birthday=datetime(1990,1,1)
print(f'birthday is {birthday}')

# date time formatting codes in 
print(f'birthday is {birthday:%B %d Any_String_like_year %Y}')

#***************************************************************************** 