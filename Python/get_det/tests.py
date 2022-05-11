from get_det import get_det
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(get_det([[0,1],[1,0]]), -1)
Test.assert_equals(get_det([[69,0],[1,1]]), 69)
Test.assert_equals(get_det([[7,420,8],[5,7,0],[1,1,7]]), -14373)
Test.assert_equals(get_det([[5,1],[1,6]]), 29)
Test.assert_equals(get_det([[1,2,3],[4,5,6],[7,8,9]]), 0)
Test.assert_equals(get_det([[-1,1,-1],[-1,-55,1],[1,-1,-1]]), -112)
Test.assert_equals(get_det([[2,7,6],[9,5,1],[4,3,8]]), -360)
