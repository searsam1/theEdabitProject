def is_exact(n):
	

TestsConsoleTest.assert_equals(is_exact(2), [2, 2])

Test.assert_equals(is_exact(6), [6, 3])

Test.assert_equals(is_exact(24), [24, 4])

Test.assert_equals(is_exact(120), [120, 5])

Test.assert_equals(is_exact(5040), [5040, 7])

Test.assert_equals(is_exact(40320), [40320, 8])

Test.assert_equals(is_exact(3628800), [3628800, 10])

Test.assert_equals(is_exact(20922789888000), [20922789888000, 16])

Test.assert_equals(is_exact(125), "Not exact!")

Test.assert_equals(is_exact(721), "Not exact!")

Test.assert_equals(is_exact(1024), "Not exact!")

Test.assert_equals(is_exact(41845579776000), "Not exact!")