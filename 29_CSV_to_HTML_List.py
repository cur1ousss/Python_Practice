# convert patrons list in csv form to html list

	# some lines unnecessary in csv file remove them using .next() 
	# choose only specific header fields
	# cannot use split method to parse names since some field{email} may falter

import csv

html_output=''
names=[]

with open('29_ExamplePatrons.csv','r') as data_file:
	csv_data=csv.reader(data_file)

	print(csv_data) # is object in memory will only print location memory
		# this object is an iterable and behaves like a generator hence need to loop over it 
				# can either go line by line
				# or print all at once in form of list
	print(list(csv_data)) # convert to human readable list form
	
	# stepping over generators using next() method
	next(csv_data)	# skip header
	next(csv_data)	# skip 1st line intro

	for line in csv_data:
		print(line)
		if line[0]=='No Reward patrons list':
			break
		names.append(f'{line[0]} {line[1]}')


for name in names:
	print(name)

html_output+=f'<p> There are currently {len(names)} public contribuitors patrons. Thank You! </p> '
	# += to append

# creating HTML unordered List now
html_output+='\n<ul>'	# <UL> unordered list tag

for name in names:
	html_output+=f'\n\t<li>{name}</li>'
		# <li> list element tag
html_output+='\n</ul>'


#*****************************************************************************
# Using DictReader better than csvReader normal

	# turns each line into Dictionary instead of a list
		# fields are keys
		# data as values
import csv

html_output=''
names=[]

with open('29_ExamplePatrons.csv','r') as data_file:
	csv_data=csv.DictReader(data_file,delimiter=',')

	for item in csv_data:
		print(item)


	# since headers by default skipped
	# only need to step over 1st x lines if needed
	next(csv_data)

	for line in csv_data:
		if line['FirstName']=='No Reward patrons list':
			break
		names.append(f"{line['FirstName']} {line['LastName']}")
				# *** When Handling F strings and Dict use alternate "" and '' for Dict Keys and F string
		
for name in names:
	print(name)

html_output+=f'<p> There are currently {len(names)} public contribuitors patrons. Thank You! </p> '
	# += to append

# creating HTML unordered List now
html_output+='\n<ul>'	# <UL> unordered list tag

for name in names:
	html_output+=f'\n\t<li>{name}</li>'
		# <li> list element tag
html_output+='\n</ul>'