def swap_cards(n1, n2):
	low = str(min(int(i) for i in str(n1)))
	high = str(n2)[0]
	n1, n2 = str(n1), str(n2)
	idx = n1.index(low)
	if idx == 0:
		n1 = high + n1[1]
	else:
		n1 = n1[1] + high
	n2 = low + n2[1]
	return n1 > n2
