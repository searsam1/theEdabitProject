def average_ascii(txt):
	words = txt.split()
	word_sum = lambda word : sum(ord(char) for char in word)
	global_average = sum(word_sum(word) for word in words) / len(words)
	word_sums = lambda words : [word_sum(word) > global_average for word in words]
	
	z = zip(word_sums(words),words)

	res = [] 
	for pair in z:
		i,j = pair
		if i:
			res.append(j.upper())
		else:
			res.append(j)
	return " ".join(res)


average_ascii("Tell me the time")
