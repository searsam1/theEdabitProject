from alt_semi import alt_semi
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(alt_semi(1), 0)
Test.assert_equals(alt_semi(3), 2)
Test.assert_equals(alt_semi(4), 11)
Test.assert_equals(alt_semi(6), 571)
Test.assert_equals(alt_semi(9), 326036)
Test.assert_equals(alt_semi(16), 19696498855099)
Test.assert_equals(alt_semi(21), 48773618867405512406)
