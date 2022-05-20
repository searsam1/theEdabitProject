from resistance_calculator import resistance_calculator
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(resistance_calculator([10, 20, 30, 40, 50]), [4.38, 150])
Test.assert_equals(resistance_calculator([25, 14, 65, 18]), [5.48, 122])
Test.assert_equals(resistance_calculator([10, 10]), [5, 20])
Test.assert_equals(resistance_calculator([0, 0, 0, 0]), [0,0])
Test.assert_equals(resistance_calculator([1.1, 2.1, 3.2, 4.3, 5.4, 6.5]), [0.44, 22.6])
Test.assert_equals(resistance_calculator([332.963, 87.036]), [69, 420])
Test.assert_equals(resistance_calculator([12345, 0]), [0, 12345])
