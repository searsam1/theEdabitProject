from dial import dial
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")
		
Test.assert_equals(dial("1-800-HOTLINEBLING"), "1-800-468546325464")
Test.assert_equals(dial("hello-world!"), "43556-96753!")
Test.assert_equals(dial("aaaabcccdefggg"), "22222222333444")
Test.assert_equals(dial("01023468adghijgkmz?"), "010234682344454569?")
Test.assert_equals(dial("SwApPeDcAsE"), "79277332273")
Test.assert_equals(dial("VAPORWAVE"), "827679283")
