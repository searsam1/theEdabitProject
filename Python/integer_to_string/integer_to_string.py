
res = []

def base_8(n):
	if n < 1:
		res.append('%')
		return "".join(str(i) for i in res)[::-1]
	res.append(n % 8)
	n //= 8
	return base_8(n)


def base_2(n):
	if n < 1:
		res.append('%')
		return "".join(str(i) for i in res)[::-1]
	res.append(int(bool(n % 2)))
	n //= 2
	return base_2(n)

def base_16(n):
	if n < 1:
		res.append('%')
		return "".join(str(i) for i in res)[::-1]
	res.append("{:x}".format((n % 16)))
	n //= 16
	return base_16(n)


def integer_to_string(number, base):
	d = {
	2 : base_2,
	8 : base_8,
	16 : base_16,
	}
	return [i for i in d[base](number).split("%") if i][0]
