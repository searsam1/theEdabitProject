
import re, random, string

def ana_str_str(needle, haystack):
    l = len(needle)
    while len(haystack) >= l:
        if all(i in needle for i in haystack[:l]):
            return True
        haystack = haystack[1:]
    return False

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
            
Test.assert_equals(ana_str_str('car', 'race'), True)
Test.assert_equals(ana_str_str('nod', 'done'), True)
Test.assert_equals(ana_str_str('bag', 'grab'), False)
huge = ''.join([random.choice(string.ascii_lowercase) for _ in range(10000)]) + 'orchestra'
Test.assert_equals(ana_str_str('carthorse', huge), True)