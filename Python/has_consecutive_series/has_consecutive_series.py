import numpy as np

def has_consecutive_series(v1, v2):
	
	mn, mx = min([v1,v2], key=len), max([v1,v2], key=len)
	if mn == mx:
		mn,mx = v1, v2
	else:
		while len(mn) < len(mx):
			mn.append(0)
	arr1, arr2 = np.array(mn), np.array(mx)


	combined_vector = arr1 + arr2
	print(combined_vector)
	check = all(abs(combined_vector[i-1] - combined_vector[i]) == 1
		for i in range(1,len(combined_vector))
	)
	return check
x = has_consecutive_series([1, 2, 3], [1, 1, 1])
print(x)