def smallest_transform(n):
	 diff = lambda x,y : sum(abs(int(i) - int(j)) for i,j in zip(x,y))

	 arr = []
	 l = len(str(n))
	 for i in str(n):
	 	x = i * l
	 	y = str(n)
	 	res = diff(x,y)
	 	arr.append(res)
	 return min(arr)

smallest_transform(1234)
