from change_string import change_string
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(change_string("ApPle"), "ELQPB")
Test.assert_equals(change_string("draGON"), "OPHARD")
Test.assert_equals(change_string("ZebrA"),  "BRBEA")
Test.assert_equals(change_string("sNaKe"), "ELAOS")
Test.assert_equals(change_string("MElon"), "NOLFN")
