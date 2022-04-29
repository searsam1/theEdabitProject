from is_autobiographical import is_autobiographical
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")
		
Test.assert_equals(is_autobiographical(6210001000), True)
Test.assert_equals(is_autobiographical(12345), False)
Test.assert_equals(is_autobiographical(1210), True)
Test.assert_equals(is_autobiographical(638), False)
Test.assert_equals(is_autobiographical(0), False)

Test.assert_equals(is_autobiographical(10 ** 10), False)
Test.assert_equals(is_autobiographical(2020), True)
Test.assert_equals(is_autobiographical(3211000), True)
Test.assert_equals(is_autobiographical(3434343), False)
Test.assert_equals(is_autobiographical(2100), False)
