def sqr_digits(n):

	s = sum(int(i)**2 for i in str(n))
	return s

def is_happy(n):
	while n > 1 and n != 4: 
		n = sqr_digits(n)
	return n == 1
	
	



is_happy(89)