def lost_dog(*arr):
	
	dog = 0
	d = {}
	dog_count = 0 
	for i in range(len(arr)):
		building = arr[i]

		if dog in building:
			dog_count += 1
			d["Dog{}".format(dog_count)] = "House ({}) and Room ({})".format(i+1,building.index(dog)+1)

	return d if d else "Dog not found!"
lost_dog([1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1])