
def lowest_element(arr,x,y):
	bottom,top = (x+1,y), (x-1,y)
	left,right = (x, y-1), (x, y+1)
	diagonal_top_left, diagonal_top_right = (x-1,y-1), (x-1,y+1)
	diagonal_bottom_left, diagonal_bottom_right = (x+1,y-1), (x+1,y+1)

	def get_val(tup):
		x,y = tup
		try:

			if x < 0 or y < 0:
				return None
			return arr[x][y]

		except IndexError as IE:
			pass

	arr2 = [diagonal_top_left, top, diagonal_top_right, left, right, diagonal_bottom_left, bottom, diagonal_bottom_right]

	minn = min(get_val(t) for t in arr2 if get_val(t))
	if arr[x][y] < minn:
		return arr[x][y]
	return minn


