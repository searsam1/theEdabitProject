def brackets(exp):
	

TestsConsoleTest.assert_equals(brackets("(a*(b-c)     )"), True)

Test.assert_equals(brackets(" ) (a-b-45/7*(a-34))"), False)

Test.assert_equals(brackets("sin(90       )+      cos1)"), False)

Test.assert_equals(brackets(" (...). .%_.(.... )"), True)

Test.assert_equals(brackets(" (...)...(..(...).... )  "), True)

Test.assert_equals(brackets(") .. .() (        ).. . ("), False)

Test.assert_equals(brackets(")))((("), False)

Test.assert_equals(brackets("  (...).!.)...("), False)

Test.assert_equals(brackets("a+b"), True)

Test.assert_equals(brackets(""), True)

Test.assert_equals(brackets("(a+f).`!=.)...) "), False)