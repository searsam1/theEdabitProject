def ana_str_str(needle, haystack):
	pass...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleimport random, string
Test.assert_equals(ana_str_str('car', 'race'), True)
Test.assert_equals(ana_str_str('nod', 'done'), True)
Test.assert_equals(ana_str_str('bag', 'grab'), False)
huge = ''.join([random.choice(string.ascii_lowercase) for _ in range(10000)]) + 'orchestra'
Test.assert_equals(ana_str_str('carthorse', huge), True, 'This one takes a long time if you are not efficient!')