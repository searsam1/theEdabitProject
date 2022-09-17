
vows = "aeiou"

def spoonerise(phrase):
    word_1, word_2 = phrase.split()

    res_1 = ""
    while word_1[0] not in vows:
        res_1 += (word_1[0])
        word_1 = word_1[1:]
    res_2 = ""
    while word_2[0] not in vows:
        res_2 += (word_2[0])
        word_2 = word_2[1:]
    
    word_1 = res_2 + word_1
    word_2 = res_1 + word_2
    return word_1 + " " + word_2
    
    


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