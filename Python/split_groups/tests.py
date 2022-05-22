from split_groups import split_groups
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(split_groups('aaabbbaabbab'), ['aaa', 'bbb', 'aa', 'bb', 'a', 'b'])
Test.assert_equals(split_groups('5556667788'), ['555', '666', '77', '88'])
Test.assert_equals(split_groups('abbbcc88999&&!!!_'), ['a', 'bbb', 'cc', '88', '999', '&&', '!!!', '_'], 'It should work with special chars.')
Test.assert_equals(split_groups('555'), ['555'])
Test.assert_equals(split_groups('AABBCC'), ['AA', 'BB', 'CC'])
