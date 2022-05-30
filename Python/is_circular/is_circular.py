from itertools import permutations

def check(lst):
	if len(lst) < 2:
		return False
	elif len(lst) == 2:
		return lst[0][0] == lst[-1][-1] and lst[0][-1] == lst[1][0]
	res = [] 
	for i in range(1, len(lst)):
		ele1, ele2 = lst[i-1][-1], lst[i][0]
		res.append(ele1 == ele2)
	res.append(lst[0][0] == lst[-1][-1])
	return all(res)

def is_circular(lst):
	perms = permutations(lst, len(lst))


	for i in perms:
		if check(i):
			return True
	return False

is_circular([[1,2,3],[3,4,4,4,4,4,5],[3,4,4,4,4,4,5],[3,4,4,4,4,4,5],[1,2,3]])

