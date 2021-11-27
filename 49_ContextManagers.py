# Context Managers help managing resources
	# handle teardown of resources

# normal way of file handling
f=FileExistsError
f.open()
f.write()
f.close()

# using context manager -> automatically closes file resource even if we get an error
with open():
	f.write()

# context Manager Uses
	# databases
	# apply release locks

#----------------------------------------------------------------------------- 
# Writing Custom Context Managers
	# using class
	# using function with a decorator

	
# in below examples replicating functionailty of open() function in context manager of files
	# Custom Context Manager using class
class OpenFile():
	def __init__(self,filename,mode):
	    	self.filename=filename
		self.mode=mode

	def __enter__(self):
		self.file=open(self.filename,self.mode)
		return	self.file
			# returning object we are working with within the context manager
				# ? returning object of context manager type	

	def __exit__(self,exc_type,exc_val,traceback):
		self.file.close()


with OpenFile('49_sample.txt','w') as f:	# f is a file object within the context manager returned
	f.write('Testing')

print(f.closed)

#----------------------------------------------------------------------------- 
# Custom Context manager using a function 

from contextlib import contextmanager

@contextmanager
def open_file(file,mode):
	f=open(file,mode)
	yield f	# upto here similar to __enter__() method of above custom context manager class
	f.close()	# teardown code

with open_file('49_sample.txt','w') as f:	# f is a file object within the context manager returned
	f.write('Testing')
# when exited with clause , everything after yield executed
print(f.closed)

# including try except block -> finally will get executed in case if execeptions faced
from contextlib import contextmanager

@contextmanager
def open_file(file,mode):
	try:
		f=open(file,mode)
		yield f	# upto here similar to __enter__() method of above custom context manager class
	finally:
		f.close()	# teardown code

with open_file('49_sample.txt','w') as f:	# f is a file object within the context manager returned
	f.write('Testing')
# when exited with clause , everything after yield executed
print(f.closed)

#-----------------------------------------------------------------------------
# P >> cd dir then back
 
import os
from contextlib import contextmanager

cwd=os.getcwd()
os.chdir('49_sampleDir_1')
print(os.listdir())
os.chdir(cwd)

cwd=os.getcwd()
os.chdir('49_sampleDir_2')
print(os.listdir())
os.chdir(cwd)