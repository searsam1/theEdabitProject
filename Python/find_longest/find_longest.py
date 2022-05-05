def find_longest(sentence):
	words = sorted(sentence.split(), key=lambda x: len([i for i in x if i.isalpha()]), 
	reverse=True
	)
	res = []
	for word in words:
		new_word = ""
		for char in word:
			if not char.isalpha():
				res.append(new_word)
				next
			else:
				new_word += char
		res.append(new_word)
				
	return res[0].lower()
	