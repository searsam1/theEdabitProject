def left_rotations(txt):
	r = [txt]
	for i in range(len(txt) - 1):
		txt = txt[1:] + txt[0]
		r.append(txt)
	return r

def right_rotations(txt):
	r = [txt]
	for i in range(len(txt) - 1):
		txt = txt[-1] +  txt[:-1]
		r.append(txt)
	return r
