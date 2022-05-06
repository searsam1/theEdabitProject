from remainder import remainder
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(remainder(7, 2), 1)
Test.assert_equals(remainder(3, 4), 3)
Test.assert_equals(remainder(5, 5), 0)
Test.assert_equals(remainder(1, 3), 1)
