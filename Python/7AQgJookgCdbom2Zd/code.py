def pig_latin(txt):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(pig_latin("Cats are great pets."), "Atscay areway reatgay etspay.")
Test.assert_equals(pig_latin("Tom got a small piece of pie."), "Omtay otgay away mallsay iecepay ofway iepay.")
Test.assert_equals(pig_latin("He told us a very exciting tale."), "Ehay oldtay usway away eryvay excitingway aletay.")
Test.assert_equals(pig_latin("A diamond is not enough."), "Away iamondday isway otnay enoughway.")
Test.assert_equals(pig_latin("Hurry!"), "Urryhay!")