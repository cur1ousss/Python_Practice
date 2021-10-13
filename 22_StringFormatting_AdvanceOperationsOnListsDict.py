# using String concatenation for String Format presentation while Printing
person={'name':'Jenny','age':23}
sentence='My name is '+person['name']+' and i am '+ str(person['age'])+' years old'

print(f'Concatention for formatting   ** {sentence}')
	# limitations with concatenation for formatting purposes
		# pass integers as strings
		# need put spaces ' ' in correct locations beg and end of var
		# not enough readable

# F string
sentence=f'My name is {person["name"]} and i am {person["age"]} years old'
	# Please mind the single ' and double " quotes in the above statements as placing them wrong will give syntax error.
	# F strings with Dictionary in {} use combination of '' and "" outside inside vice versa cannot homogenously all "" ''

print(f'F strings for fomatting \t** {sentence}')


# using .format() formatting function
	# {} are placeholders
sentence='My name is {} and i am {} years old.'.format(person['name'],person['age'])

print(f'.format() function for formatting ** {sentence}')

	# explicitly numbering placeholders
		# numbering placeholders useful when values need to be repeated
sentence='My name is {0} and i am {1} years old.'.format(person['name'],person['age'])

# numbering placeholders useful when values need to be repeated
tag='h1'
text='This is a headline'
sentence='<{0}>{1}<{0}>'.format(tag,text)

print(f'numbering placeholders {sentence}')

# grabbing specific fields from our placeholders
person={'name':'Jenny','age':23}
sentence='My name is {0[name]} and i am {1[age]}'.format(person,person)
sentence='My name is {1[name]} and i am {0[age]}'.format(person,person) # numbering does'nt affect much [attributeName] attirbuteName is Important for Accessing element

print(f'grabbing fields from placeholders {sentence}')


	# using placeholder single nummber 0[attribute] and accessing attribute with it // same way how access elements of list
sentence='My name is {0[name]} and i am {0[age]}'.format(person)
listee=['Jenn',23]
sentence='My name is {0[0]} and i am {0[1]} years old.'.format(listee)

print(sentence)



class Person():

	def __init__(self,name,age):
		self.name=name	# name attribute
		self.age=age	# age attribute

p1=Person('Jack',33)	# instance of class Person
sentence='My name is {0.name} and i am {0.age} years old.'.format(p1) 
# PlaceholderNumber.attribute of class for Classes 
# PlaceholderNumber[DictKey or ListIndex] for Dictionaries and List

print(sentence)

# passing keyword arguments to .format() placeholders
sentence='My name is {name} and i am {age} years old.'.format(name='Ramlal',age=33)
print(sentence)

# Unpacking Lists and Dictionaries
person={'name':'Jenn','age':32}
sentence='My name is {name} and i am {age} years old.'.format(**person)

print(sentence)

#*****************************************************************************
# Formatting Numbers

for i in range(1,11):
	sentence='The value is {}'.format(i)
	print(sentence)

 # condition to add 0 before single digit number // 0 padding
	# use : for formatting numbers
for i in range(1,11): # or range(11)  		# 0'th index also padded in starting
	sentence='The value is {:01}'.format(i)	# has no effect neither does affect 10 printing 
	sentence='The value is {:02}'.format(i) # pads 1 to 9
	sentence='The value is {:03}'.format(i) # pads 1 to 10
	print(sentence)

# handling decimals

pi=3.1459265

sentence='pi is {:.2f}'.format(pi) # vid 22 - https://www.youtube.com/watch?v=vTX3IwquFkc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU his Ouput is 3.14 py2.7 but my py 3.6.9 output is rounded off 3.15?
print(sentence)


# comma separators for big numbers

sentence='1 MB is equal to {:,} bytes'.format(1000**2)	# comma separated on English system 3 zeores places
print(sentence)

# comma spearated and upto 2 decimal places
	# Combining Number Formatting chain
sentence='1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)

#***************************************************************************
# Importing Date Time

import datetime

mydate=datetime.datetime(2016,9,24,12,30,45) # Computer form  YY MM DD Hr Min Sec
print(mydate)

# human readable date time Comma separated
	# https://docs.python.org/3/library/datetime.html for format codes padding
sentence='{:%B %d, %Y}'.format(mydate) # Month DayNumber , Year
print(sentence)

	# ALSO STUDY F STRINGS AND DATE TIME ....>!>!>>!>!>! ????????????
sentence=f'{mydate:%B %d, %Y} fell on a {mydate:%A} and was the {mydate:%j} day of the year'
	# F String Formatting Date Time
num=1203912.3469420

out=f'Printing deez nuts original Number {num} now Formatting {num:12} padded left , now put comma {num:,} , also round off {num:.3f}'
print(out)
	# padding in decimal long number??????

# Q. print day of year and date

# sentence='{:%B %d, %Y} fell on a {:%A} and was the {:%j} day of the year'.format(mydate) >> ERROR only single mydate

sentence='{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(mydate)
sentence='{:%B %d, %Y} fell on a {:%A} and was the {:%j} day of the year'.format(mydate,mydate,mydate)
print(sentence)