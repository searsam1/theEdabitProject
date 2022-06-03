
def semi(n):
	print(n)
	if n in [1,2]:
		return n
	return n * semi(n-2)

def alt(n):
	if n in [1,2,-1,-2]:
		return n
	return n - ( alt((n-1) * -1 ))

	
def alt_semi(n):
	return alt(n) - semi(n)


print(alt(4))