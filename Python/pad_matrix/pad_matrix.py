def pad_matrix(matrix):
	res = [0 for i in range(len(matrix[0]) + 2)]
	res = [res] + [[0] + lst + [0] for lst in matrix] + [res]

	return res