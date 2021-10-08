# Slicing
	# way to extract certain element from list or string


myList=  [0,1,2,3,4,5,6,7,8,9]
# index  0 1  2  3  4  5  6  7  8  9
#index -10 -9 -8 -7 -6 -5 -4 -3 -2 -1	
	#  indexes can also be negative

# list[start:end:step]
	# start included
	# end Not included / excluded
	# step 
		# start and end are indexes not values in list

	
print(myList[3]) # print(myList(x)) # x - index , myList(x) - value at x index

a = ['Mary', 'had', 'a', 'little', 'lamb']
#	0 	1	2	3	4
#	-5	-4	-3	-2	-1

print(a[-1:-5])

print(a[0:-5])

print(a[-1:-5])	# printing only works from left to right 
			# here op - [] empty
print(a[-5:-1]) # normal op

print(a[-1:-1]) # op - [] empty

a = ['Mary', 'had', 'a', 'little', 'lamb']
#	0 	1	2	3	4
#	-5	-4	-3	-2	-1

print(a[0:5:0]) # ValueError slice step cannot be zero

print(a[0:5:4]) # step size inclusive element

print(a[0:5:5]) # only op first element


print(a[:]) # prints entire list

print(a[:-1]) # start to end

a = ['Mary', 'had', 'a', 'little', 'lamb']
#	0 	1	2	3	4
#	-5	-4	-3	-2	-1

# step is +1 positive one by default
# step can be negative but not zero

print(a[-1:1:-1])
print(a[3:0:-1])
	# printing in reverse starting from last index -1 to lefter index since step is -1
	# end index not inclusive even when going in reverse

# print Entire list in Reverse
print(a[::-1])
print(*a[::-1])	


# Slicing Strings

sample_url='http://coreyms.com'

print(sample_url)
# Reverse the Url
print(sample_url[::-1])

# Get top level domain of url {.com .org .net .in}
print(sample_url[-4:])

# print url without http
print(sample_url[7:])

# print only name of website
print(sample_url[7:-4])