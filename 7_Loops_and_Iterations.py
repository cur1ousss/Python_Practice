nums=[1,2,3,4,5]

for num in nums:
	print(num)

# break >> break out of a loop
# continue >> moves onto Next Iteration | skip to next iteration | skip 1 iteration


# break
for var in nums:
	if(var==3):
		print("Found 3")
		break
	print(var)

# continue
for var in nums:
	if(var==3):
		continue # Skipping number 3
	print(var)
#*******************************************************************************

# Nested Loops
for num in nums:
	for alpha in "abc":
		print(num,alpha)
	
	# prints combo of every letter for every number

num1=[1,2,3]
num2=[1,2,3]

for num in num1:
	for numx in num2:
		print(f"printing num {numx}")

#******************************************************************************* 
num1=[100,200,300]
num2=[1,2,3]

for num in num1:
	print(f"Id FIRST num {id(num)}")
	print(f"Value FIRST num {num}")
	for num in num2:
		print(f"Id SECOND num {id(num)}")
		print(f"Value SECOND num {num}")

		# 1st num will be gone? or num is only variable name referring to element in List hence no effect
			# Result >> # num is only variable name referring to element in List hence no effect

#*******************************************************************************

# range() when want to go through Loop certain number of Times
	# range(End_Number) >> Number is not included 
	#		>> Counting starts from 0

	# range(End_Number)
	# range(Start_Number,End_Number)

for i in range(10):
	print(i)

for i in range(1,11):
	print(i)

# While Loop
x=1
while x<10:
	if(x==5):
		print("x is 5 breaking")
		break
	print(f"Running {x}")
	x+=1

# Infinite while conditional Loop >> to break out of infinite loop have to have break condition
	# while True:
x=1
while True:
	if(x==5):
		print("x is 5 breaking")
		break
	print(f"Running {x}")
	x+=1