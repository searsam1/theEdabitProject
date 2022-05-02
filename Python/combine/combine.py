def combine(lst):
	FSA = {}
	for l in lst:
		FSA[l[0]] = ["0","1"]
	for l in lst:
		if l[1] == 1:
			FSA[l[0]][1] = l[2]
		elif l[1] == 0:
			FSA[l[0]][0] = l[2]
	return FSA
# example tests

