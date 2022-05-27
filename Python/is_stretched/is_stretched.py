def is_stretched(s1, s2):
	
	const = s1.count(s1[0])

	check = ""
	for i in s2:
		check += i * const
	return check == s1


def split_up(s):
	res = [None] 
	for i in s:
		if res[-1] != i:
			res.append(i)
	print(res)

split_up("1111h1h1h3h32h23hhh2h2hghdfh")


