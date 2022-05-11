def split_n_cases(txt, cases):
	if len(txt) % cases:
		return ["Error"]
	step = len(txt) // cases
	res = [txt[i:i+step] for i in range(0,len(txt), step)]
	return res
	