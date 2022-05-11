import re 

def find_glasses(lst):
	
	p = "O(-+)O"
	for s in lst:
		for i in re.findall(p,s):
			if len(set(i)) == 1:
				return lst.index(s)

print(find_glasses(['OOOO----~OOO', '-------', 'OOOOOOO', 'OO-OO-OO-O']))