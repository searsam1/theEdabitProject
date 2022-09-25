def swap(a, b, c):
	return [a,b][a ^ c == 0]

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            


Test.assert_equals(swap(1, 0, 0), 1)
Test.assert_equals(swap(1, 3, 1), 3)
Test.assert_equals(swap(27, 31, 31), 27)

Test.assert_equals(swap(1, 2, 2), 1)
Test.assert_equals(swap(-3, 4, -3), 4)
Test.assert_equals(swap(-2, 1, 1), -2)
Test.assert_equals(swap(0, 2, 2), 0)
Test.assert_equals(swap(9, -9, 9), -9)
Test.assert_equals(swap(-3, -29, -3), -29)
Test.assert_equals(swap(-29, -3, -3), -29)