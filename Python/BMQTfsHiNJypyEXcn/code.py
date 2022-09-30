def primal_strength(n):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(primal_strength(5), "Balanced")
Test.assert_equals(primal_strength(211), "Balanced")
Test.assert_equals(primal_strength(593), "Balanced")
Test.assert_equals(primal_strength(1693), "Strong")
Test.assert_equals(primal_strength(599), "Strong")
Test.assert_equals(primal_strength(2203), "Strong")
Test.assert_equals(primal_strength(19), "Weak")
Test.assert_equals(primal_strength(2971), "Weak")
Test.assert_equals(primal_strength(1493), "Weak")