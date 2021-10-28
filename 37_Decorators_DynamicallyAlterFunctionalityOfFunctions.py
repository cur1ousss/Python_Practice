# Rabbit hole: Classes > Decorators > Closures > First-Class Functions
# Multiprocessing > Threading > Decorators > Closures > First-Class Functions

# 1. https://www.youtube.com/watch?v=kr0mpwqttM0 -> First Class Functions
# 2. https://www.youtube.com/watch?v=swU3c34d2NQ -> Closures before Decorators
# 3. https://www.youtube.com/watch?v=FsAPt_9Bf3U -> Decorators


#***************************************************************************** 

# 1. https://www.youtube.com/watch?v=kr0mpwqttM0 -> First Class Functions

# First Class Functions
	# In languages with first-class functions, the names of functions do not have any special status; they are treated like ordinary variables with a function type.
	# In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens. This means the language supports passing functions as arguments to other functions, returning them as the values from other functions, and assigning them to variables or storing them in data structures
	# In programming language design, a first-class citizen (also type, object, entity, or value) in a given programming language is an entity which supports all the operations generally available to other entitiesThese operations typically include being passed as an argument, returned from a function, modified, and assigned to a variable.


# assigning function as normal variable
def square(x):
	return x*x

f=square(5)

print(square)	# prints objects memory location
print(f)	# prints 25

f=square	# f takes up/absorbs/imitates behaviour of function
print(f)	# prints objects memory location
# now can use f as a function square
print(f(5))

# passing functions as arguments and returning functions as result of other functions called Higher order functions {functions that accept/return other functions as arguments/results}
def cube(x):
	return x*x*x

def my_map(func,arg_list):
	result=[]
	for i in arg_list:
		result.append(func(i)) 	# aka using function in another function
	return result

squaresList=my_map(square,[1,2,3,4,5])
cubesList=my_map(cube,[1,2,3,4,5])
print(squaresList)
print(cubesList)

# returning function as a result of another function
def logger(msg):
	def log_message():
		print('Log:',msg)
	return log_message

log_hi=logger('Hi!') # log_hi=log_message()
log_hi()	# log_message() -> print() gets executed here as log_hi() is now a executable function

	# advantage/use of returning function as a result of another function
def html_tag(tag):

	def wrap_text(msg):
		print('<{0}>{1}</{0}>'.format(tag,msg))
	return wrap_text

print_h1=html_tag('h1')	# print_h1 is equal to returned function wrap_text() of higher order function html_tag()
print_h1('Test Headline!') # since equal to wrap_text() pass parameter of form of wrap_text(msg)  , rememers the earlier tag passed as well
print_h1('Another Headline!')

print_p=html_tag('p')
print_p('Test Paragraph!')

	# used for logging

#***************************************************************************** 

# 2. https://www.youtube.com/watch?v=swU3c34d2NQ -> Closures before Decorators
# Closures
	# closures allow us to take advantage of first class functions

	# "Therefore, in simple terms: A closure is an inner function that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing"


	# In programming languages, a closure, also lexical closure or function closure, is a technique for implementing lexically scoped name binding in a language with first-class functions. Operationally, a closure is a record storing a function[a] together with an environment.[1] The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.[b] Unlike a plain function, a closure allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.

def outer():
	message='Hi'
	def inner():
		print(message)	# message is a free variable
			# when inner() function accesses the message variable this is actually free variable since not defined in inner function() but have access within the inner function
	
	return inner() # returning invoked instance of function

outer()	

def outer():
	message='Hi'
	def inner():
		print(message)	# message is a free variable
			# when inner() function accesses the message variable this is actually free variable since not defined in inner function() but have access within the inner function
	
	return inner 	# returning function waiting to be executed

my_func=outer()	
print(my_func) # op -> <function outer.<locals>.inner at 0x7fd2ddc0e820>
print(my_func.__name__)


hi_func=outer('Hi')
hello_func=outer('Hekko')

hi_func()	# hi
hello_func()	# hekko

# so a Closure is an inner function that remembers and has access to variables to the local scope in which it was created even after the outer function has finished executing

# a closure closes over the free variables from its environment

import logging
logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
	def log_func(*args): # *args means any number of arguments inputted
		logging.info('Running "{}" with arguments {}'.format(func.__name__,args))
		print(func(*args))
	return log_func

def add(x,y):
	return x+y
def sub(x,y):
	return x-y

add_logger=logger(add)
sub_logger=logger(sub)

add_logger(3,3)
add_logger(4,5)

sub_logger(10,5)
sub_logger(20,10)

	# this logger is use case for Decorator

#***************************************************************************** 

# 3. https://www.youtube.com/watch?v=FsAPt_9Bf3U -> Decorators

# Decorators

# recap of closures
def outer(msg):
    message=msg

    def inner():
        print(message)

    return inner

hi_func=outer('Hi')
bye_func=outer('Bye')

hi_func()
bye_func()
    
        # also works
def outer(msg):
    def inner():
        print(msg)

    return inner

hi_func=outer('Hi')
bye_func=outer('Bye')

hi_func()
bye_func()

# Decorator 
 # Decorator is just a function that takes another function as an argument adds some kind of functionality and returns another function without altering the source code of the function passed in

def decorator_func(msg):
    def wrapper_func():
        print(msg)
    return wrapper_func
            # returns wrapper function that is waiting to be executed

# below is a simple Decorator example
def decorator_func(original_func):
	def wrapper_func():
		print(f'Wrapper executed this before {original_func.__name__}')
		return original_func()
	return wrapper_func

def display():
    print('display function ran')

decorated_display=decorator_func(display)
decorated_display()
    # wrapper_func executed first then original_func() inside wrapper_func() executed
    
