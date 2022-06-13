from fib_seq import fib_seq
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(fib_seq(2), [0,1])
Test.assert_equals(fib_seq(4), [0,1,1,2])
Test.assert_equals(fib_seq(0), [])
Test.assert_equals(fib_seq(7), [0,1,1,2,3,5,8])
Test.assert_equals(fib_seq(), None, 'An empty input has to return None')
Test.assert_equals(fib_seq(20), [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181])
Test.assert_equals(fib_seq(1), [0])
