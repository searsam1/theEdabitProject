import re

def depth(lst):
	
	count = 0
	if type(lst) == list:
		count += 1
	else:
		return count
	for i in lst:
		
		if type(i) is list:
			print(count)
			count += depth(i)
		
	return count


	




print(
	depth( [1, 2, 3, 4, [[5]], [[6]], 7] )
	)
