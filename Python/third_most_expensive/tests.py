from third_most_expensive import third_most_expensive
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(third_most_expensive({}), False)
Test.assert_equals(third_most_expensive({"piano": 100}), False)
Test.assert_equals(third_most_expensive({"piano": 100, "stereo": 200 }), False)
Test.assert_equals(third_most_expensive({"piano": 100, "stereo": 200, "tv": 10 }), "tv")
Test.assert_equals(third_most_expensive({"piano": 100, "stereo": 200, "tv": 10, "timmy": 500 }), "piano")
Test.assert_equals(third_most_expensive({"computer": 1000, "piano": 500, "stereo": 200, "tv": 10, "timmy": 1 }), "stereo")

# Author: Miguel Carvalho
