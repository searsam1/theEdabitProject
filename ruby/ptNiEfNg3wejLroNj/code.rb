def new_and(a, b)
	
end

TestsConsoleTest.assert_equals(new_and(true, true), true)

Test.assert_equals(new_and(true, false), false)

Test.assert_equals(new_and(false, true), false)

Test.assert_equals(new_and(false, false), false)