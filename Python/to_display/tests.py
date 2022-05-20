from to_display import to_display
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		assert a == b
Test.assert_equals(to_display(0x0), 0x3F) # 0
Test.assert_equals(to_display(0x1), 0x06) # 1 right side
Test.assert_equals(to_display(0x2), 0x5B) # 2
Test.assert_equals(to_display(0x3), 0x4F) # 3
Test.assert_equals(to_display(0x4), 0x66) # 4
Test.assert_equals(to_display(0x5), 0x6D) # 5
Test.assert_equals(to_display(0x6), 0x7D) # 6 top hook
Test.assert_equals(to_display(0x7), 0x07) # 7 no middle slash
Test.assert_equals(to_display(0x8), 0x7F) # 8
Test.assert_equals(to_display(0x9), 0x6F) # 9 bottom hook
Test.assert_equals(to_display(0xA), 0x77) # A Upper case
Test.assert_equals(to_display(0xB), 0x7C) # b lower case
Test.assert_equals(to_display(0xC), 0x39) # C Upper case
Test.assert_equals(to_display(0xD), 0x5E) # d lower case
Test.assert_equals(to_display(0xE), 0x79) # E Upper case
Test.assert_equals(to_display(0xF), 0x71) # F Upper case