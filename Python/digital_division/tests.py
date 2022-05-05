from digital_division import digital_division
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(digital_division(21), 1, "Example #1")
Test.assert_equals(digital_division(128), 2, "Example #2")
Test.assert_equals(digital_division(100), 2, "Example #3")
Test.assert_equals(digital_division(12), "Perfect", "Example #4")
Test.assert_equals(digital_division(31), "Indivisible", "Example #5")
Test.assert_equals(digital_division(111), "Perfect")
Test.assert_equals(digital_division(40), 2)
Test.assert_equals(digital_division(35), "Indivisible")
Test.assert_equals(digital_division(666), 2)
Test.assert_equals(digital_division(735), "Perfect")
Test.assert_equals(digital_division(1890), 1)
Test.assert_equals(digital_division(444268), "Indivisible")
Test.assert_equals(digital_division(123456789), "Indivisible")
Test.assert_equals(digital_division(1), "Perfect")
