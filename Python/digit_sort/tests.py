from digit_sort import digit_sort
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(digit_sort([77, 23, 5, 7, 101]), [101, 23, 77, 5, 7])
Test.assert_equals(digit_sort([1, 5, 9, 2, 789, 563, 444]), [444, 563, 789, 1, 2, 5, 9])
Test.assert_equals(digit_sort([53219, 3772, 564, 32, 1]), [53219, 3772, 564, 32, 1])
Test.assert_equals(digit_sort([9, 667, 87, 56, 3023, 5555, 111]), [3023, 5555, 111, 667, 56, 87, 9])
