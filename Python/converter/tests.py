from converter import converter
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(converter(["celsius", 20], "kelvin"), 293.1)
Test.assert_equals(converter(["celsius", 5], "kelvin"), 278.1)
Test.assert_equals(converter(["celsius", 34], "fahrenheit"), 93.2)
Test.assert_equals(converter(["celsius", -2], "fahrenheit"), 28.4)
Test.assert_equals(converter(["kelvin", 18], "fahrenheit"), -427.3)
Test.assert_equals(converter(["kelvin", -10], "celsius"), -283.1)
Test.assert_equals(converter(["fahrenheit", 7], "kelvin"), 259.3)
Test.assert_equals(converter(["fahrenheit", 25], "celsius"), -3.9)
