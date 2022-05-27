from is_stretched import is_stretched
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(is_stretched("pppaaannndddaaa", "panda"), True)
Test.assert_equals(is_stretched("hheelllloo", "hello"), True)
Test.assert_equals(is_stretched("magnet", "magnet"), True)
Test.assert_equals(is_stretched("eeeeemmmmmoooootttttiiiiiooooonnnnn", "emotion"), True)
Test.assert_equals(is_stretched("sssshhiipp", "ship"), False)
Test.assert_equals(is_stretched("cccaaannnddooorrr", "candor"), False)
Test.assert_equals(is_stretched("relationshiipp", "relationship"), False)
Test.assert_equals(is_stretched("magneto", "magnet"), False)
Test.assert_equals(is_stretched("maggnet", "magnet"), False)
