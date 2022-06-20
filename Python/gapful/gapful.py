def is_gapful(n):
	return not n % int(str(n)[0] + str(n)[-1])

def gapful(n):
	
	if n <= 100:
		return 100
	n_copy = n
	lower = [] 
	upper = [] 

	while not is_gapful(n_copy):
		n_copy -= 1
	lower.append(n_copy)
	n_copy = n
	while not is_gapful(n_copy):
		n_copy += 1
	upper.append(n_copy)
	
	if lower[0] == upper[0]:
		return n
	if n - lower[0] <  upper[0] - n:
		return lower[0]
	elif n - lower[0] >  upper[0] - n:
		return upper[0]
	else:
		return lower[0]

