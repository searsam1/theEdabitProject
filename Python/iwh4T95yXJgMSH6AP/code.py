def keep_skyline(grid):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(
	keep_skyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]),
	[[8, 0, 8, 7], [7, 4, 7, 7], [9, 4, 8, 7], [0, 3, 3, 0]]
)
Test.assert_equals(
	keep_skyline([[3, 1, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [1, 3, 1, 1]]),
	[[8, 4, 8, 7], [7, 4, 7, 7], [9, 4, 8, 7], [3, 3, 3, 3]]
)
Test.assert_equals(
	keep_skyline([[11, 19, 4, 5, 6], [6, 21, 5, 13, 4], [9, 2, 0, 11, 3]]),
	[[11, 19, 5, 13, 6], [11, 21, 5, 13, 6], [11, 11, 0, 11, 6]]
)
Test.assert_equals(
	keep_skyline([[11, 10, 6], [14, 5, 8], [7, 2, 0], [8, 18, 12], [2, 8, 4]]),
	[[11, 11, 11], [14, 14, 12], [7, 7, 0], [14, 18, 12], [8, 8, 8]]
)