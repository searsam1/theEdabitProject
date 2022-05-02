import math

def check_power2(n):
	if n == 1:
		return True
	x = 2	
	check = lambda n : int("".join(sorted(str(n),reverse=True)))

	while x < (n*4):
		if check(x) == check(n):
			return True
		x *= 2
	return check(x) == check(n)
