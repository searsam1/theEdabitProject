from overlapping import overlapping
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(overlapping([(4, 24), (3, 10), (4, 18)]), (4, 10))
Test.assert_equals(overlapping([(4, 9), (8, 22), (8, 24)]), (8, 9))
Test.assert_equals(overlapping([(12, 16), (11, 20), (11, 24)]), (12, 16))
Test.assert_equals(overlapping([(9, 13), (12, 17), (11, 23), (3, 21)]), (12, 13))
Test.assert_equals(overlapping([(5, 9), (7, 8), (2, 11), (2, 12)]), (7, 8))
Test.assert_equals(overlapping([(4, 18), (6, 17), (5, 8), (6, 16)]), (6, 8))
Test.assert_equals(overlapping([(4, 9), (8, 22), (10, 24)]), 'No overlapping')
Test.assert_equals(overlapping([(9, 11), (12, 17), (11, 23), (3, 21)]), 'No overlapping')
Test.assert_equals(overlapping([(4, 24), (24, 25), (4, 30)]), (24, 24))
