from actual_memory_size import actual_memory_size
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(actual_memory_size("256MB"), "238MB")
Test.assert_equals(actual_memory_size("512MB"), "476MB")
Test.assert_equals(actual_memory_size("2GB"), "1.86GB")
Test.assert_equals(actual_memory_size("8GB"), "7.44GB")
Test.assert_equals(actual_memory_size("16GB"), "14.88GB")
Test.assert_equals(actual_memory_size("32GB"), "29.76GB")
Test.assert_equals(actual_memory_size("1GB"), "930MB")
