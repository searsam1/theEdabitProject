def is_icecream_sandwich(txt):
	s = sorted(list(set(txt)),key = lambda x : txt.index(x))
	if len(s) != 2:
		return False
	if txt.count(s[0]) % 2:
		return False
	return True
			
	