import re 
def complex_to_tuple(param):
	res = [] 
	for i in range(len(param)):
		if param[i] in "+-" and i != 0:
			a,b = param[:i], param[i:].strip("i").strip("+")
			a,b = int(a), int(b)
			return (a,b)
		