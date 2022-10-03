def shape_in_shape(shape1, shape2):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(shape_in_shape("Circle, 3", "Rectangle, 3, 14"), False)
Test.assert_equals(shape_in_shape("Circle, 5", "Rectangle, 3, 14"), True)
Test.assert_equals(shape_in_shape("Triangle, 5, 5", "Circle, 2"), False)
Test.assert_equals(shape_in_shape("Triangle, 10, 5", "Circle, 2"), True)
Test.assert_equals(shape_in_shape("Circle, 10", "Pentagon, 10"), True)
Test.assert_equals(shape_in_shape("Pentagon, 10", "Circle, 10"), False)