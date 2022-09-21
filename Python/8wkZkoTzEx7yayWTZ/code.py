def self_descriptive(n):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(self_descriptive(10313317), True)
Test.assert_equals(self_descriptive(41322324151819), True)
Test.assert_equals(self_descriptive(3133141), False)
Test.assert_equals(self_descriptive(22), True)
Test.assert_equals(self_descriptive(2), False)
Test.assert_equals(self_descriptive(21322313), False)
Test.assert_equals(self_descriptive(201314), False)
Test.assert_equals(self_descriptive( 613223141526171819), True)