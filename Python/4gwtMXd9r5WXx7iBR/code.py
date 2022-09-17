def flatten(lst):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(flatten([[6, 7], [4, 5]]), [6, 7, 4, 5])
Test.assert_equals(flatten([[[[[["cat"]]]]]]), ["cat"])
Test.assert_equals(flatten([[3, [5, 6]], [9, 3]]), [3, 5, 6, 9, 3])
Test.assert_equals(flatten([1, [2, 3], [4, [5, 6]], [7, [8, [9, 0]]]]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
Test.assert_equals(flatten([[1], [[2], [3], [4, [5], 6]], [7, 8, 9, 0]]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])