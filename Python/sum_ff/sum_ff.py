def factors(n):
	return [i for i in range(2,int(n/2) + 1) if not n % i]

def is_prime(n):
	for i in range(2,int(n**.5) + 1):
		if not n % i:
			return False
	return True

def sum_ff(a):
	facts = factors(a)
	facts = sum(sum((factors(i) for i in facts), start=[]))
	return facts
sum_ff(12)