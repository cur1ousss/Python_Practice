# Earlier seens arguments into wrapper function of decorator
# now look into arguments into Decorator

# basic hello world in flask with Arguments passed to Decorators
from flask import Flask
app = Flask(__name__)


@app.route("/") # app route decorator with / string arg
def hello():
    return "Hello World!"


@app.route("/about") # app route decorator with about page string url
def about():
    return "About Page"

if __name__ == "__main__":
    app.run()



# basic Decorator
def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print('Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print('Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)
display_info('Travis', 30)

# adding customised prefix to the print statements in the wrapper -> example of using argument to the decorator since that argument will be the prefix/prefux

def prefix_decorator(prefix):
	def decorator_function(original_function):
		def wrapper_function(*args, **kwargs):
			print(prefix,'Executed Before', original_function.__name__)
			result = original_function(*args, **kwargs)
			print(prefix,'Executed After', original_function.__name__, '\n')
			return result
		return wrapper_function
		# Everything nested here has access to prefix variable argument
	# since nested need to return decorator as well
	return decorator_function

# @decorator_function -> incase of arguments to decorator use outside function to take arguments
@prefix_decorator('TESTING_prefix:') # display_info=prefix_decorator('LOG: ')(display_info)
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)
display_info('Travis', 30)

# @prefix_decorator('LOG:') equivalent to display_info=prefix_decorator('LOG: ')(display_info)