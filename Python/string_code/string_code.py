import string

v_count = lambda word : sum(c in "aeiou" for c in word)

def string_code(sentence):
	lower_sentence = sentence.lower()
	words = "".join(i for i in lower_sentence 
		if i.isalpha() or i == " "
		).split()
	counts = [(v_count(word) , len(word) - v_count(word) ) 
		for word in words
		]
	cons = " ".join(map(str, map(lambda x: x[0], counts) ))
	vows = " ".join(map(str, map(lambda x: x[1], counts) ))
	return [vows, cons]
	
