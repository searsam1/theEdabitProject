from replace_next_largest import replace_next_largest
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(replace_next_largest([5, 7, 3, 2, 8]), [7, 8, 5, 3, -1])
Test.assert_equals(replace_next_largest([4, 1, 6, -7, -8, 2]), [6, 2, -1, 1, -7, 4])
Test.assert_equals(replace_next_largest([2, 3, 4, 5]), [3, 4, 5, -1])
Test.assert_equals(replace_next_largest([1, 0, -1, 8, -72]), [8, 1, 0, -1, -1])
