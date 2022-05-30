from depth import depth
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(depth([1, 2, 3, 4]), 1)
Test.assert_equals(depth([1, [2, 3, 4]]), 2)
Test.assert_equals(depth([1, [2, [3, 4]]]), 3)
Test.assert_equals(depth([1, [2, [3, [4]]]]), 4)

## More Tests
Test.assert_equals(depth([1, [2, [3, [4]]], 4]), 4)
Test.assert_equals(depth([1, [2], 3, [4], 5, [6]]), 2)
Test.assert_equals(depth([1, 2, 3, 4, [[5]], [6], 7]), 3)
