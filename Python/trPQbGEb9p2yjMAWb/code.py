def every_some(test, val, a, b, c, d, e):
	

TestsConsoleTest.assert_equals(every_some(">= 1", "everybody", 1, 1, -1, 1, 1), False, "Example #1")

Test.assert_equals(every_some(">= 1", "somebody", -1, -1, -1, -1, 1), True, "Example #2")

Test.assert_equals(every_some("< 4 / 2", "everybody", 1, 2, 1, 0, -10), False, "Example #3")

Test.assert_equals(every_some("!= 0", "everybody", False, False, False, False, False), False)

Test.assert_equals(every_some("<= 10 * 2", "somebody", 21, 68, 104, 20, 3), True)

Test.assert_equals(every_some("!= 1", "everybody", True, True, True, True, True), False)

Test.assert_equals(every_some("== 9 % 9", "somebody", 9, 1, 81, 218, 33), False)