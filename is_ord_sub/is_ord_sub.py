def is_ord_sub(smlst, biglst):
	
	while smlst[0] != biglst[0]:
		biglst.pop(0)
		if not len(biglst):
			break
		smlst.pop(0)
		if not len(smlst):
			break