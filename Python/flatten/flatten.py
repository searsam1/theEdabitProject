
def flatten(r):	
	
	# res = lambda r : sum([flatten(i) for i in r], []) if type(r) is list else [r]
	# Credit: Deep Xavier

	if type(r) is list:
		return sum([flatten(i) for i in r], [])
	else:
		return [r]


		


x = flatten([[1,2,3,4],[5,6,7,8,[9,10,11,12]]])
print(x)


