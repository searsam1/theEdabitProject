from column import column
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(column("A"), 1)
Test.assert_equals(column("B"), 2)
Test.assert_equals(column("Z"), 26)
Test.assert_equals(column("AA"), 27)
Test.assert_equals(column("BA"), 53)
Test.assert_equals(column("BB"), 54)
Test.assert_equals(column("CW"), 101)
Test.assert_equals(column("DD"), 108)
Test.assert_equals(column("PQ"), 433)
Test.assert_equals(column("ZZ"), 702)
Test.assert_equals(column("ABC"), 731)
Test.assert_equals(column("ZZT"), 18272)
Test.assert_equals(column("STVW"), 348059)
