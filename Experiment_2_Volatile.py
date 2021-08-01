list_Courses=["Computer Science","Maths","Physics","Biology","Chemisty"]

str_List="- ".join(list_Courses)

print(str_List)

new_List=str_List.split(" - ")

print(new_List)

str_list=" - ".join(list_Courses) # OP >> Computer Science - Maths - Physics - Biology - Chemisty
	# "left_Half_PrevTerm (Separator like - , ) Right_Half_NextTerm"

print(str_list)

new_List=str_list.split("-")

print(new_List)