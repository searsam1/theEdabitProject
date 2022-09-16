
import re


def erase(txt):
    while "#" in txt:
        idx = txt.index("#")
        if idx == 0:
            txt = txt[1:]
        else:
            txt = txt[:idx-1] + txt[idx + 1:]
    return txt


class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(erase("he##l#hel#llo"), "hello")
Test.assert_equals(erase("major# spar##ks"), "majo spks" )
Test.assert_equals(erase("si###t boy"), "t boy")
Test.assert_equals(erase("motion #sick"), "motionsick")
Test.assert_equals(erase("m#oti#o#n sick##ne#ss##"), "otn sin")
Test.assert_equals(erase("courz#i#age"), "courage")
Test.assert_equals(erase("aris##### c#r#ti#c"), " tc")
Test.assert_equals(erase("beauty##"), "beau")
Test.assert_equals(erase("beauty#"), "beaut")
Test.assert_equals(erase("b#"), "")
Test.assert_equals(erase("####"), "")