
from itertools import combinations,permutations

def f(n):
	
	arr = [j for j in range(1,n+1) for i in range(2)]
	perms = list(set(permutations(arr,2)))
	geo_mean = lambda a,b : int((a*b)**.5) == (a*b)**.5
	res = []

	for perm in perms:
		a,b = perm
		res.append(geo_mean(a,b))

	total = res.count(True) / len(res)
	return total