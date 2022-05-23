def column(txt):
	scores = { chr(i).upper() : i-96 for i in range(97,123) }
	
	res = [scores[score] for score in txt][::-1]
	print(res)

	total = 0
	for i in range(len(res)):
		power = 26 ** i * res[i]
		print(power)
		total += power
	return total
		