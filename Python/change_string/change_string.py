
# from string import ascii_uppercase
import string
str_asc_up = string.ascii_uppercase
d = {j : i for i,j in enumerate(str_asc_up)}
d_r = {i : j for i,j in enumerate(str_asc_up)}

def change_string(s):
	
	key = d
	res = [i.upper() if 
			i.islower() 
				else 
				d_r[d[i] + 1 if d[i] != 25 else 0]
				for i in s][::-1]
	return "".join(res)
	
