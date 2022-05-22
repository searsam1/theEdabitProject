def can_build(digits, lst):
	

	d = {count : idx for count,idx in enumerate(digits)}
	
	s = "".join(str(i) for i in lst)

	res = [] 
	for digit in set(s):
		digit = int(digit)
		correct_count = d[digit]
		actual_count = s.count(str(digit))

		if actual_count > correct_count:
			return False
	return True

		
	

x = can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 80, 0])
print(x)