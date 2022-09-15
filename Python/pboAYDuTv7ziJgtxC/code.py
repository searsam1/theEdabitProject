def min_turns(current, target):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(min_turns("4089", "5672"), 9)
Test.assert_equals(min_turns("1732", "4444"), 9)
Test.assert_equals(min_turns("7109", "2332"), 13)
Test.assert_equals(min_turns("2391", "4984"), 10)
Test.assert_equals(min_turns("1234", "3456"), 8)
Test.assert_equals(min_turns("1111", "1100"), 2)
Test.assert_equals(min_turns("1111", "0000"), 4)
Test.assert_equals(min_turns("0000", "9999"), 4)