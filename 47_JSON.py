# Javascript Object Notation JSON
	# common data format for storing information
	# used when fetching data from online api
	# used for configuration files and storing data on local machine in structured form

# inspired by Javascript but now independent works for all langs

import json
from os import stat, write

# err 	# multi line string that is valid Json almost looks like python dictionary -> has key people , value of people is an array of more objects and each object has key of name , phone ,emails

# people_string is a multi line string that is valid json
	# looks like a py dict this json here has key called people value of people is an array of objects , each object has keys and values 
people_string='''	
{
	"people":[
		{
			"name":"John Smith",
			"phone":"231-555-7164",
			"emails":["johnsmith@bogusemail.com","johnsmith@work-palce.com"],
			"has_license":false
		},
		{
			"name":"Jane Doe",
			"phone":"560-555-3241",
			"emails":null,
			"has_license":true
		}
	]
}
'''

# loading json {string formatted in python} into python object to make work ez
data=json.loads(people_string)
print(data)	# output is converted decoded form of above json following below table reference
print(type(data)) # to check type of variable

	# when we load json into python object it uses following Conversion table -> https://docs.python.org/3/library/json.html#encoders-and-decoders 

		       ## JSON 	 	Python
			
			# object 	 dict
			# array 	 list
			# string 	 str
			# number(int) 	 int
			# number(real) 	 float
			# true 	 	 True
			# false 	 False
			# null 	 	 None	

for person in data['people']:
	print(person)
	print(person['name'])	# since converted object json into dict py when loading access like dict

# Dump python string into Json object
	# use case >> sanitize/updating json using py and convert back to json

data=json.loads(people_string)
for person in data['people']:
	del person['phone']	# deleting phone numbers example

new_String=json.dumps(data)

print(new_String)

# to make more readable use indent argument while loading >> indent tells how many spaces per level to leave
new_String=json.dumps(data,indent=2)
print(new_String)

# can also sort keys alphabetically while dumping 
new_String=json.dumps(data,indent=2,sort_keys=True)
print(new_String)

#*****************************************************************************
# Loading Json files to edit in py and load back

import json

# use load method to load json file
# use loads method to load json string

with open('47_sample.json','r') as f:
	data=json.load(f)

for state in data['states']:
	print(state)
	print(state['name'],state['abbreviation'])	# print multiple objects using , or f string for better formatting
	del state['area_codes']

# dump method converts data into json file
# dumps method converts data into json string

with open('47_newsample.json','w') as writefile:
	json.dump(data,writefile)
	json.dump(data,writefile,indent=2)

#***************************************************************************** 

# real example json from website public apis

# to make request to web api use urllib module builtin, can also use requests library
	# https://www.youtube.com/watch?v=9N6a-VLBa2I -> original video
			# url yahoo api redundant in 2021 so refer video for output
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as responseFromSite:
	source=responseFromSite.read()
	
print(source)

data=json.loads(source)
print(json.dumps(data,indent=2))

# count elements in list
print(len(data['list']['resources']))
		# resources dictlist within list key

for item in data['list']['resources']:
	print(item)
		# *** item now latches onto exterior list key->resources key
			# can now access keys within it using item['keyName']
	name=item['resource']['fields']['name']
			# name key within fields key with parent resource key
	price=item['resource']['fields']['price']

# make currency convertor using conversion rates mentioned in above json
usd_rates=dict()
for item in data['list']['resources']:
	print(item)
	name=item['resource']['fields']['name']
			# name key within fields key with parent resource key
	price=item['resource']['fields']['price']
	usd_rates[name]=price

print(usd_rates['USD/EUR'])
print(50*float(usd_rates['USD/GMP']))