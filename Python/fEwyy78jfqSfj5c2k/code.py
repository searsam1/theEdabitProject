def admirable(n):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(admirable(6), 'Perfect')
Test.assert_equals(admirable(12), 2)
Test.assert_equals(admirable(18), 'Neither')
Test.assert_equals(admirable(496), 'Perfect')
Test.assert_equals(admirable(138), 6)
Test.assert_equals(admirable(612), 'Neither')
Test.assert_equals(admirable(1876), 28)
Test.assert_equals(admirable(5456), 496)