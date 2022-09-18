def alt_semi(n):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(alt_semi(1), 0)
Test.assert_equals(alt_semi(3), 2)
Test.assert_equals(alt_semi(4), 11)
Test.assert_equals(alt_semi(6), 571)
Test.assert_equals(alt_semi(9), 326036)
Test.assert_equals(alt_semi(16), 19696498855099)
Test.assert_equals(alt_semi(21), 48773618867405512406)