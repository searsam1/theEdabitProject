from product_pair import product_pair
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

lst = [1, -2, -3, 4, 6, 7]
Test.assert_equals(product_pair(lst[:], 1), (-3, 7))
Test.assert_equals(product_pair(lst[:], 2), (-21, 42))
Test.assert_equals(product_pair(lst[:], 3), (-126, 168))
Test.assert_equals(product_pair(lst[:], 6), (1008, 1008))
Test.assert_equals(product_pair(lst[:], 7), None)
Test.assert_equals(product_pair([0,1,2,3,4], 2), (0, 12))
Test.assert_equals(product_pair([0,-1,-2,-3,-4], 2), (0, 12))
Test.assert_equals(product_pair([0,-1,-2,-3,-4], 3), (-24, 0))
Test.assert_equals(product_pair([-1,-2,-3,-4], 2), (2, 12))
Test.assert_equals(product_pair([-1,-2,-3,-4], 3), (-24, -6))
Test.assert_equals(product_pair([], 2), None)
Test.assert_equals(product_pair([-4, -10, -1], 2), (4, 40))
Test.assert_equals(product_pair([0, 6, 3, 5, 4], 4), (0, 360))
Test.assert_equals(product_pair([5, 4, 3, 3, 6], 2), (9, 30))
lst.extend([0] * 10)
Test.assert_equals(product_pair(lst[:], 2), (-21, 42))
Test.assert_equals(product_pair(lst[:], 3), (-126, 168))
lst.extend([0] * 20)
Test.assert_equals(product_pair(lst[:], 2), (-21, 42))
Test.assert_equals(product_pair(lst[:], 3), (-126, 168))
lst.extend([0] * 50)
Test.assert_equals(product_pair(lst[:], 2), (-21, 42))
Test.assert_equals(product_pair(lst[:], 3), (-126, 168))
# Mubashir
