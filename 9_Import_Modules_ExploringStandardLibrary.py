# ***************************************************************************** 
import Sample_CustomModulefor_9_
	# since created in Same Directory can Directly Import Module

courses=["History","Math","Sciences"]

	# moduleName.function() cannot directly call function()
index=Sample_CustomModulefor_9_.find_index(courses,"Math")
print(index)

# to Shorten moduleName.function() everytime use Aliases while importing Module
import Sample_CustomModulefor_9_ as s_module

index=s_module.find_index(courses,"Hindi")
print(index)


# importing Function() itself >> to shorten writing and Direct call Function

from Sample_CustomModulefor_9_ import find_index  # only gives access to that particular Function Not other components

index=find_index(courses,"Marathi")
print(index)

# Importing Multiple components>> Function,Variable
from Sample_CustomModulefor_9_ import find_index,test	

print(test)

# Aliasing Imported Function

from Sample_CustomModulefor_9_ import find_index as fi

index=fi(courses,"Ruski")
print(index)

# importing Everything from Module
	# generally not used since creates confusion if same name function is the one imported or local while debugging
from Sample_CustomModulefor_9_ import *

print(test)

# *****************************************************************************
# Import >> import checks multiple locations listed in list >> sys.path

import sys
print(sys.path)

import Experiment_Module 	# Module located in Same Directory works Directly 

import Experiment_Module_Folder 
	# cannot >> import Experiment_Module_inFolder
import Experiment_Module_Folder.Experiment_Module_inFolder
	# For Modules in SubDirectories in Same Directory need to Import folderName.moduleName Chaining

# if try to Import module Not installed or Hidden in Sub Directory get Error

# to fix Import error
	# Inserting into sys.path list
	# Editing Environment Variable

import sys
sys.path.append("Path_to_Module")
	# not best approach since Temporary also if we need module multiple times need to hardcode and reapeat it multiple times
		# Edit Environment Variable

# Sys.path secondly looks into Python Path Environment Variable
		# $PATH export for Linux
		# Env Var in settings for Windows

# *****************************************************************************

# Standard Library

# random >> standard library module

import random

courses=["Hindi","Math","Sciences","Tamil"]

randomCourse=random.choice(courses)
print(randomCourse)

# math >> module for mathematical Calculations

import math

# deg to radian

rads=math.radians(90)
print(rads)
print(math.sin(rads))

# calendar 
# datetime module 

import datetime
import calendar

print(datetime.date.today())

print(calendar.isleap(2017))

import os

print(os.getcwd())  # current working directory

# library modules are .py files as well
	# print their location using __ dunder
print(os.__file__)

import antigravity  # antigravity joke module opens Webcomic for Python Joke meme


# FINISHED BASICS >>> 9 Videos https://www.youtube.com/watch?v=xFciV6Ew5r4&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=9
	# After this watch videos according to Interest and Need unordered
	
#X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X* 