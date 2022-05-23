from alternate_sort import alternate_sort
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(alternate_sort([5, 1, "a", "c", 2, 1, 3, "c", "b", "e"]), [1, "a", 1, "b", 2, "c", 3, "c", 5, "e"])
Test.assert_equals(alternate_sort([-2, "f", "A", 0, 100, "z"]), [-2, "A", 0, "f", 100, "z"])
Test.assert_equals(alternate_sort(["a", "b", "c", 1, 2, 3]), [1, "a", 2, "b", 3, "c"])
Test.assert_equals(alternate_sort(["e", "d", "a", "b", "i", "t", 1, 10, 100, 2, 20, 200]), [1, "a", 2, "b", 10, "d", 20, "e", 100, "i", 200, "t"])
Test.assert_equals(alternate_sort(["X", 15, 12, 18, "Y", "Z"]), [12, "X", 15, "Y", 18, "Z"])
