def combine_lists(*arr):

	def padded(arr):
		l = len(max(arr, key=len))
		for lst in arr:
			while len(lst) != l:
				lst.append("*")
		return arr

	def combined(lst):
		arr = []
		for i in range(len(lst)):
			col = []
			for j in range(len(lst)):
				col.append(lst[j][i])
			arr.append(col)
		return arr
		
	return combined(padded(arr))
#
"""
	afairwell2pawns
	
	from itertools import zip_longest

	def combine_lists(*matrix):
		return list(map(list, zip_longest(*matrix, fillvalue='*')))

"""