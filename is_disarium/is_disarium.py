def is_disarium(n):
	
	i = 1
	arr = [] 
	for number in str(n):
		number = int(number) 
		number = number ** i 
		arr.append(number)
		i += 1 
	return sum(arr) == n
