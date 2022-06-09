

def factorial(n):
	k = 1
	while n > 1:
		k *= n
		n -= 1
	return k

def get_catalan_number(n):

	numerator = factorial(2*n)
	denominator = factorial(n+1) * factorial(n)
	return numerator / denominator



print(get_catalan_number(10))


