def replace_next_largest(lst):
	
	for i in range(len(lst)):
		ele = lst[i]

		rest_of_the_elements = lst[i + 1:]
		
		for j in range(len(rest_of_the_elements)):

			ele2 = rest_of_the_elements[j]
			if  ele2 > ele:
				lst[i],lst[j-1] = lst[j-1],lst[i]
				print(lst)
		



replace_next_largest([5, 7, 3, 2, 8])