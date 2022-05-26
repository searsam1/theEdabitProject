def phi(n):
	factors = lambda n : [i for i in range(1,n+1) if not n % i]
	main = factors(n)

	gcf = 0
	for i in range(n, -1, -1):
		f = factors(i)
		
		f = [i for i in f if i in main]
		if f == [1]:
			gcf += 1
	return gcf

	

phi(9)
