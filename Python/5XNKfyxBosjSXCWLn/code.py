def is_modest(num):
	

TestsConsoleTest.assert_equals(is_modest(2036), True, "Example #1")

Test.assert_equals(is_modest(3412), False, "Example #2")

Test.assert_equals(is_modest(21333), True, "Example #3")

Test.assert_equals(is_modest(8), False, "Example #4")

Test.assert_equals(is_modest(13), True)

Test.assert_equals(is_modest(329), False)

Test.assert_equals(is_modest(433), True)

Test.assert_equals(is_modest(2037), True)

Test.assert_equals(is_modest(2038), False)

Test.assert_equals(is_modest(12036), True)

Test.assert_equals(is_modest(20010), False)

Test.assert_equals(is_modest(450810), True)

Test.assert_equals(is_modest(4221344), False)

Test.assert_equals(is_modest(9111111), True)