def zipper(lst1, lst2):
	if lst1 == lst2:
		return True
	if lst1[-1] != lst2[-1]:
		return False
	l1, l2 = lst1, lst2
	if len(lst1) < len(lst2):
		l1, l2 = lst2, lst1

	offset = 0 

	while len(l1) > len(l2):
		l2.insert(0, "f")
		offset += 1
	z = list(zip(l1,l2))
	for i in range(len(z)):
		tup = z[i]
		if len(set(tup)) == 1:
			print(tup)
			i -= 1
			return [i-offset,i]


