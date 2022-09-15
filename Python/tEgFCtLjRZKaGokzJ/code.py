def to_star_shorthand(txt):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(to_star_shorthand("abbccc"), "ab*2c*3")
Test.assert_equals(to_star_shorthand("haaaappyyyyy"), "ha*4p*2y*5")
Test.assert_equals(to_star_shorthand("77777geff"), "7*5gef*2")
Test.assert_equals(to_star_shorthand("11223344"), "1*22*23*24*2")
Test.assert_equals(to_star_shorthand("abc"), "abc")
Test.assert_equals(to_star_shorthand(""), "")