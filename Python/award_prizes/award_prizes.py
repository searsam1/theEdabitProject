
def award_prizes(names):
	names_copy = names
	gold = max(names_copy.items(), key= lambda lst: lst[1])
	
	names_copy[gold[0]] = 0
	silver = max(names_copy.items(), key= lambda lst: lst[1])
	
	names_copy[silver[0]] = 0
	bronze = max(names_copy.items(), key= lambda lst: lst[1])
	
	names_copy[bronze[0]] = 0

	for k, v in names_copy.items():
		if v != 0:
			names[k] = "Participation"
	names[gold[0]], names[silver[0]], names[bronze[0]] = "Gold", "Silver", "Bronze"
	return names

	

