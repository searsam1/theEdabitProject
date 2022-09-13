def dead_end(n):
	

TestsConsoleTest.assert_equals(dead_end(1), (1, 1))

Test.assert_equals(dead_end(9), (2, 1))

Test.assert_equals(dead_end(1000), (1, 1000))

Test.assert_equals(dead_end(999), (3, 370))

Test.assert_equals(dead_end(38), (12, 174813842944))

Test.assert_equals(dead_end(93), (9, 217))

Test.assert_equals(dead_end(11615819), (74, 1354959139828966431926720346323206635520))

Test.assert_equals(dead_end(100000001), (15, 220258825732))