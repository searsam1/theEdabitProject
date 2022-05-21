def is_set(cards):
	colors = len({d.get("color") for d in cards}) in [1,3]
	nums = len({d.get("number") for d in cards}) in [1,3]
	shades = len({d.get("shade") for d in cards}) in [1,3]
	shapes = len({d.get("shape") for d in cards}) in [1,3]

	return colors and nums and shades and shapes


