def make_number(n):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(make_number(9), [[2,3,4], [4,5]], "Example #1")
Test.assert_equals(make_number(8), [], "Example #2")
Test.assert_equals(make_number(100), [[9,10,11,12,13,14,15,16], [18,19,20,21,22]], "Example #3")
Test.assert_equals(make_number(5), [[2,3]])
Test.assert_equals(make_number(18), [[3,4,5,6], [5,6,7]])
Test.assert_equals(make_number(40), [[6,7,8,9,10]])
Test.assert_equals(make_number(1), [])
Test.assert_equals(make_number(3), [[1, 2]])
Test.assert_equals(make_number(333), [
  [
    10, 11, 12, 13, 14, 15, 16,
    17, 18, 19, 20, 21, 22, 23,
    24, 25, 26, 27
  ],
  [
    33, 34, 35, 36, 37,
    38, 39, 40, 41
  ],
  [ 53, 54, 55, 56, 57, 58 ],
  [ 110, 111, 112 ],
  [ 166, 167 ]
])