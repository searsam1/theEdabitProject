def all_pairs(lst, target):

	res = []
	while lst:
		ele = lst.pop(0)
		for j in lst:
			if ele + j == target:
				res.append(sorted([ele,j]))
	res = sorted(res, key=lambda x : min(x))
	return res

