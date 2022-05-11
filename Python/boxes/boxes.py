def boxes(weights):
	weight_l = len(weights)
	box = [weights.pop(0)]
	res = []
	while weights:
		b = weights.pop(0)
		if b + sum(box) > 10:
			res.append(box)
			box = [b]
		elif b + sum(box) == 10:
			res.append(box + [b])
			box = []
		else:
			box.append(b)
	print(res)
	count = sum(len(i) for i in res)

	if count != weight_l:
		try:
			res = res + [[b]]
		except UnboundLocalError:
			return 1
	return len(res)

print(
	boxes([8, 3, 2, 1, 1, 2, 1, 3, 2, 1])
	)
	