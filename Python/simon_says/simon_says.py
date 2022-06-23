# Panther Piss
def simon_says(lst):
	def has_simon(sentence): return "simon" in sentence.lower()

	keywords = {"add" : lambda x,y : x + y,
		 "multiply" : lambda x,y: x * y, 
		 "subtract" : lambda x,y: x - y, 
		}


	res = 0
	for sentence in lst:
		words = sentence.split()
		if has_simon(sentence):
			n = int("".join(i for i in sentence if i.isnumeric()))

			for word in words:
				if keywords.get(word):
					res = keywords.get(word)(res, n)
	return res
# Panther Piss