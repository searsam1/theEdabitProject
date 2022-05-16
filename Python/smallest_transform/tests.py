from smallest_transform import smallest_transform
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(smallest_transform(399), 6)
Test.assert_equals(smallest_transform(1234), 4)
Test.assert_equals(smallest_transform(153), 4)
Test.assert_equals(smallest_transform(33338), 5)
Test.assert_equals(smallest_transform(7777), 0)
Test.assert_equals(smallest_transform(977), 2)
Test.assert_equals(smallest_transform(589), 4)
