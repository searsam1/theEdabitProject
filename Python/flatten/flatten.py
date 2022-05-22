#//x = all(not isinstance(ele, list) for ele in arr) # thats the key


main = []
def flatten(arr):	
	
	res = [] 
	if isinstance(arr, list):
		for i in arr:
			res.append(flatten(i))
	else:
		return arr
	if isinstance(res, list):
		for i in res:
			x = flatten(i)
			if x:
				print(x)
		


x = flatten([[[[[["direction"], [372], ["one"], [[[[[["Era"]]]], "Sruth", 3337]]], "First"]]]])
print(main)


