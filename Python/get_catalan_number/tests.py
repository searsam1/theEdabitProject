from get_catalan_number import get_catalan_number
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		assert a == b

Test.assert_equals(get_catalan_number(0), 1)
Test.assert_equals(get_catalan_number(3), 5)
Test.assert_equals(get_catalan_number(7), 429)
Test.assert_equals(get_catalan_number(8), 1430)
Test.assert_equals(get_catalan_number(9), 4862)
Test.assert_equals(get_catalan_number(1), 1)
Test.assert_equals(get_catalan_number(4), 14)
Test.assert_equals(get_catalan_number(11), 58786)
Test.assert_equals(get_catalan_number(17), 129644790)