# Decorating functions helps add functionality to our existing functions by adding that functionality inside of our wrapper

def decorator_func(original_func):
	def wrapper_func():
		print(f'Wrapper executed this before {original_func.__name__}')
		return original_func()
	return wrapper_func

@decorator_func  # equivalent to display=decorator_func(display)
def display():
    print('display function ran')
	# **** using tag annotation @decorator_func is similar to
		# display=decorator_func(display)
			# passing that function into decorator function
	
display()	# output will have wrapper code added to original function display()

# annotations helpful for chaining decorators over nomarl assigning and passing into decorator function

# @decorator
#  def function():
#     ...

# is equivalent to: function = decorator(function).

# above method won't work incase original_func() took any arguments
	# need to use *args **kwargs for positional , keyword arguments in wrapper function otherwise throws error TypeError by definiton takes 0 args but passed 2 for the decorated func display_info maybe 3,4 ... 

	# *args,**kwargs allow function to accept any arbitary number of positional or keyword arguments for our functions

	# use *args **kwargs in wrapper function since has use of original_func() inside if did'nt maybe did't need to pass -> that use case would have been different then no wrapper decorator in that case
def decorator_func(original_func):
	def wrapper_func(*args,**kwargs):
		print(f'Wrapper executed this before {original_func.__name__}')
		return original_func(*args,**kwargs)
	return wrapper_func

@decorator_func  # equivalent to display=decorator_func(display)
def display():
    print('display function ran')
	# **** using tag annotation @decorator_func is similar to
		# display=decorator_func(display)
			# passing that function into decorator function
	
display()	# output will have wrapper code added to original function display()



@decorated_func
def display_info(name,age):
	print(f'display info ran with arguments ({name},{age})')

print(display_info.__name__) # actually executing wrapper here
display_info('john',25)

	#***************************************************************************** 
# Classes as Decorators instead of functions as decorators

# def decorator_func(original_func):
#     def wrapper_func(*args,**kwargs):
# 	print(f'Wrapper executed this before {original_func.__name__}')
# 	return original_func(*args,**kwargs)
#     return wrapper_func

class decorator_class(object):
	# we passed original function to our decorator function using as an argument
	# in case of classes use __init__ method to pass original function to class as parameter
	def __init__(self,original_func): # self for the instance
		self.original_func=original_func
			# this gonna tie the function with the instance of the class 
	
	# using __call__ method add more functionality like wrapper_func() above
	def __call__(self,*args,**kwargs):	# gonna behave like wrapper_func()
		print(f'__call__() method executed this before {self.original_func.__name__}')
		return self.original_func(*args,**kwargs)
		# using an instance now so call original_func() by instance self

@decorator_class  # equivalent to display=decorator_class(display) then display()
def display():
    print('display function ran')
	
display()	

@decorator_class
def display_info(name,age):
	print(f'display info ran with arguments ({name},{age})')
display_info('john',25)


# Practical Example of Decorators 
	# Logging {below}
		# Decorators used for 
			# loggers
			# class properties
			# routing for some web frameworks

	# making logger to keep track how many times function run and number of arguments passed used
def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)

	def wrapper(*args,**kwargs):
		logging.info('Ran with args: {}, and kwargs {}'.format(args,kwargs))
		return orig_func(*args,**kwargs)
	return wrapper

def my_timer(orig_func):
	import time

	def wrapper(*args,**kwargs):
		t1=time.time()
		result=orig_func(*args,**kwargs)
		t2=time.time()-t1
		print(f'{orig_func.__name__} ran in {t2} secs')
		return result
	return wrapper

@my_logger
def display_info(name,age):
	print(f'display info ran with arguments ({name},{age})')

display_info('john',25)

# using logger as a decorator can now reuse it to fit any function
	# otherwise without decorators would have to make custom logger for each function
	
import time 
@my_timer # custom decorator to time functions
def display_info(name,age):
	time.sleep(1)
	print(f'display info ran with arguments ({name},{age})')

display_info('john',25)

# Chaining Decorators -> example my_logger and my_timer
#
from functools import wraps
	# to preserve information of the original_func in decorators use functools module wraps
	# wraps -> using decorator inside of a decorator
	# decorate all of the wrappers() with wraps() deorator
def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)

	@wraps(orig_func)
	def wrapper(*args,**kwargs):
		logging.info('Ran with args: {}, and kwargs {}'.format(args,kwargs))
		return orig_func(*args,**kwargs)
	return wrapper

def my_timer(orig_func):
	import time

	@wraps(orig_func)
	def wrapper(*args,**kwargs):
		t1=time.time()
		result=orig_func(*args,**kwargs)
		t2=time.time()-t1
		print(f'{orig_func.__name__} ran in {t2} secs')
		return result
	return wrapper

@my_logger
@my_timer 	
# Way to Chain Decorators is Stacking
	# but problem with stacking is , since 
		# @my_logger is equivalent to -> display_info=my_logger(display_info)
		# on stacking decorators it becomes
			# display_info=my_logger(my_timer(display_info))
				# thus return type of my_timer is wrapper of my_timer which goes as parameter param to my_logger which on otherhand needs the original function display_info() otherwise .__name__ is wrong and args are wrong therefore use
					# from functools import wraps
					# @wraps(orig_func)  -> above each wrapper of stacked decorator to resolve wrapper to stick to original function and not the stacked(()) returned output of inner decorator
	# @my_logger
	# @my_timer Stack is equivalent equibalent to
		# display_info=my_logger(my_timer(display_info))
		# lower ones in the stack are innermost() and get executed first than the higher ones on the stack
			# keep time sensitive innermost inside to execute first

def display_info(name,age):
	print(f'display info ran with arguments ({name},{age})')

print(display_info.__name__)
display_info('john',25)