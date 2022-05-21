from is_set import is_set
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(is_set(
[{"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"}, 
{"color": "red", "number": 1, "shade": "lined", "shape": "diamond"}, 
{"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"}]
), False)

Test.assert_equals(is_set(
[{"color": "purple", "number": 3, "shade": "full", "shape": "oval"}, 
{"color": "green", "number": 1, "shade": "full", "shape": "oval"}, 
{"color": "red", "number": 3, "shade": "full", "shape": "oval"}]
), False)

Test.assert_equals(is_set(
[{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"}, 
{"color": "red", "number": 2, "shade": "lined", "shape": "diamond"}, 
{"color": "purple", "number": 3, "shade": "full", "shape": "oval"}]
), False)

Test.assert_equals(is_set(
[{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"}, 
{"color": "red", "number": 1, "shade": "lined", "shape": "diamond"}, 
{"color": "red", "number": 1, "shade": "lined", "shape": "oval"}]
), False)

Test.assert_equals(is_set(
[{"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"}, 
{"color": "red", "number": 1, "shade": "lined", "shape": "diamond"}, 
{"color": "red", "number": 1, "shade": "lined", "shape": "oval"}]
), True)

Test.assert_equals(is_set(
[{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"}, 
{"color": "red", "number": 2, "shade": "lined", "shape": "diamond"}, 
{"color": "red", "number": 3, "shade": "full", "shape": "oval"}]
), True)

Test.assert_equals(is_set(
[{"color": "green", "number": 1, "shade": "empty", "shape": "squiggle"}, 
{"color": "green", "number": 2, "shade": "empty", "shape": "diamond"}, 
{"color": "green", "number": 3, "shade": "empty", "shape": "oval"}]
), True)

Test.assert_equals(is_set(
[{"color": "purple", "number": 1, "shade": "full", "shape": "oval"}, 
{"color": "green", "number": 1, "shade": "full", "shape": "oval"}, 
{"color": "red", "number": 1, "shade": "full", "shape": "oval"}]
), True)
