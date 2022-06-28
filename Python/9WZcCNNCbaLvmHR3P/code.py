def is_new(n):
	n_string = str(n).replace("0", "")
	if n < 10 or len(n_string) == 1:
		return True
	if "0" in str(n):
		if str(n)[1] != "0":
			return False
	return "".join(sorted(n_string)) == n_string
print("\n~~\n")        


# Test.assert_equals(is_new(90), True)

# Test.assert_equals(is_new(601), False) 

# Test.assert_equals(is_new(123), True)

# Test.assert_equals(is_new(321), False)

# Test.assert_equals(is_new(40567), True)

# Test.assert_equals(is_new(10783), False)

# Test.assert_equals(is_new(4444), True)

# Test.assert_equals(is_new(102), True)

# Test.assert_equals(is_new(30004), True)

# Test.assert_equals(is_new(40003), False)

# Test.assert_equals(is_new(125609), False)

# Test.assert_equals(is_new(23401), False)