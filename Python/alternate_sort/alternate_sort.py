def alternate_sort(lst):
	ints = sorted(i for i in lst if type(i) is int)
	chars = sorted(i for i in lst if type(i) is str)
	arr = list(zip(ints, chars))
	res = [] 
	for lst in arr:
		for ele in lst:
			res.append(ele)
	return res

alternate_sort(["X", 15, 12, 18, "Y", "Z"])