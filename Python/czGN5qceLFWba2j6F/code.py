def is_self_describing(num):
	

TestsConsoleTest.assert_equals(is_self_describing(10123331), True, "Example #1")

Test.assert_equals(is_self_describing(224444), True, "Example #2")

Test.assert_equals(is_self_describing(2211), False, "Example #3")

Test.assert_equals(is_self_describing(333), False, "Example #4")

Test.assert_equals(is_self_describing(1), False)

Test.assert_equals(is_self_describing(27273332), True)

Test.assert_equals(is_self_describing(11), False)

Test.assert_equals(is_self_describing(22), True)

Test.assert_equals(is_self_describing(19212332), True)

Test.assert_equals(is_self_describing(4444332231), False)

Test.assert_equals(is_self_describing(881722888888), True)