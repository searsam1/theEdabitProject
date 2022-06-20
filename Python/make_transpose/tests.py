from make_transpose import make_transpose
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(make_transpose([[1,2,3],[4,5,6],[7,8,9]]), [[1,4,7],[2,5,8],[3,6,9]])
Test.assert_equals(make_transpose([[1,2],[3,4],[5,6]]), [[1,3,5],[2,4,6]])
Test.assert_equals(make_transpose([[1,2],[3,4],[5,6],[7,8],[9,10]]), [[1,3,5,7,9],[2,4,6,8,10]])
Test.assert_equals(make_transpose([[42]]), [[42]])
Test.assert_equals(make_transpose([[0.5,0.6,0.8]]), [[0.5],[0.6],[0.8]])
Test.assert_equals(make_transpose([[0,0]]), [[0],[0]])
Test.assert_equals(make_transpose([["a","b"]]), [["a"],["b"]])

# Author: Mariusz Najwer
