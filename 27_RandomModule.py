# random module should'nt be used for security purposes or cryptography Use Secrets Module instead

import random

value=random.random()
	# .random() returns float value 0 to 1 0 inclusive never 1 only upto 0.9999
print(value)

value=random.uniform(1,10) 
	# random.uniform(begInt,endInt) float value between Range given
print(value)

# random.random() and random.uniform(4,7)  used less since return Float value

# random.randint(beg,end) both inclusive Integer value
value=random.randint(1,6)
	# dice example
print(value)

# choice() picks random number from list
import random
greetings=['hey','hello','hi','howdy','hola']

value=random.choice(greetings)
print(f'{value} Corey')

# get Multiple random Choices()
	# example Roulette
import random
colors=['Red','Black','Green']
result=random.choices(colors,k=10)
	# k is how many times want to pick random choices
		# how many results needed each time 1 choice color
print(result)

# adding Weights to choices 
	# real roulette example
import random
colors=['Red','Black','Green']
result=random.choices(colors,weights=[18,18,2],k=10)
	# weights
		# list of weight associated with each index value 
	# k is how many times want to pick random choices
		# how many results needed each time 1 choice color
print(result)


# Randomly shuffle list of values
	# example deck of cards
import random
deck=list(range(1,53))
print(deck)

random.shuffle(deck)
	# random.shuffle(ListX) shuffles in place - no new temp copy created changes are overwritten to original 
print(deck)

	# to pick 5 cards from deck
		# can't use choices() since can give same card multiple times physically not possible hence use sample() method
import random
deck=list(range(1,53))

hand=random.sample(deck,k=5)
	# random.sample(List,k=5) k=5 number of samples
print(hand)

# https://www.python.org/dev/peps/pep-0008/ Styling Indentation guide

# Creating Random Data for Next Video CSV Tutorial 28 29

''' Super simple module to create basic random data for tutorials'''
import random

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@bogusemail.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')