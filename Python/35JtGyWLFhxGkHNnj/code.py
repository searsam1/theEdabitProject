def sel_reverse(lst, length):
	

TestsConsoleTest.assert_equals(sel_reverse([1, 2, 3, 4, 5, 6], 2), [2, 1, 4, 3, 6, 5])

Test.assert_equals(sel_reverse([2, 4, 6, 8, 10, 12, 14, 16], 3), [6, 4, 2, 12, 10, 8, 16, 14])

Test.assert_equals(sel_reverse([5, 7, 2, 6, 0, 4, 6], 100), [6, 4, 0, 6, 2, 7, 5])

Test.assert_equals(sel_reverse([6, 0, 0, 0, 3, 8, 9, 7, 1], 9), [1, 7, 9, 8, 3, 0, 0, 0, 6])

Test.assert_equals(sel_reverse([12, 54, 67, 34, 65, 34, 33], 0), [12, 54, 67, 34, 65, 34, 33])

Test.assert_equals(sel_reverse([12, 54, 67, 34, 65, 34, 33], 1), [12, 54, 67, 34, 65, 34, 33])

Test.assert_equals(sel_reverse([22, 13, 22, 13, 13, 22, 22, 13], 5), [13, 13, 22, 13, 22, 13, 22, 22])

Test.assert_equals(sel_reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [2, 1, 4, 3, 6, 5, 8, 7, 10, 9])

Test.assert_equals(sel_reverse([1], 2), [1])

Test.assert_equals(sel_reverse([1, 2], 2), [2, 1])