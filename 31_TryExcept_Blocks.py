# Basic Structure
try:
	pass
except Exception:
	pass
else:
	pass
finally:
	pass		
		# pass Keyword is filler since can't leave Empty use pass keyword


# useful to handle exceptions >> does not throw stack trace in terminal instead shows End user readable basic Error

try:
	f=open('WrongFile.txt')
except Exception:
	print('Error! File Name wrong')
		# Exception 
			# is general exception will catch all exceptions
				# but better to use Specific Excpetion NameType to know what kind of error


# Using Multiple Exceptions
	# Exceptions fall through from Top to Bottom checked

try:
	f=open('WrongFile.txt')
	var=badVar	
except FileNotFoundError as e:
	print('Error! File Name wrong File Not FOund')
	print(e)
except Exception as e:
	print(e)	
		# use General Exception at End otherwise won't fall through specific if general placed Above


	# if both lines have exceptions , exception caught at intial first line will be captured and reported
try:
	f=open('WrongFile.txt')
	var=badVar	
except Exception as e:
	print(e)	
	

# else clause
	# used to run code in case try block does'nt raise an/throw exception
	# else clause only runs if we don't throw an exception
try:
	f=open('Exp.cpp')
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print(f.read())
	f.close()

# finally clause
	# runs no matter if exception raised or not
	# used to generally release resources example file close, database close etc
try:
	f=open('Exxp.cpp')
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print(f.read())
	f.close()
finally:
	print('Exceuted Last Closed File')
	f.close()


# Raising Custom Exceptions
try:
	f=open('Corruptt.cpp')
	if f.name=='CorruptFile.txt':
		raise Exception
except FileExistsError:
	print('Tatti')
except Exception as e:
	print('Custom Print for exception')