from is_circular import is_circular
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(is_circular([[9, 8], [6, 9, 1], [8, 4, 2], [1, 9], [2, 1, 6]]), True)
Test.assert_equals(is_circular([[1, 2, 7], [7, 9, 3], [3], [3, 4], [4, 2, 1]]), True)
Test.assert_equals(is_circular([[1, 2], [2, 3], [3, 4], [4, 5]]), False)
Test.assert_equals(is_circular([[9, 9], [9, 2], [2, 9], [9, 5], [5, 9], [9, 6], [6, 9]]), True)
Test.assert_equals(is_circular([[1, 2], [4, 1], [3, 4], [2, 3]]), True)
Test.assert_equals(is_circular([[1, 1], [1, 2]]), False)
Test.assert_equals(is_circular([[6, 7, 8, 9], [1, 2, 3, 4, 5, 6], [6, 6, 9], [9, 0, 1]]), False)
Test.assert_equals(is_circular([[2, 1], [1, 2]]), True)
Test.assert_equals(is_circular([[2, 1], [1, 2], [2, 1], [1, 3, 1], [1, 4, 4]]), False)
