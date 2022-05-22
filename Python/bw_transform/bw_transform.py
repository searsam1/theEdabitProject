def bw_transform(text):
	rotations = [text]
	for i in range(len(text) - 1):
		text = text[1:] + text[0]
		rotations.append(text)
	rotations.sort()
	last_column = "".join(row[-1] for row in rotations)
	return last_column



bw_transform("banana$")