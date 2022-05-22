def max_consec(lst):
	lst = sorted(set(lst))
	s = sorted(lst)
	offset = 0
	for i in range(1, len(s)):
		e1 = s[i-1]
		e2 = s[i]

		if abs(e1 - e2) != 1:
			lst.insert(i + offset, "$")
			offset += 1
	lst = " ".join(str(i) for i in lst)
	lst = lst.split("$")
	lst = [[i for i in i.split(" ") if i] for i in lst]
	return len(max(lst,key=len))
	


max_consec([4, 9, 10, 5, 17, 3, 8, 11, 1, 12, 18, 20])