def swap_cards(n1, n2):
	arr1, arr2 = [int(i) for i in str(n1)], [int(i) for i in str(n2)]
	low = min(arr1)
	high = arr2[0]
	
	idx = arr1.index(low)
	arr1[idx],arr2[0] = high,low
	
	n1,n2 = int("".join(map(str,arr1))), int("".join(map(str,arr2)))
	return n1 > n2 
