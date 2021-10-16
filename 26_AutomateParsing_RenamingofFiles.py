# Have File list
# Earth - Our Solar System - #4.mp4
# Jupiter - Our Solar System - #10.mp4
# Uranus - Our Solar System - #7.mp4
# Venus - Our Solar System - #5.mp4
	# need to order rename them by number first and remove - and #

import os

os.chdir('Path/to/FoldercontainingFiles/Videos')

for f in os.listdir():
	f_name,f_ext=os.path.splitext(f)
			# splittext() returns tuple of FileName and Extension	
	f_title,f_course,f_num=f_name.split('-') 
		# removing -
			# can also f_title,f_course,f_num=f_name.split(' - ') 
	f_title=f_title.strip()
		# .strip() to remove trailing and heading spaces
	f_course=f_course.strip()
	f_num=f_num.strip()[1:].zfill(2)
		# .strip()[1:]
			# to strip # omiting 0 pos on # and get from 1 to end position data only
			# sorting by file name 1 and 10 will be close hence need to pad 0 for single digit numbers using zfill(2) 2 digits wide

	new_name='{}-{}{}'.format(f_num,f_title,f_ext)

	os.rename(f,new_name)