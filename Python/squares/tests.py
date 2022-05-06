from squares import squares
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(squares(35, 70), 3)
Test.assert_equals(squares(100, 1000), 22)
Test.assert_equals(squares(3, 9), 2)
Test.assert_equals(squares(17, 24), 0)
Test.assert_equals(squares(433, 100000), 296)
Test.assert_equals(squares(1, 1000000000), 31622)
Test.assert_equals(squares(89784519, 103811134), 713)
Test.assert_equals(squares(50979851, 733216221), 19937)
