def star_rating(lst):
	total_stars = sum((idx+1) * i for idx, i in enumerate(lst))
	avg_rating = total_stars  / sum(lst)
	string = "[{0:.2f}] {1}".format(avg_rating, "*" * round(avg_rating))
	return string

	
	

