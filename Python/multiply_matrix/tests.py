from multiply_matrix import multiply_matrix
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(multiply_matrix([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]), [[30,36,42],[66,81,96],[102,126,150]])
Test.assert_equals(multiply_matrix([[1,2],[4,5]],[[1,2,3],[4,5,6],[7,8,9]]), "ERROR")
Test.assert_equals(multiply_matrix([[1,2,3],[4,5,6],[7,8,9]],[[1,2],[4,5]]), "ERROR")
Test.assert_equals(multiply_matrix([[1,2,3]],[[1],[2],[3]]), [[14]])
Test.assert_equals(multiply_matrix([[1],[2],[3]], [[1,2,3]]), [[1,2,3],[2,4,6],[3,6,9]])
Test.assert_equals(multiply_matrix([[8,8],[8,8]],[[7,7],[7,7]]), [[112,112],[112,112]])

# Author: Mariusz Najwer
