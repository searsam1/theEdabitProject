from deep_count import deep_count
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(deep_count([1, 2, 3]), 3)
Test.assert_equals(deep_count(["x", "y", ["z"]]), 4)
Test.assert_equals(deep_count(["a", "b", ["c", "d", ["e"]]]), 7)
Test.assert_equals(deep_count([[1], [2], [3]]), 6)
Test.assert_equals(deep_count([[[[[[[[[]]]]]]]]]), 8)
Test.assert_equals(deep_count([None]), 1)
Test.assert_equals(deep_count([[]]), 1)
Test.assert_equals(deep_count([[None], [False, ["edabit"]], [0]]), 8)
