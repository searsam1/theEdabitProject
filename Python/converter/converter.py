def converter(a, b):
	if a[0] == "fahrenheit":
		if b == "kelvin":
			return round((a[1] - 32) * (5/9) + 273.15,1)
		elif b == "celsius":
			return round((a[1] - 32) * (5/9),1)
	elif a[0] == "celsius":
		if b == "kelvin":
			return round(273.15 + a[1],1)
		elif b == "fahrenheit":
			return round((a[1] * 9/5) + 32,1)
	elif a[0] == "kelvin":
		if b == "fahrenheit":
			return round((a[1] - 273.15) * (9/5) + 32,1)
		elif b == "celsius":
			return round(a[1] - 273.15,1)
