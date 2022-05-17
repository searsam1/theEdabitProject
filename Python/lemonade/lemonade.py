def lemonade(bills):
	total = 0
	for bill in bills:
		change = bill - 5
		total -= change
		if total < 0:
			return False
		total += 5
	return True
	