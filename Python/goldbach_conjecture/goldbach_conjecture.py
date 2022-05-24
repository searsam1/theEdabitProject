#
is_prime = lambda n : all( bool(n % i) for i in range(2,int(n**.5)+1) )
def goldbach_conjecture(n):
	if n % 2 or n <= 2:
		return []
	for i in range(2,n):
		if is_prime(i) and is_prime(n - i) and i + (n-i) == n:
			return [i, n-i]
#