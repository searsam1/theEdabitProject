def max_occur(text):
	mx = text.count(max(text, key=text.count))
	if mx == 1:
		return "No Repetition"
	collection = [i for i in set(text) if text.count(i) == mx]
	return sorted(collection)
	
	
	#wrong answer
	
		