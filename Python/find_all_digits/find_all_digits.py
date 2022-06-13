def find_all_digits(nums):
	s1 = set("".join(map(str, nums)))
	s2 = "".join(map(str, nums))

	s1 = sorted(s1, key=lambda x: s2.index(x))
	s1 = list(map(int,s1))
	if len(s1) == 10:
		key = s1[-1]

		return nums[::-1].index(int(key))