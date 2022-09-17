def spoonerise(phrase):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(spoonerise("crushing failure"), "fushing crailure")
Test.assert_equals(spoonerise("christmas eve"), "istmas chreve")
Test.assert_equals(spoonerise("highlighter fluid"), "flighlighter huid")
Test.assert_equals(spoonerise("chocolate biscuits"), "bocolate chiscuits")
Test.assert_equals(spoonerise("edabit rules!"), "redabit ules!")