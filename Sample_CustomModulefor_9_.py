print("Imported custom_Module")

test="Test String"

def find_index(toSearch,target):
	"""Find index of a value in Sequence"""
	for i,value in enumerate(toSearch):
		if(value==target):
			return 1
	return -1
