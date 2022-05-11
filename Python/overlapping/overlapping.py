def overlapping(lst):
	mins = [l[0] for l in lst]
	maxes = [l[1] for l in lst]
	
	return [(max(mins) ,min(maxes)),"No overlapping"][max(mins) > min(maxes)]


print(
	overlapping([(11, 18), (3, 7), (2, 20), (5, 16)])
	)
			
