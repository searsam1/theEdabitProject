from sum_ff import sum_ff
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(sum_ff(98), 16)
Test.assert_equals(sum_ff(435), 74)
Test.assert_equals(sum_ff(534), 188)
Test.assert_equals(sum_ff(3123), 353)
Test.assert_equals(sum_ff(1232), 1931)
Test.assert_equals(sum_ff(12), 7)
Test.assert_equals(sum_ff(31232), 32630)
Test.assert_equals(sum_ff(4234), 208)
Test.assert_equals(sum_ff(655), 0)
Test.assert_equals(sum_ff(432), 1240)
Test.assert_equals(sum_ff(2343), 170)
