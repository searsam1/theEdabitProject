def digit_sort(lst):
	res = sorted(lst, key=lambda x: ( len(str(x)),x*-1 ),
	reverse=True)
	return res