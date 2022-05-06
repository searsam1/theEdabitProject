from left_side import left_side
from left_side import right_side
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(left_side([5, 2, 1, 4, 8, 7]), [0, 0, 0, 2, 4, 4])
Test.assert_equals(left_side([3, 8, 2, 5, 4]), [0, 1, 0, 2, 2])
Test.assert_equals(left_side([1, 2, 3, 4, 5]), [0, 1, 2, 3, 4])
Test.assert_equals(right_side([5, 2, 1, 4, 8, 7]), [3, 1, 0, 0, 1, 0])
Test.assert_equals(right_side([3, 8, 2, 5, 4]), [1, 3, 0, 1, 0])
Test.assert_equals(right_side([1, 2, 3, 4, 5]), [0, 0, 0, 0, 0])
