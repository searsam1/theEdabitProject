from inc_or_dec import inc_or_dec
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(inc_or_dec(0), 1)
Test.assert_equals(inc_or_dec(1), 10)
Test.assert_equals(inc_or_dec(2), 100)
Test.assert_equals(inc_or_dec(3), 475)
Test.assert_equals(inc_or_dec(4), 1675)
Test.assert_equals(inc_or_dec(5), 4954)
Test.assert_equals(inc_or_dec(6), 12952)
# Mubashir
