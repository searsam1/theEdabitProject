def clock(time):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(clock("12:00:00"), 0.0)
Test.assert_equals(clock("12:15:00"), 82.5)
Test.assert_equals(clock("12:32:44"), 179.967)
Test.assert_equals(clock("03:33:33"), 94.525)
Test.assert_equals(clock("01:59:59"), 60.092)