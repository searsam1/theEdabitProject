from fair_die import fair_die
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(fair_die([8, 10, 5, 15, 15, 10]), True, '7.38 < 11.0705')
Test.assert_equals(fair_die([21, 22, 17, 31, 29, 30]), True, '6.64 < 11.0705')
Test.assert_equals(fair_die([8, 16, 16, 9, 11, 3]), False, '11.95 > 11.0705')
Test.assert_equals(fair_die([14, 10, 16, 14, 15, 15]), True, '1.57 < 11.0705')
Test.assert_equals(fair_die([7, 18, 15, 21, 14, 28]), False, '14.61 > 11.0705')
Test.assert_equals(fair_die([29, 34, 33, 38, 41, 35]), True, '2.46 < 11.0705')
Test.assert_equals(fair_die([10, 20, 11, 5, 19, 16]), False, '12.56 < 11.0705')
