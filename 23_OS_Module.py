# Os Module
	# allows to interact with underlying Operating system -
		# navigate file system and add change move
		# look and change evironment variables

# dir() - shows attributes and methods of the passed Object
import os
print(dir(os))

# os.getcwd() - print current working directory
print(os.getcwd())

# os.chdir('path') - change working directory
os.chdir('/home/cyberpunk/A_HOME/ADevNLearning/Python_Practice')
print(os.getcwd())

import os

print('F strings in functions os.mkdir() and os.makedirs()')

print(f'Current working Directory is {os.getcwd()}')




# os.listdir('Path') - if path not passed by default lists contents of current working directory otherwise lists contents of path passed
print(os.listdir()) # output as list

# # Making New Folder

	# os.makedirs() - makes intermediate level directories if they don't exist
	# os.mkdir() - error if intermediate level directories don't exist

# os.mkdir('TopFolder/DeezNuts') # Creates Single level file hence error in this since TopFolder does'nt exist
os.mkdir(f'{os.getcwd()}/MkdirFString') 
	# custom Path F Strings and os.mkdir() os.makedirs() 
os.mkdir('TempMkDir') # works
os.makedirs('/home/cyberpunk/TestPythonTmp/MakeDirsLevel1/MakeDirsSubLevel') # Create Sub Deep Level Top Directories Structure as well if they don't exist

# proceeding from makedirs and mkdir after

os.mkdir('Toplevel/SubDir1') # Error since Toplevel Folder dir does'nt exist
os.makedirs('Toplevel/SubDir1') # Creates Toplevel folder dir if does'nt exist
	
	# os.makedirs() - useful for tree structure directories

# Deleting Removing Folders
os.rmdir('PathTop/SubDir1') # will not remove intermediate directories
os.removedirs('PathTop/SubDir1') # will remove intermediate directories
	
	# os.rmdir() - better since can remove specific
	# os.removedirs() - dangerous since sub Top structure also deleted

print(os.listdir())

# Rename File or Folder
os.rename('OldName.txt','NewName.txt')

# Information about file
x=os.stat('Python.txt')
print(x)

size=os.stat('Python.txt').st_size	# size returned in Bytes
print(size)

# last modification time - os.stat('File.txt').st_mtime
	# returned in computer format Convert to human readable

import os
from datetime import datetime

modif_time=os.stat('FilePath/FileName.txt').st_mtime
print(datetime.fromtimestamp(modif_time))

# To see entire File directory tree and files within desktop Traverseing files
os.walk()
	# os.walk() is a generator that yeilds a tuple() of 3 values as its walking the directory tree
	# directory path
	# directories within that path
	# and files within that path

# By default os.walk() traverses from Top Down
import os

for dirpath,dirnames,filenames in os.walk('Begining/Path/Folder'):
	print('Current Path : ',dirpath)
	print('Directories : ',dirnames)
	print('Files : ',filenames)
	print('---------------------------')

	# can use to custom Implement Search File or Folder Option

# Access Home Directory location by grabbing Home Evironment Variable

print(os.environ) # prints all Environment variables
print(os.environ.get('HOME'))	

	# create New File in Home Directory -- to continue more using Fwrite
newFilePath=os.environ.get('HOME') + 'NewFile.txt'
print(newFilePath)
	# problem with this Approach hard to remember and Not Consistent for ' / ' positions may give error if no / between 2
	# so use path module for consistency among various os

file_path=os.path.join(os.environ.get('HOME'),'NewFile.txt')

print(os.path.basename('/tmp/File.txt'))  # grab file name of any path we're working on , does'nt have to be a real path
os.path.dirname('tmp/Subdir/File.txt') # dirname gives Top Directory Name

os.path.split('Path/into/File.txt') # gives comma separated path / elements
os.path.splitext('Path/into/File.txt') # split path different and Extension of file separate
# check if path exists
os.path.exists('Path/to/File.txt')	# Returns True False

os.path.isdir()
os.path.isfile()

print(dir(os.path))