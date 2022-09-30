def zeroes_to_end(lst):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsolea1 = [1, 2, 0, 0, 4, 0, 5]
a2 = [0, 0, 1, 3]
a3 = [0, 0, 2, 0, 5]
a4 = [4, 4, 5]
a5 = [0, 0]

r1 = zeroes_to_end(a1)
r2 = zeroes_to_end(a2)
r3 = zeroes_to_end(a3)
r4 = zeroes_to_end(a4)
r5 = zeroes_to_end(a5)

Test.assert_equals(r1, [1, 2, 4, 5, 0, 0, 0])
Test.assert_equals(r2, [1, 3, 0, 0])
Test.assert_equals(r3, [2, 5, 0, 0, 0])
Test.assert_equals(r4, [4, 4, 5])
Test.assert_equals(r5, [0, 0])

Test.assert_equals(id(a1), id(r1))
Test.assert_equals(id(a2), id(r2))
Test.assert_equals(id(a3), id(r3))
Test.assert_equals(id(a4), id(r4))
Test.assert_equals(id(a5), id(r5))