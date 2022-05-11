from integer_to_string import integer_to_string
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(integer_to_string(10, 2), "1010")
Test.assert_equals(integer_to_string(1642, 8), "3152")
Test.assert_equals(integer_to_string(102, 2), "1100110")
Test.assert_equals(integer_to_string(212, 16), "d4")
Test.assert_equals(integer_to_string(18, 2), "10010")
Test.assert_equals(integer_to_string(3162, 16), "c5a")
Test.assert_equals(integer_to_string(10, 8), "12")
Test.assert_equals(integer_to_string(162, 8), "242")
Test.assert_equals(integer_to_string(27, 2), "11011")
Test.assert_equals(integer_to_string(4321, 16), "10e1")
Test.assert_equals(integer_to_string(1622, 16), "656")
