from phi import phi
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(phi(1), 1)
Test.assert_equals(phi(3), 2)
Test.assert_equals(phi(9), 6)
Test.assert_equals(phi(19), 18)
Test.assert_equals(phi(33), 20)
Test.assert_equals(phi(51), 32)
Test.assert_equals(phi(54), 18)
Test.assert_equals(phi(86), 42)
Test.assert_equals(phi(144), 48)
Test.assert_equals(phi(209), 180)
Test.assert_equals(phi(666), 216)
Test.assert_equals(phi(1000), 400)
