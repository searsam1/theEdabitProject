from boxes import boxes
import unittest

i = 0
class Test(unittest.TestCase):
	
	def assert_equals(a,b,message=None):
		global i
		i += 1
		s = f"[Challenge {i} ➜ " + f'{["Fail", "Pass"][a==b]}]\t'
		res = "\t{"  + f"[{a}]"  + f"[{b}]" + "\t}"
		print("<" + "-" * (len(s)-1),end="")
		print(res,end=" - ")
		print(s,end="")
		print("-" * (len(s)-1) + ">",end="")
		print("\n",end="")
		
		






Test.assert_equals(boxes([7, 1, 2, 6, 1, 2, 3, 5, 9, 2, 1, 2, 5]), 5)
Test.assert_equals(boxes([2, 7, 1, 3, 3, 4, 7, 4, 1, 8, 2]), 5)
Test.assert_equals(boxes([1, 3, 3, 3, 2, 1, 1, 9, 7, 10, 8, 6, 1, 2, 9]), 8)
Test.assert_equals(boxes([4, 1, 2, 3, 5, 5, 1, 9]), 3)
Test.assert_equals(boxes([3, 1, 2, 7, 2, 6, 1]), 3)
Test.assert_equals(boxes([4, 6, 1, 9, 6, 1, 1, 9, 2, 9]), 6)
Test.assert_equals(boxes([2, 2, 10, 10, 1, 5, 2]), 4)
Test.assert_equals(boxes([9, 6, 2, 3, 1, 2, 4, 8, 3, 1, 3]), 5)
Test.assert_equals(boxes([2, 5, 1, 6, 2, 9, 5, 2, 1, 6, 1, 6, 6, 1]), 7)
Test.assert_equals(boxes([1, 2, 3, 2, 6, 4, 1]), 3)
Test.assert_equals(boxes([1, 1, 2, 1, 2, 10, 2, 2, 5, 1, 5]), 4)
Test.assert_equals(boxes([8, 3, 2, 1, 1, 2, 1, 3, 2, 1]), 3)
Test.assert_equals(boxes([1, 5, 3, 1, 2, 3, 2, 6, 3, 1, 3, 8, 1]), 5)
Test.assert_equals(boxes([8, 1, 1, 4, 7, 2, 1, 3, 1, 9, 7, 1, 5, 1, 1]), 7)
Test.assert_equals(boxes([2, 3, 4, 10, 1, 2, 5, 1, 1, 1, 1, 8, 2, 1]), 5)
Test.assert_equals(boxes([4, 6, 7, 3, 2, 2, 3, 1, 2, 2, 10, 3, 2]), 6)
Test.assert_equals(boxes([9, 2, 3, 4, 1, 3, 1, 1, 3]), 3)
Test.assert_equals(boxes([6, 2, 1, 9, 1, 8, 2, 8, 6, 6]), 6)
Test.assert_equals(boxes([6, 9, 3, 8, 10, 4, 7]), 7)
Test.assert_equals(boxes([4, 3, 1, 1, 1, 4, 7, 2, 1, 10, 1, 3, 8]), 6)
Test.assert_equals(boxes([10]), 1)
