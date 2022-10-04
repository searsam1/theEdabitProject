
import math



def shape_in_shape(shape1, shape2):
    def Circle(r) : return math.pi * int(r)**2
    def Triangle(b, h) : return int(b) * int(h) / 2
    def Rectangle(width, l=None) : return int(width) * int(l) if l else int(width)**2
    def Pentagon(a) : return  ((5 * (5 + 2 * 5**.5))**.5 * int(a)**2) / 4
    def shape(s) : return list(map(lambda x: x.strip(","), s.split()))
    s1, s2 = shape(shape1), shape(shape2)
    res_s1 = {k : v(*s1[1:]) for k,v in vars().items() if k == s1[0]}
    res_s2 = {k : v(*s2[1:]) for k,v in vars().items() if k == s2[0]}
    return (res_s1[s1[0]] > res_s2[s2[0]])
    
    




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