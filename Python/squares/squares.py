import math

def squares(a, b):
	a_copy,b_copy = a,b
	while math.sqrt(a) != int(math.sqrt(a)):
		a += 1
	while math.sqrt(b) != int(math.sqrt(b)):
		b += 1
	res = math.sqrt(b) - math.sqrt(a)
	
	if res < 2:
		if math.sqrt(a_copy) == int(math.sqrt(a_copy)):
			res += 1
		if math.sqrt(b_copy) == int(math.sqrt(b_copy)):
			res += 1
	return res
