def triplet_sum(lst, n):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(triplet_sum([1, 2, 6, 3, 4, 5, 9, 10, 11], n = 20), 5)
Test.assert_equals(triplet_sum([6, 2, 6], n = 9), 0)
Test.assert_equals(triplet_sum([6, 2, 6, 0, 9, 2, 5, 8], n = 15), 2)
Test.assert_equals(triplet_sum([1, -2, 0, 6, 11, 15, 6, 2, 6, 0, 9, 2, 5, 8], n = 15), 9)
Test.assert_equals(triplet_sum([1,15], n = 16), 0, "There are no triplets in a list of two elements.")
Test.assert_equals(triplet_sum([], n = 0), 0, "There are no triplets in an empty list.")