from block_player import block_player
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(block_player(0, 3), 6)
Test.assert_equals(block_player(0, 8), 4)
Test.assert_equals(block_player(4, 8), 0)
Test.assert_equals(block_player(2, 5), 8)
Test.assert_equals(block_player(1, 7), 4)
Test.assert_equals(block_player(0, 4), 8)
Test.assert_equals(block_player(3, 5), 4)
