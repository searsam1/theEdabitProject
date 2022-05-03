def babbage(n):
	i = 0
	n_copy = n

	while not str(n**.5).endswith(".0"):
		i += 1
		n = str(i) + str(n_copy)
		n = int(n)
	if n_copy == 269696:
		return ["Babbage was incorrect!","Babbage was correct!"][n**.5 == 99736]
	return n**.5



print(babbage(481))