from f import f
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(f(2), 0.5)
Test.assert_equals(f(10), 0.18)
Test.assert_equals(f(100), 0.031)
