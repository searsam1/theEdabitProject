def deep_count(lst):
	
	total = 0
	while len(lst):
		if type(lst[0]) == list:
			lst = lst[1]
			total  += 1
		print(lst)






deep_count([[[[]]]])