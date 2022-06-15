def digits_count(n):
	n = abs(n)
	if n < 10:
		return 1
	total = 1
	while n > 10:
		n //= 10
		total += 1
	return total