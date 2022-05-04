from itertools import combinations
def is_ord_sub(smlst, biglst):
	combs = combinations(biglst, len(smlst))
	return tuple(smlst) in combs
		
		