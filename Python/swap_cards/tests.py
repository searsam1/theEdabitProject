from swap_cards import swap_cards
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(swap_cards(41, 98), True)
Test.assert_equals(swap_cards(12, 28), True)
Test.assert_equals(swap_cards(67, 53), False)
Test.assert_equals(swap_cards(77, 54), False)
Test.assert_equals(swap_cards(45, 23), False)
Test.assert_equals(swap_cards(74, 81), True)
Test.assert_equals(swap_cards(75, 35), True)
Test.assert_equals(swap_cards(21, 25), True)
Test.assert_equals(swap_cards(22, 34), True)
Test.assert_equals(swap_cards(24, 12), False)
Test.assert_equals(swap_cards(52, 46), True)
Test.assert_equals(swap_cards(88, 45), False)
Test.assert_equals(swap_cards(48, 54), True)
Test.assert_equals(swap_cards(75, 87), True)
Test.assert_equals(swap_cards(13, 12), True)
Test.assert_equals(swap_cards(25, 41), True)
Test.assert_equals(swap_cards(48, 14), False)
