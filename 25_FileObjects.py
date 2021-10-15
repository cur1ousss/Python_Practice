# usually recommended Context Manager to open files 

# same directory file can open with Direct Name
	# for file in Other directories pass full Path
filex=open('25FileSample.txt')
	# by default file Opens in Reading Mode
filex=open('25FileSample.txt','r')

print(filex.name)
	# print name of file
print(filex.mode)
filex.close() 
	# need to explicitly close file
	# if not closed then end up with leaks that run over the maximum allowed file descriptiors on your system and applications could throw and error

# Opening File using Context Manager
with open('25FileSample.txt','r') as filex:
	# benefit of context manager >> file access limited to this block as soon as exit out of block file automatically closed hence no leaks
	# will also close file in case of Exceptions
	pass

# we still have access to filex variable out of that block but file remains closed
print(filex.closed) 
	# returns True/False in case file is closed 


with open('25FileSample.txt','r+') as f:
	fContents=f.read()
		# loads all contents of file into memory so can run out of memory for large files
			# for large files not good approach use other methods - filex.readlines() ....
	# print(fContents) # works

print(fContents)	# works

with open('25FileSample.txt','r+') as f:
	fContents=f.readlines()
	print(fContents)
		# .readlines() - returns list of contents of file separated by '\n'
	
	fContents=f.readline() 
		# grabs single line from file
			# everytime run gets the next line
	fContents=f.readline()
			# reads next 2nd line

	for line in f:
		print(line,end=' ')	# reads line by line


with open('25FileSample.txt','r+') as f:
	fContents=f.read(100)
		# can pass size of characters to be read from file in file.read()
			# space is 1 character size
	print(fContents)

	fContents=f.read(100) # will read next Characters 100 Since file pointer will pick off from where left earlier
	print(fContents)

	# read() returns empty string when reach end of file 
	f.read(100) # won't have any effect

	# reading File in Chunks loop
with open('25FileSample.txt','r+') as f:
	sizetoRead=100
	fContents=f.read(sizetoRead)

	while len(fContents) > 0:
		print(fContents,end=' ')
		fContents=f.read(sizetoRead)

	print(f.tell())
		# file.tell() returns index/position of file pointer

	f.seek(0)
		# fileN.seek(int) - used to set position of filePointer anywhere

#*****************************************************************************

# Writing to Files

	# cannot write to file in r mode
		# set to w or r+

# if file Not exists w mode will create New file
# if file exists w mode will Overwrite file contents
	# then use a mode for appending if file Exists
with open('25FileWrite.txt','w'):
	pass	# gives no error but cannot refer by name has no use

with open('25FileWrite.txt','w') as f:
	f.write('Test')	
	f.write('\nR') # will write where pointer left off above # overwrites only when invoking w mode 
	
	f.seek(0)
	f.write('R')
		# will turn Test -> Rest  // won't overwrite whole line but only as many characters passed


#*****************************************************************************

# Reading Writing on Multiple Files
	# Nesting File Operations
with open('25FileSample.txt','r') as rf:
	with open('25SampleCopy.txt','w') as wf:
		# can merge above both lines but readablity also important
		for line in rf:
			wf.write(line)

# Copying a large Picture file
	# cannot simply imagex.open() need to Open image in Binary mode
	# https://docs.python.org/3/library/functions.html#open
with open('25pepeTest.jpeg','rb') as pepeImg:
	# rb as read mode binary
	with open('25pepeTestCOPY.png','wb') as pepePng:
			# Jpeg to png allowed ? yes more study cross format needed 
				# can cross format as .txt but unreadable in text editor notepad
		# pepePng.write(pepeImg) # TypeError: a bytes-like object is required, not '_io.BufferedReader'
		for pepe in pepeImg:
			pepePng.write(pepe)
		
# Chunking on image
with open('25pepeTest.jpeg','rb') as pepeImg:
	# rb as read mode binary
	with open('25pepeTestCOPY.png','wb') as pepePng:
		# pepePng.write(pepeImg)
		
		chunkSize=4096 # can choose any
		rfChunk=pepeImg.read(chunkSize)

		while len(rfChunk) > 0:
			pepePng.write(rfChunk)
			rfChunk=pepeImg.read(chunkSize)
		

		
		for pepe in pepeImg:
			pepePng.write(pepe)