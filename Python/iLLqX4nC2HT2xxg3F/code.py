def deepest(lst)
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(deepest([1, 4, 5]), 1)
Test.assert_equals(deepest([[2, 3], 4, [6, 7, [8]]]), 3)
Test.assert_equals(deepest([5, [[[[[[[[[[2]]]]]]]]]], [[[[[[[[[[[[4]]]]]]]]]]]]]), 13)
Test.assert_equals(deepest([[[3, 2, [[4]], 8], [[2, 4], 5]], 3, 5, [9, 1]]), 5)
Test.assert_equals(deepest([[6, 9, 6], [[[1, 4], 0, 8], [8, 0, [4, 1]]], [[5, 3, 4], [4, 3, 5]]]), 4)