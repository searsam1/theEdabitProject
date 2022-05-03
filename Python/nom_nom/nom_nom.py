def nom_nom(lst):
	if all(lst[i] >= lst[i-1] for i in range(1,len(lst))):
		return lst
	temp = []
	for i in range(1,len(lst)):
		if lst[i-1] > lst[i]:
			temp.append(lst[i-1] + lst[i])
			lst.pop(0),lst.pop(0)
			lst = temp + lst
			return nom_nom(lst)

print(nom_nom([5,3,7]))

	


