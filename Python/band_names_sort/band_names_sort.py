def band_names_sort(r):
	
	res = [band.replace("The ","").replace("An ","").replace("A ","") 
		for band in r]
	z = list(zip(r,res))
	z = sorted(z, key = lambda x: x[1])
	z = [i[0] for i in z]
	return z

# names = ["The Plot in You", "The Devil Wears Prada", "Pierce the Veil", "Norma Jean", "The Bled", "Say Anything", "The Midway State", "We Came as Romans", "Counterparts", "Oh, Sleeper", "A Skylit Drive", "Anywhere But Here", "An Old Dog"]

# print(band_names_sort(names))