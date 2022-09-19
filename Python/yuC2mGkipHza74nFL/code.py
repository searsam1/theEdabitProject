def two_powers_of_two(n):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(two_powers_of_two(0), False)
Test.assert_equals(two_powers_of_two(1), True)
Test.assert_equals(two_powers_of_two(2), True)
Test.assert_equals(two_powers_of_two(3), True)
Test.assert_equals(two_powers_of_two(4), True)
Test.assert_equals(two_powers_of_two(5), True)
Test.assert_equals(two_powers_of_two(6), True)
Test.assert_equals(two_powers_of_two(9), True)
Test.assert_equals(two_powers_of_two(14), False)
Test.assert_equals(two_powers_of_two(32), True)
Test.assert_equals(two_powers_of_two(48), True)
Test.assert_equals(two_powers_of_two(68), True)
Test.assert_equals(two_powers_of_two(72), True)
Test.assert_equals(two_powers_of_two(80), True)
Test.assert_equals(two_powers_of_two(96), True)

Test.assert_equals(two_powers_of_two(1052672), True)
Test.assert_equals(two_powers_of_two(131080), True)
Test.assert_equals(two_powers_of_two(270336), True)
Test.assert_equals(two_powers_of_two(1048578), True)
Test.assert_equals(two_powers_of_two(262176), True)