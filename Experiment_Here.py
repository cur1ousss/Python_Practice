# ***************************************************************************** 

if True:
	print("condtion True")

if False:		# False Condition gets Ignored not Executed hence No Output
	print("something")	


language="Python"

if language=="Python":
	print("condition is True")


# Boolean Operators
# ==
# !=
# >
# <
# >=
# <=
# is {Object Identity}	>> checks if same object in Memory | if they have same id different from ==

tmp="string"

if tmp=="string":
	print("tmp string")



	print("below block after gap") # Works

print("Tabbed out")	

# If Else Elif

if language=="Python":
	print("language is python")
elif language=="Java":
	print("languge is Java")
else:
	print("Other language")

# Python does'nt have SWITCH CASE

# Boolean Operations
	# and
	# or 
	# not

user="Admin"
logged_in=True

if user=="Admin" and logged_in:
	print("admin page")
else:
	print("Bad creds")


logged_in=False

if not logged_in:
	print("please Log in")
else:
	print("Bad Creds")

result=True

if not result:
	print("failed")
else:
	print("passed")

# Output >> Passed


# Two objects can be equal and Not be the same object in the memory

a=[1,2,3]
b=[1,2,3]

print(a==b)
print(a is b)  # is Matches Memory Location so here A is NOT B , OP >> false

# Location of Object in Memory using id()
print(id(a))
print(id(b))

c=[1,2]
d=c
print(c is d)
print(c==d)
