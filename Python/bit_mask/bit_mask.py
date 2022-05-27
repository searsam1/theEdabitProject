def bit_mask(n, b):
	
	
	bits = "{0:b}".format(n).rjust(b+1, "0")[::-1][b]
	return bits
	

bit_mask(1,10)
