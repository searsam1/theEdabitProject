def brackets(exp):
	
	s = "".join(i for i in exp if i == "(" or i == ")")
	if len(s) == 0:
		return True
	return s.count("(") == s.count(")") and s[0] != ")" and s[-1] != "("
    

class Test():

    def assert_equals(a,b):
        print(a,b)




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