from goldbach_conjecture import goldbach_conjecture
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(goldbach_conjecture(1), [])
Test.assert_equals(goldbach_conjecture(4), [2, 2])
Test.assert_equals(goldbach_conjecture(7), [])
Test.assert_equals(goldbach_conjecture(8), [3, 5])
Test.assert_equals(goldbach_conjecture(10), [3, 7])
Test.assert_equals(goldbach_conjecture(24), [5, 19])
Test.assert_equals(goldbach_conjecture(100), [3, 97])
Test.assert_equals(goldbach_conjecture(1234), [3, 1231])
Test.assert_equals(goldbach_conjecture(1400), [19, 1381])
Test.assert_equals(goldbach_conjecture(1566), [7, 1559])
Test.assert_equals(goldbach_conjecture(3444), [11, 3433])
# Mubashir
