from has_consecutive_series import has_consecutive_series
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(has_consecutive_series([1, 2, 3], [1, 1, 1]), True)
Test.assert_equals(has_consecutive_series([1, 2, 3], [1, 2, 1]), False)
Test.assert_equals(has_consecutive_series([4, 6, -5, 8, 4], [-2, -3, 9, -3, 2]), True)
Test.assert_equals(has_consecutive_series([12, 3], [0, 10, 14, 15, 16]), True)
Test.assert_equals(has_consecutive_series([8, 6, 10], [25, 28, 25, 26, 28, 29]), False)
Test.assert_equals(has_consecutive_series([11, 5, 3], [-2, 5, 8, 12]), True)
Test.assert_equals(has_consecutive_series([11, 5, 3], [-2, 5, 8, 11]), False)
