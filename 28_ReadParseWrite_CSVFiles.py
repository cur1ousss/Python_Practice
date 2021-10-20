# CSV Comma separated values
	# delimiter example comma used to separate values, tab , - etc
	# first line contains field names
	# second line onwards values

# https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files

import csv

with open('names.csv','r') as csv_file:
	csvReader=csv.reader(csv_file)
		# csv.reader() uses dialect in background that expects values to be of certain format

	print(csvReader) # just an object in memory Need to iterate for human readable

	next(csvReader)
		# shifting/skipping to next line to ignore First line Filed Parameter name - from concept of generators

	for line in csvReader:
		print(line[2])
	

# writing to new CSV using ' - ' delimiter
import csv

with open('names.csv','r') as csv_file:
	csvReader=csv.reader(csv_file)
		# csv.reader() uses dialect in background that expects values to be of certain format

	print(csvReader) # just an object in memory Need to iterate for human readable

	with open('New_Names.csv','w') as newFile:
		csvWriter=csv.writer(newFile,delimiter='-')
			# csv.writer(FileX,delimiter='')
		csvWriter=csv.writer(newFile,delimiter='\t')
			

		for line in csvReader:
			csvWriter.writerow(line)
			# advantage of csv writer and csv reader instead of normal string parsing ->
				# since email might contain ' - ' the csv module automatically puts " " quotes around those values so when read they are known as whole values and not split wrong
	

# reading csv file with wrong delimiter
import csv

with open('New_Names.csv','r') as csv_file:
	csvReader=csv.reader(csv_file)
		# reading \t as , separated wrong format delimiter
			# file elements will be read as whole since no , found
				# therefore need to specify correct delimiter
	for line in csvReader:
		print(line)

with open('New_Names.csv','r') as csv_file:
	csvReader=csv.reader(csv_file,delimiter='\t')
			# using delimter in csv.reader(file,delimiter='\t')
	
#***************************************************************************** 

# Dictionary Reader Dictionary Writer - preferred by Corey over CSV reader CSV writer
	
	# DictReader
with open('names.csv','r') as csv_file:
	csvReader=csv.DictReader(csv_file)
			# using DictReader the field names are now Keys and the rows are values for those keys
	for line in csvReader:
		print(line)
	for line in csvReader:
		print(line['email'])
			# referring values using 'email' key

	# DictWriter
		# need to pass field names as keys in DictWriter not needed in DictReader
with open('names.csv','r') as csv_file:
	csvReader=csv.DictReader(csv_file)

	with open('new_namesD.csv','w') as newFile:
		fieldNames=['first_name','last_name','email']

		csvWriter=csv.DictWriter(newFile,fieldnames=fieldNames,delimiter='\t')

		csvWriter.writeheader()
			# writing fieldNames as first line header
		
		for line in csvReader:
			csvWriter.writerow(line)


	# writing only specific columns fields using DictWriter
		# using limited fieldnames and deleting key in DictWrite writerow
		# using 2 dictionary copy limited fields key to other
with open('names.csv','r') as csv_file:
	csvReader=csv.DictReader(csv_file)

	with open('new_namesD.csv','w') as newFile:
		fieldNames=['first_name','last_name']
				# remove field from FieldNames and then delete it later from Dict while writing

		csvWriter=csv.DictWriter(newFile,fieldnames=fieldNames,delimiter='\t')

		csvWriter.writeheader()
			# writing fieldNames as first line header
		
		for line in csvReader:
			del line['email']
				# deleting email key
			csvWriter.writerow(line)