def is_autobiographical(n):
	res = [] 
	for i in range(len(str(n))):
		res.append( str(str(n).count(str(i))) )
	res = int("".join(res))
	return res == n