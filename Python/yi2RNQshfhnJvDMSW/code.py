def squish(lst, d):
	

TestsConsoleTest.assert_equals(squish([1, 2, 3, 4, 5], "left"), [[1, 2, 3, 4, 5], [3, 3, 4, 5], [6, 4, 5], [10, 5], [15]])

Test.assert_equals(squish([1, 0, 2, -3], "left"), [[1, 0, 2, -3], [1, 2, -3], [3, -3], [0]])

Test.assert_equals(squish([4, 9, -3, 2, 5], "left"), [[4, 9, -3, 2, 5], [13, -3, 2, 5], [10, 2, 5], [12, 5], [17]])

Test.assert_equals(squish([8, -7, 6, 1, 0, 2], "left"), [[8, -7, 6, 1, 0, 2], [1, 6, 1, 0, 2], [7, 1, 0, 2], [8, 0, 2], [8, 2], [10]])

Test.assert_equals(squish([8, 7], "left"), [[8, 7], [15]])

Test.assert_equals(squish([8], "left"), [[8]])

Test.assert_equals(squish([], "left"), [])



Test.assert_equals(squish([1, 2, 3, 4, 5], "right"), [[1, 2, 3, 4, 5], [1, 2, 3, 9], [1, 2, 12], [1, 14], [15]])

Test.assert_equals(squish([1, 0, 2, -3], "right"), [[1, 0, 2, -3], [1, 0, -1], [1, -1], [0]])

Test.assert_equals(squish([4, 9, -3, 2, 5], "right"), [[4, 9, -3, 2, 5], [4, 9, -3, 7], [4, 9, 4], [4, 13], [17]])

Test.assert_equals(squish([8, -7, 6, 1, 0, 2], "right"), [[8, -7, 6, 1, 0, 2], [8, -7, 6, 1, 2], [8, -7, 6, 3], [8, -7, 9], [8, 2], [10]])

Test.assert_equals(squish([8, 7], "right"), [[8, 7], [15]])

Test.assert_equals(squish([8], "right"), [[8]])

Test.assert_equals(squish([], "right"), [])