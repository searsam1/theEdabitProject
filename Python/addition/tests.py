from addition import addition
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(addition(2), 3, "2 plus 1 equals 3.")
Test.assert_equals(addition(-9), -8, "-8 plus 1 equals 9.")
Test.assert_equals(addition(0), 1, "0 plus 1 equals 1.")
Test.assert_equals(addition(999), 1000, "999 plus 1 equals 1000.")
Test.assert_equals(addition(73), 74, "73 plus 1 equals 74.")
