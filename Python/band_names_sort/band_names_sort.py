def band_names_sort(r):
	
	res = [band.lstrip("The ").lstrip("An ").lstrip("A ") 
		for band in r]
	z = list(zip(r,res))
	z = sorted(z, key = lambda x: x[1])
	z = [i[0] for i in z]
	print(z)




print(band_names_sort(['The New Yardbirds', 'The Beatles', 'The Square Roots', 'On A Friday', 'An Irony']))