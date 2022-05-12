from is_icecream_sandwich import is_icecream_sandwich
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(is_icecream_sandwich(""), False, "too short")
Test.assert_equals(is_icecream_sandwich("AABBBAA"), True)
Test.assert_equals(is_icecream_sandwich("3&&3"), True)
Test.assert_equals(is_icecream_sandwich("yyyyymmmmmmmmyyyyy"), True)
Test.assert_equals(is_icecream_sandwich("hhhhhhhhmhhhhhhhh"), True)
Test.assert_equals(is_icecream_sandwich("CDC"), True)
Test.assert_equals(is_icecream_sandwich("BBBBB"), False, "only filling")
Test.assert_equals(is_icecream_sandwich("AAACCCAA"), False, "ends are unbalanced")
Test.assert_equals(is_icecream_sandwich("AACDCAA"), False, "can only have one type of filling")
Test.assert_equals(is_icecream_sandwich("AAABB"), False, "only one end")
Test.assert_equals(is_icecream_sandwich("AA"), False, "too short")
Test.assert_equals(is_icecream_sandwich("A"), False, "too short")
