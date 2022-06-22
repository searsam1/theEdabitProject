import re 

def string_expansion(txt):
	
	current_n = 1
	string = "" 

	for char in txt:
		if char.isnumeric():
			current_n = int(char)

		else:
			string += char * current_n
	return string



	

string_expansion("cvyb239bved2dv")


