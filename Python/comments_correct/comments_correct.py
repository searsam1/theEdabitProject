def comments_correct(txt):
	return not txt.count("/") % 2 and not txt.count("*") % 2
	