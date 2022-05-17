def fair_die(lst):
	
	total_rolls = sum(lst)
	probability = 6  / total_rolls

	expected = total_rolls / 6

	chi = sum((expected - actual)**2 for actual in lst) / expected
	return chi < 11.0705
