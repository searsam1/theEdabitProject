from left_rotations import left_rotations
from left_rotations import right_rotations
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(left_rotations("abc"), ["abc", "bca", "cab"])
Test.assert_equals(left_rotations("abcdef"), ["abcdef", "bcdefa", "cdefab", "defabc", "efabcd", "fabcde"])
Test.assert_equals(left_rotations("himalaya"), ["himalaya", "imalayah", "malayahi", "alayahim", "layahima", "ayahimal", "yahimala", "ahimalay"])
Test.assert_equals(left_rotations("aab"), ["aab", "aba","baa"])
Test.assert_equals(right_rotations("abc"), ["abc", "cab", "bca"])
Test.assert_equals(right_rotations("abcdef"), ["abcdef", "fabcde", "efabcd", "defabc", "cdefab", "bcdefa"])
Test.assert_equals(right_rotations("himalaya"), ["himalaya", "ahimalay", "yahimala", "ayahimal", "layahima", "alayahim", "malayahi", "imalayah"])
Test.assert_equals(right_rotations("aab"), ["aab", "baa","aba"])
