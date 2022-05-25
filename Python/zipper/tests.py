from zipper import zipper
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(zipper([5, 5, 7, 8, 9, 1, 2], [3, 2, 1, 1, 6, 6, 6, 6, 1, 2]), [4, 7])
Test.assert_equals(zipper([5, 4, 3, 2, 6], [6, 4, 3, 2, 6]), [0, 0])
Test.assert_equals(zipper([5, 4, 3, 2, 7], [6, 4, 3, 2, 6]), False)
Test.assert_equals(zipper([1, 5, 4, 3], [9, 8, 7, 5, 4, 3]), [0, 2])
Test.assert_equals(zipper([7, 8, 9, 9, 9], [8, 8, 9, 9, 9, 9, 9]), [1, 3])
Test.assert_equals(zipper([7, 8, 5, 1, 5], [6, 6, 5, 1, 5]), [1, 1])
Test.assert_equals(zipper([6, 6, 5, 1, 5], [6, 6, 5, 1, 5]), True)
Test.assert_equals(zipper([1, 1, 2, 6, 6, 5, 1, 5], [7, 8, 9, 4, 4, 6, 6, 5, 1, 5]), [2, 4])
