#
def left_side(lst):
	res = [] 
	for i in range(len(lst)):
		ele = lst[i]
		mini_lst = lst[:i]
		count = sum(ele > n for n in mini_lst)
		res.append(count)
	return res

def right_side(lst):
	res = [] 
	for i in range(len(lst)-1,-1,-1):
		ele = lst[i]
		mini_lst = lst[i+1:]
		count = sum(ele > n for n in mini_lst)
		res.append(count)
	res.reverse()
	return res
#
