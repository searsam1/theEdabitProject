def sort_by_answer(lst):
	key_func = lambda i : eval(i.replace("x", "*"))
	return sorted(lst,key=key_func)