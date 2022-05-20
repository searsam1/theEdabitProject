def elasticize(word):
	

	
	if not len(word) % 2:
		idx = len(word) // 2
		left,right = word[:idx], word[idx:]	
		left = "".join(left[i]*(i+1) for i in range(len(left)))
		right = "".join(right[i]*(len(right)-i) for i in range(len(right)))
		return left + right
	else:
		idx = len(word) // 2
		middle = word[idx] * (idx + 1)
		word = word[:idx] + word[idx + 1:]
		left,right = word[:idx], word[idx:]	
		left = "".join(left[i]*(i+1) for i in range(len(left)))
		right = "".join(right[i]*(len(right)-i) for i in range(len(right)))

		return left + middle + right
		


print(elasticize("KAYAK"))

