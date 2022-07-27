def get_name_and_top_note(students):
	
	res = []
	for d in students:
		name = d["name"]
		try:
			top_note = max(d["notes"])
		except ValueError as VE:
			top_note = 0
		
		temp = {"name" : name, "top_note" : top_note}
		res.append(temp)
	return res