from can_build import can_build
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], []), True)
Test.assert_equals(can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 8]), True)
Test.assert_equals(can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 80]), True)
Test.assert_equals(can_build([0, 1, 2, 2, 3, 0, 0, 0, 1, 1], [123, 444, 92]), True)
Test.assert_equals(can_build([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 23, 45, 6789]), True)
Test.assert_equals(can_build([0, 2, 3, 0, 5, 0, 0, 0, 0, 1], [11, 2, 22, 49, 444, 4]), True)
Test.assert_equals(can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 80, 0]), False)
Test.assert_equals(can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1]), False)
Test.assert_equals(can_build([0, 2, 3, 0, 5, 0, 0, 0, 0, 1], [11, 7, 2, 22, 49, 444, 4]), False)
Test.assert_equals(can_build([0, 2, 3, 0, 5, 0, 0, 0, 0, 1], [11, 2, 22, 49, 444, 44]), False)
Test.assert_equals(can_build([10, 2, 3, 8, 5, 8, 5, 5, 3, 1], [11, 2, 22, 49, 444, 998, 87, 44]), False)
