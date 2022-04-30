from is_ord_sub import is_ord_sub
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")
		
Test.assert_equals(is_ord_sub([4, 3], [3, 4]), False)
Test.assert_equals(is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]), True)
Test.assert_equals(is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]), True)
Test.assert_equals(is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]), False)
Test.assert_equals(is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]), True)
Test.assert_equals(is_ord_sub([0, 1, 0, 1], [1, 0, 1, 0, 1]), True)
Test.assert_equals(is_ord_sub([0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 1, 1, 0]), False)
Test.assert_equals(is_ord_sub([0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0]), False)
Test.assert_equals(is_ord_sub([1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]), False)
Test.assert_equals(is_ord_sub([1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1]), True)
