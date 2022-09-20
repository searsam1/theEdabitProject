def group_monotonic(a):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsolelst = [
    [[], []],
    [[0], []],
    [[1], []],
    [[0, 1], []],
    [[1, 0], []],
    [[1, 1], []],
    [[0, 1, 2], []],
    [[2, 1, 0], []],
    [[0, 2, 1], [1]],
    [[1, 0, 2], [1]],
    [[0, 1, 1, 0], [2]],
    [[1, 2, 3, 4, 4, 4, 3, 2, 1], [5]],
    [[0, 6, 10, 9, 3, -3, -9, -10, -6, 0], [2, 7]]]
for input, output in lst:
    Test.assert_equals(group_monotonic(input), output)