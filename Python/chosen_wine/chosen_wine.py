def chosen_wine(wines):
	if len(wines) >= 2:
		return sorted(wines, key=lambda x: x["price"])[1]['name']
	elif not len(wines):
		return None
	else:
		return wines[0]["name"]