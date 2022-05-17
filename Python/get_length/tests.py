from get_length import get_length
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(get_length([1, [2,3]]), 3)
Test.assert_equals(get_length([1, [2, [3, 4]]]), 4)
Test.assert_equals(get_length([1, [2, [3, [4, [5, 6]]]]]), 6)
Test.assert_equals(get_length([1, 7, 8]), 3)
Test.assert_equals(get_length([2]), 1)
Test.assert_equals(get_length([2, [3], 4, [7]]), 4)
Test.assert_equals(get_length([2, [3, [5, 7]], 4, [7]]), 6)
Test.assert_equals(get_length([2, [3, [4, [5]]], [9]]), 5)
Test.assert_equals(get_length([]), 0)
