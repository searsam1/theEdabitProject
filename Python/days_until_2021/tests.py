from days_until_2021 import days_until_2021
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(days_until_2021("12/29/2020"), "3 days")
Test.assert_equals(days_until_2021("1/1/2020"), "366 days")
Test.assert_equals(days_until_2021("2/28/2020"), "308 days")
Test.assert_equals(days_until_2021("6/30/2020"), "185 days")
Test.assert_equals(days_until_2021("10/22/2020"), "71 days")
Test.assert_equals(days_until_2021("12/31/2020"), "1 day")
