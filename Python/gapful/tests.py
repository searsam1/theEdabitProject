from gapful import gapful
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(gapful(25), 100)
Test.assert_equals(gapful(100), 100)
Test.assert_equals(gapful(103), 105)
Test.assert_equals(gapful(1442), 1441)
Test.assert_equals(gapful(3345), 3333)
Test.assert_equals(gapful(4780), 4773)
Test.assert_equals(gapful(3078), 3078)
