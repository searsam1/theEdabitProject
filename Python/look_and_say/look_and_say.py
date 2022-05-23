
def look_and_say(term):
	"""
		"1211" > ["1", "2", "11"]
				one 1  one 2  two 1's
				1   1  1   2  2    1
				111221
	"""
	groups = [] 
	container = [] 
	for i in range(1, len(term)):
		e1, e2 = term[i-1], term[i]
		if e1 == e2:
			container.append(e1)
		else:
			container.append(e1)
			groups.append(container)
			container = [] 
	container.append(e2)
	groups.append(container)	
	print(groups)
	res = [str(lst.count(lst[0])) + lst[0] for lst in groups]
	res = "".join(res)
	return res

