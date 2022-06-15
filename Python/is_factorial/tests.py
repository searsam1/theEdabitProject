from is_factorial import is_factorial
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(is_factorial(6), True)
Test.assert_equals(is_factorial(16), False)
Test.assert_equals(is_factorial(24), True)
Test.assert_equals(is_factorial(36), False)
Test.assert_equals(is_factorial(720), True)
Test.assert_equals(is_factorial(120), True)
Test.assert_equals(is_factorial(721), False)
