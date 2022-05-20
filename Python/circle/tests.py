from circle import circle
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(circle(3), 82.699)
Test.assert_equals(circle(4), 90.032)
Test.assert_equals(circle(8), 97.45)
Test.assert_equals(circle(90), 99.98)
Test.assert_equals(circle(600), 100.0)
