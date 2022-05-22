from bw_transform import bw_transform
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(bw_transform("banana$"), "annb$aa")
Test.assert_equals(bw_transform("mississippi$"), "ipssm$pissii")
Test.assert_equals(bw_transform("abaaba$"), "abba$aa")
Test.assert_equals(bw_transform("acccgtttgtttcaatagatccatcaa$"), "aacc$tacgttctaccatcaatatttgg")
