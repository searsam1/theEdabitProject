from split import split
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(split("beautifully"), ["b", "eau", "t", "i", "f", "u", "l", "l", "y"])
Test.assert_equals(split("spoonful"), ["s", "p", "oo", "n", "f", "u", "l"])
Test.assert_equals(split("swimming"), ["s", "w", "i", "m", "m", "i", "n", "g"])
Test.assert_equals(split("courage"), ["c", "ou", "r", "a", "g", "e"])
Test.assert_equals(split("cooing"), ["c", "ooi", "n", "g"])
