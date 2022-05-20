def resistance_calculator(resistors):
	

	series = sum(resistors)
	if resistors.count(0):
		return [0,series]
	para = round(1 / sum(1 / r for r in resistors if r),2)
	return [para, round(series,2)]


print(resistance_calculator([10, 20, 30, 40, 50,0]))
