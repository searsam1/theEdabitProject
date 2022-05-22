
def split_groups(txt):

	res = [txt[0]]

	for i in txt[1:]:
		if i == res[-1]:
			res.append(i)
		else:
			res.append("$")
			res.append(i)
	res = "".join(res).split("$")
	return res




split_groups('5556667788')

