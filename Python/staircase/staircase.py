#
def staircase(n):
	is_neg,n,string = n < 0,abs(n), ""
	
	for i in range(1,n+1):
		left = (n-i) * "_"
		right = i * "#"
		
		if is_neg:
			left,right = right, left

		s = left + right + "\n"
		string += (s)
		
	return string.strip("\n") if not is_neg else string.strip("\n")[::-1]
#