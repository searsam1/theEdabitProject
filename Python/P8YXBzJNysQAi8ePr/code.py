def digitaldrome(n):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(digitaldrome(1357), "Metadrome", "Example #1")
Test.assert_equals(digitaldrome(12344), "Plaindrome", "Example #2")
Test.assert_equals(digitaldrome(7531), "Katadrome", "Example #3")
Test.assert_equals(digitaldrome(9874441), "Nialpdrome", "Example #4")
Test.assert_equals(digitaldrome(666), "Repdrome", "Example #5")
Test.assert_equals(digitaldrome(1985), "Nondrome", "Example #6")
Test.assert_equals(digitaldrome(33333), "Repdrome")
Test.assert_equals(digitaldrome(1), "Repdrome")
Test.assert_equals(digitaldrome(4899), "Plaindrome")
Test.assert_equals(digitaldrome(7521), "Katadrome")
Test.assert_equals(digitaldrome(23), "Metadrome")
Test.assert_equals(digitaldrome(2340), "Nondrome")
Test.assert_equals(digitaldrome(1000000), "Nialpdrome")
Test.assert_equals(digitaldrome(269), "Metadrome")