# Javascript Object Notation JSON
	# common data format for storing information
	# used when fetching data from online api
	# used for configuration files and storing data on local machine in structured form

# inspired by Javascript but now independent works for all langs

import json

	# multi line string that is valid Json almost looks like python dictionary -> has key people , value of people is an array of more objects and each object has key of name , phone ,emails

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

# loading into python object to worke ez
data=json.loads(people_string)
print(data)
print(type(data))

	# when we load json into python object it uses following Conversion table -> https://docs.python.org/3/library/json.html#encoders-and-decoders 

			# JSON 	 	Python
			
			# object 	 dict
			# array 	 list
			# string 	 str
			# number(int) 	 int
			# number(real) 	 float
			# true 	 	 True
			# false 	 False
			# null 	 	 None	

