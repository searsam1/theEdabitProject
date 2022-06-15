def is_factorial(n):
	i = 1
	l = [] 
	while not n % i:
		l.append(i) 
		i += 1

	res = 1
	for i in l:
		res *= i
		if res == n:
			return True
	return res == n