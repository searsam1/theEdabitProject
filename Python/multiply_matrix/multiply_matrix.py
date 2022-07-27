def multiply_matrix(m1, m2):
	if len(m1[0]) != len(m2):
		return "ERROR"
	cols = []
	for i in range(len(m1)):
		row = [] 
		for j in range(len(m2)):
			row.append(m2[j][i])
		cols.append(row)
	matrix = []
	for row in m1:
		temp = [] 
		for col in cols:
			x = sum(i[0]*i[1] for i in list(zip(row,col)))
			temp.append(x)
		matrix.append(temp)
	return matrix



assert multiply_matrix([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]) == [[30, 36, 42], [66, 81, 96], [102, 126, 150]]

[
	[1,2,3], [1,2,3]
	[4,5,6], [4,5,6]
	[7,8,9], [7,8,9]
],

[
	[30, 36, 42], 
	[66, 81, 96], 
	[102, 126, 150]]



[[1,2,3],[4,5,6],[7,8,9]]


print("Test Passed.")

