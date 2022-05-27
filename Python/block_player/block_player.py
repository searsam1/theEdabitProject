def block_player(a, b):
	arr = [
	[0,1,2], 
	[3,4,5], 
	[6,7,8]]
	
	rows = arr
	cols = []

	for i in range(len(arr)):
		col = [] 
		for j in range(len(arr[i])):
			col.append(arr[j][i])
		cols.append(col)
	
	diagonal_left = [] 
	for i in range(len(arr)):
		diagonal_left.append(arr[i][i])
	
	diagonal_right = [] 
	for i in range(len(arr)):
		diagonal_right.append(arr[i][-i-1])
	
	matrix = rows + cols + [diagonal_right] + [diagonal_left]
	
	res = [] 
	for lst in matrix:
		if a in lst and b in lst:
			res = lst
			break
	for i in res:
		if i not in [a,b]:
			return i


print(block_player(0,8))


