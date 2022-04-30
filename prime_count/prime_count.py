primes = {3}

def is_prime(n):
	if n in primes: # works because we call it in prime_counts scope
		return True #					where we already defined primes
	if all(n % i for i in range(2,int(n**.5) + 1)):
		primes.add(n)
		return True
	return False
def prime_count(a, b, primes=primes):
	total = 0 
	for i in range(a+1,b+1):
		if is_prime(i):
			total += 1
	return total	


prime_count(1,100)
prime_count(1,100000)
prime_count(1,10000000)
