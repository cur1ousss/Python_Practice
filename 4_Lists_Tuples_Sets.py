# Lists & Tuples for Sequential Data
# Sets unordered data with unique no duplicates

list_Courses=["Computer Science","Maths","Physics","Biology","Chemisty"]

print(list_Courses) # Output in form of square same list >> ["Computer Science","Maths","Physics","Biology","Chemisty"]
print(f"length is {len(list_Courses)}") # len(ListName) prints len of list
 	# print(len(list_Courses))

print(list_Courses[0]) # indexing start 0 -> n-1
# Output Simple string >> Computer Science
# List Index out of Range Erorr

print(list_Courses[-1]) # -1 for the Last Element of List {for cases where size may increase and need to know only last element}

# Printing Range of Data from Lists
# Output of Range Data in Form >> ["Computer Science","Maths"]
print(list_Courses[0:3])    # listName[X:Y] last part not included (upto)

print(list_Courses[:2]) # listName[:X]  by default assumes from starting if nothing given in start

print(list_Courses[1:]) # listName[2:] by default assumes upto last if nothing given in last

# &&& Slicing Video Continue here later >> https://www.youtube.com/watch?v=ajrtAuDg3yw

# *****************************************************************************

			# Modifying List

list_Courses.append("Economics") # appends at last of list
# list_Courses.append("Psychology","Astronomy") # ERROR   >> List.append() takes only 1 argument

print(list_Courses)

list_Courses.insert(0,"Psychology") # list.insert(Position_Number,"Value") inserts at that position and shifts other automatically Not Overwrite

print(list_Courses)

list_Courses=["Computer Science","Maths","Physics","Biology","Chemisty"]

list_Courses2=["Pyschology","Economics"]

list_Courses.insert(0,list_Courses2) # can insert list within list But Outputs as Sublist >> [['Pyschology', 'Economics'], 'Computer Science', 'Maths', 'Physics', 'Biology', 'Chemisty']
print(list_Courses)

# list.extend("Another List or Element")		different from .append() | .extend() adds to list as whole whereas append adds as sublist
list_Courses.extend(list_Courses2)

print(f"Using .extend() {list_Courses}")

# list.remove("Element") >> removes given Element from list
list_Courses.remove("Economics")

# return_String list.pop()  >> Takes no Argument by default removes the last element, When want to use List as Stack or Queue
	# list.pop() returns the Element Popped
list_Courses.pop()
popped_Element=list_Courses2.pop()

# *****************************************************************************

# list.reverse() >> reverses List Order | Takes no Parameters{Arguments}
list_Courses.reverse()

# list.sort() >> by Default Sorts in Ascending Order Alphabetically and Numerically
# list.sort(reverse=True) >> Sorts in Descending| Reverse Order
# .sort() Method modifies Original List to Retain Original List use sorted() Function
list_Courses2.sort()

# return_Element sorted(list) >> doesnt modify original List only sorts Temporarily
Sorted_Courses=sorted(list_Courses)
print(Sorted_Courses)

# *****************************************************************************

Num_List=[1,2,3,4,5]

print(min(Num_List)) # min(list) >> prints Minimum of List
print(max(Num_List)) # max(list) >> prints Maximum of List
print(sum(Num_List)) # sum(List) >> prints Sum of Elements of List
	# max() min() work on String Lists as well Alphabetically
	# sum() doesnt work on String Lists Error

# *****************************************************************************

# Finding Index of Element in List
print(list_Courses.index("Art")) # prints index of Art in List INdexing >> 0 , 1 ,2
	# if Element doesnt exists gives ValueError()

	# Checking if Element is in list or not
print("Art" in list_Courses) # prints True | False

# *****************************************************************************

# Looping in through List

list_Courses=["Computer Science","Maths","Physics","Biology","Chemisty"]

for varName in list_Courses:
	print(varName)  # By default print statement goes to new line so Output one below Another list_Courses

print("\n")

# Enumerate items in For Loop use enumerate and index

for index,VarName in enumerate(list_Courses):		
	print(index,VarName)		# By default index Starts 0

print("\n")

for index,item in enumerate(list_Courses,start=6):
	print(index,item)		# Starting element indexing goes 6,7,8,9,10 all indexed not Skipped

# ***************************************************************************** 

# List to String and String to List

list_Courses=["Computer Science","Maths","Physics","Biology","Chemisty"]

str_List="- ".join(list_Courses)

print(str_List)

new_List=str_List.split(" - ")

print(new_List)


# Experiment >> Includes Spaces as well in matching Pattern
str_list=" - ".join(list_Courses) # OP >> Computer Science - Maths - Physics - Biology - Chemisty
	# "left_Half_PrevTerm (Separator like - , ) Right_Half_NextTerm"

print(str_list)

new_List=str_list.split("-")

print(new_List)

# ***************************************************************************** 

# Tuples
	# We cant modify tuples Tuples are immutable
	# Lists are mutable Tuples are immutable

	# Mutable

list_Courses=["Computer Science","Maths","Physics","Biology","Chemisty"]

list_2=list_Courses

list_Courses[0]="Hindi"

print(list_Courses)
print(list_2)		# Lists >> list 1 and list 2 are the SAME Mutable Object pointing to Same location hence even tho declared in start updates are carry forwarded

# Immutable

tuple_1=("Computer Science","Maths","Physics","Biology","Chemisty")
tuple_2=tuple_1

#tuple_1(0)="Marathi" # ERROR >> Tuples are immutable hence cant modify 

# ***************************************************************************** 

# SETS
	# Unordered and No Duplicates Allowed
Set_1={"Computer Science","Maths","Physics","Biology","Chemisty"}

print(Set_1)  # Since Sets are unordered Each Time Different Random Output Print of Elements

set_2={"Math","Hindi","Math"}
print(set_2) # Ouput contains only Unique Values

# to find MemberShip of element	# can also in lists ,Tuples But Sets more efficient
print("Math" in set_2)	# Output True | False


set_1={"Hindi","English","Biology"}
set_2={"Marathi","English","Math"}

# To find common elements in both sets
print(set_1.intersection(set_2))

# To find elements in 1 set not in Another
print(set_1.difference(set_2))

# To find all Elements in both sets
print(set_1.union(set_2))

# Empty Lists
emptyList=[]
emptyList=list()

# Empty Tuple
emptyTuple=()
emptyList=tuple()

# Empty Set
emptySet={} # This isnt set ! Its Dictionary
emptySet=set() # Correct Way

# Tuple and List retains all members while printing whereas Set only Prints Unique Elements
tupleo=("math","math","Science")
print(tupleo)

seto={"math","math","Science"}
print(seto)

listp=["math","math","science"]
print(listp)