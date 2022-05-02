def id_mtrx(n):
	if type(n) != int:
		return "Error"
	
	is_neg = False
	if n < 0:
		n *= -1
		is_neg = True
	arr = [] 
	for i in range(n):
		row = [] 
		for j in range(n):
			row.append(int(i == j))
		arr.append(row)
	if is_neg:
		{i.reverse() for i in arr}
	return arr