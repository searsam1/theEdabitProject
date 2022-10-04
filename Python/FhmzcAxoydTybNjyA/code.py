def carry_digits(n1, n2):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(carry_digits(36, 135), 1)
Test.assert_equals(carry_digits(671, 329), 3)
Test.assert_equals(carry_digits(1111, 3333), 0)
Test.assert_equals(carry_digits(4, 5268), 1)
Test.assert_equals(carry_digits(53214, 16905), 2)
Test.assert_equals(carry_digits(53214, 56905), 3)
Test.assert_equals(carry_digits(515, 4), 0)
Test.assert_equals(carry_digits(515, 90), 1)
Test.assert_equals(carry_digits(63223, 70000), 1)