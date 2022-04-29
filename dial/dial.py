# d = {}
# dic = {} 
# d["abc"],d["def"],d["ghi"] = 2,3,4
# d["jkl"],d["mno"],d["pqrs"]  = 5,6,7
# d["tuv"],d["wxyz"] = 8,9
# for k,v in d.items():
# 	for char in k:
# 		dic[char] = v
d = {
'r': 7, 'i': 4,
'l': 5, 's': 7, 'b': 2,
'j': 5, 'd': 3, 'a': 2,
'c': 2, 'h': 4, 'g': 4,
'p': 7, 'm': 6, 'x': 9,
'w': 9, 'q': 7, 'n': 6,
'o': 6, 't': 8, 'u': 8,
'v': 8, 'e': 3, 'y': 9, 
'k': 5, 'z': 9, 'f': 3
}

def dial(txt):
	return "".join(str(d[i.lower()]) 
		if i.isalpha() else i 
			for i in txt)
