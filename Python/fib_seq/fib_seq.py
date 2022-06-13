def fib_seq(*end):
	if not end:
		return None
	if not end[0]:
		return []
	if end[0] == 1:
		return [0]


	a,b = 0,1
	res = [a,b]
	for i in range(end[0] - 2):
		c = a + b 
		res.append(c)
		a,b = b,c
		

	return res

