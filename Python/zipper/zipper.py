def zipper(lst1, lst2):
	
	
	l1, l2 = "".join(str(i) for i in lst1), "".join(str(i) for i in lst2)
	
	for i in range(len(l1)):
		if l1[i:] in l2:
			l2_idx = l2.index(l1[i:]) - 1
			l1_idx = i - 1
			return [l1_idx, l2_idx]




print(zipper(
	[5, 5, 7, 8, 9, 1, 2], 
	[3, 2, 1, 1, 6, 6, 6, 6, 1, 2]
	))

