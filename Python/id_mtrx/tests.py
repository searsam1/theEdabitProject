from id_mtrx import id_mtrx
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")
		
Test.assert_equals(id_mtrx(1), [[1]])
Test.assert_equals(id_mtrx(2), [[1, 0], [0, 1]])
Test.assert_equals(id_mtrx(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
Test.assert_equals(id_mtrx(4), [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
Test.assert_equals(id_mtrx(-6), [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]])
Test.assert_equals(id_mtrx("edabit"), "Error", 'Incompatible types passed as n should return the string "Error".')

