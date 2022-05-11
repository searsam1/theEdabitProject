from all_pairs import all_pairs
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(all_pairs([2, 4, 5, 3], 7), [[2, 5], [3, 4]])
Test.assert_equals(all_pairs([5, 3, 9, 2, 1], 3), [[1, 2]])
Test.assert_equals(all_pairs([4, 5, 1, 3, 6, 8], 9), [[1, 8], [3, 6], [4, 5]])
Test.assert_equals(all_pairs([5, 2], 14), [])
Test.assert_equals(all_pairs([5, 5, 2], 14), [])
Test.assert_equals(all_pairs([8, 7, 7, 2, 4, 6], 14), [[6, 8], [7, 7]])
Test.assert_equals(all_pairs([8, 7, 2, 4, 6], 14), [[6, 8]])
Test.assert_equals(all_pairs([1, 3, 5, 4, 0], 4), [[0, 4], [1, 3]])
Test.assert_equals(all_pairs([1, 3, 5, 4, 0, 2], 4), [[0, 4], [1, 3]])
Test.assert_equals(all_pairs([1, 3, 5, 4, 0, 2, 2], 4), [[0, 4], [1, 3], [2, 2]])
