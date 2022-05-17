
def sle(m):
	try:
		arr1,arr2 = m[0],m[1]
		a,b,c = arr1[0],arr1[1],arr1[2]
		d,e,f = arr2[0],arr2[1],arr2[2]
		
		middle = arr1.pop(1) * -1
		arr1.append(middle)

		div = arr1.pop(0)
		arr1 = [i for i in arr1]
		
		arr1[1] *= a
		arr1[2] *= a

		y_s = d * arr1[1] + arr2[1]
		c = arr2[-1] - d * arr1[0]
		y = y_s / c
		
		x = (e - f) / d
		print(x,y)
		return (x,y)
	except Exception:
		return 0



