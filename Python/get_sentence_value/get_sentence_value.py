def get_sentence_value(txt):
	txt = "".join(i for i in txt if i.isalpha() or i == " ")
	scores = { chr(i) : i-96 for i in range(97,123)}
	get_score = lambda word : sum(scores[char.lower()] for char in word)
	return sum((get_score(word) * [1,2][all(i.isupper() for i in word)] ) for word in txt.split())
	


get_sentence_value("abc ABC Abc")