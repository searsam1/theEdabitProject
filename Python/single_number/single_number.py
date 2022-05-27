def single_number(nums):
	s = sorted(set(nums), key=lambda x : nums.count(x) )
	return s[0]