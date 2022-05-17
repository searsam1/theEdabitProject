from lemonade import lemonade
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(lemonade([5, 5, 5, 10, 20]), True)
Test.assert_equals(lemonade([5, 5, 10]), True)
Test.assert_equals(lemonade([10, 10]), False)
Test.assert_equals(lemonade([5, 5, 10, 10, 20]), False)
Test.assert_equals(lemonade([5, 5, 5, 5, 10, 5, 10, 10, 10, 20]), True)
Test.assert_equals(lemonade([5, 10, 5, 5, 5, 20, 5, 10, 5, 5, 10, 20]), True)
Test.assert_equals(lemonade([5, 10, 5, 5, 5, 20, 5, 10, 20, 5, 10, 20, 10]), False)
