def mix_middle(txt):
	word_function = lambda word : [
				word[0] + word[1:-1][::-1] + 
				word[-1] if len(word) > 1 
					else word][0]
	
	res = []
	words = txt.split()
	for word in words:
		if "-" in word:
			dash_index = word.index("-")
			word = word_function( word.replace("-","") )
			word = word[:dash_index] + "-" + word[dash_index:]
			res.append(word)
		else:
			res.append(word_function(word))
	return " ".join(res)

print(mix_middle("b"))
