from os import read, write
import time

with open('OrgNewDocSort.txt','r') as readFile:
	line1=readFile.readline()
	line2=readFile.readline()
	print(line1)
	print(line2)

with open('OrgNewDocSort.txt','r') as readFile:
	with open('NewDocSort.txt','w') as writeFile:
		
		count=1
		left=[]
		right=[]

		for x in readFile.readlines():

			print(f'Current line is {x} & value of count is {count}')


			y=x.split('\n')[0]
				# sanitise input

			print(f'value after sanitise split is {y}')
			# time.sleep(3)

			if (count-1)%4==0:
				print(f'if block of left element {x}')
				left.append(y)
			elif (count-1)%2==0:
				print(f'if block of right element {x}')
				right.append(y)

			count=count+1

	print(f'Left {left}')
	print(f'Right {right}')

with open('NewDocSort.txt','w') as writeFile:
	flag=0
	for x in left:
		w=f'{x} \t {right[flag]}\n'
		writeFile.write(w)
		print(w)
		flag+=1
		

	# print(x,y)