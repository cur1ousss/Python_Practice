# namedtuple like tuple but more readable
	# tuple different from mathematics 2 pair
from collections import namedtuple

# example RGB code color
color=(55,155,250)
	# normal tuple confusing since refer red by index 0
print(color[0])

# can use dictionary 
	# but namedtuple immutable
	# less code than dictionary

# For those experienced with using OOP, here is some helpful information not mentioned in this video:
	# namedtuple returns a class (that's a child of the built-in class tuple). The first argument you pass to namedtuple becomes the name of the class, while the list of strings becomes the attributes (data fields). You can then call the constructor (the line of code before the print() method in the video) to make objects.

# # This quote from the docs should explain a couple of points here:
# > Named tuple instances do not have per-instance dictionaries, so they are lightweight and require no more memory than regular tuples.
# > To support pickling, the named tuple class should be assigned to a variable that matches typename.
# Pickling is Python's name for its built in method of serializing an object

ColorTuple=namedtuple('Color',['red','green','blue'])
		# name of Tuple # values of tuple

color=ColorTuple(55,125,250)
color=ColorTuple(red=55,green=125,blue=250)

print(color[0]) # can also use namedTuple as normal tuple accessing index
print(color.red)
print(color.blue)

# From comments -> https://www.youtube.com/watch?v=GfxJYp9_nJA
# you can also add a built-in function example sum into a namedtuple field. For example
# define a namedtuple with func
from collections import namedtuple
Colorf = namedtuple('Colorf','r g b fun')
sample = Colorf(1,2,3,sum)
print("namedtuple clrf_ntpl.fun([1,10]): ", sample.fun([1,10]))