def profit(A, B):
	...
class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(profit(32, 69), [51, 50])
Test.assert_equals(profit(49, 51), [50, 50])
Test.assert_equals(profit(25, 26), [26, 75])
Test.assert_equals(profit(24, 26), [25, 75])
Test.assert_equals(profit(0, 1), [1, 100])
Test.assert_equals(profit(3, 6), [5, 96])
Test.assert_equals(profit(55, 65), [60, 40])
Test.assert_equals(profit(25, 75), [50, 50])