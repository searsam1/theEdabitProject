from prime_count import prime_count
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")
		
Test.assert_equals(prime_count(1, 10), 4)
Test.assert_equals(prime_count(1, 100), 25)
Test.assert_equals(prime_count(1, 1000), 168)
Test.assert_equals(prime_count(1, 10000), 1229)
Test.assert_equals(prime_count(1, 100000), 9592)
Test.assert_equals(prime_count(2090, 2098), 0)
Test.assert_equals(prime_count(548, 556), 0)
Test.assert_equals(prime_count(3297, 4297), 128)
