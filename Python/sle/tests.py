from sle import sle
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		if a != b : print(message) if message else print(a == b)
		return a == b

t1 = Test.assert_equals(sle([[1, 2, -1], [2, -3, 5]]), (1, -1))
Test.assert_equals(sle([[3, -4, 1], [2, 3, 12]]), (3, 2))
Test.assert_equals(sle([[1, -4, 12], [3, -12, 36]]), False)
Test.assert_equals(sle([[3, 2, -4], [2, 5, 1]]), (-2, 1))
Test.assert_equals(sle([[5, 3, -11], [2, 4, -10]]), (-1, -2))
Test.assert_equals(sle([[3, 1, 38], [3, 1, 83]]), False)
