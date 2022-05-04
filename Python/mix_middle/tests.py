from mix_middle import mix_middle
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(mix_middle("the quick brown fox jumps high"), "the qciuk bworn fox jpmus hgih")
Test.assert_equals(mix_middle("this sentence is quite muddled"), "tihs scnetnee is qtiue melddud")
Test.assert_equals(mix_middle("buying a first-class ticket"), "bniyug a fsalc-tsris tekcit")
Test.assert_equals(mix_middle("hello world"), "hlleo wlrod")
Test.assert_equals(mix_middle("is it a cat or a dog"), "is it a cat or a dog")
