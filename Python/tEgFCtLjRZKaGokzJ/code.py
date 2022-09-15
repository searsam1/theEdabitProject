import re
def to_star_shorthand(txt):
    # p = r"(.)(\1*)(\1)"
    p = r"(.)(\1+)(\1)|(.)(\4)|(.)"
    matches = re.findall(p,txt)
    connect = ""
    for match in matches:
        res = "".join(match)

        if len(res) > 1:
            res = str(res[0]) + "*" + str(len(res))
        connect += res
    return connect


class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

Test.assert_equals(to_star_shorthand("haaaappyyyyy"), "ha*4p*2y*5")
Test.assert_equals(to_star_shorthand("77777geff"), "7*5gef*2")
Test.assert_equals(to_star_shorthand("11223344"), "1*22*23*24*2")
Test.assert_equals(to_star_shorthand("abc"), "abc")
Test.assert_equals(to_star_shorthand(""), "")