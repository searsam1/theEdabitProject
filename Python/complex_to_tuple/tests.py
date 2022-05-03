from complex_to_tuple import complex_to_tuple
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(complex_to_tuple("1+2i"), (1,2))
Test.assert_equals(complex_to_tuple("6+9i"), (6,9))
Test.assert_equals(complex_to_tuple("-7-2i"), (-7,-2))
Test.assert_equals(complex_to_tuple("3-4i"), (3,-4))
