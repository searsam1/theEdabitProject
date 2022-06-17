from combine_lists import combine_lists
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(combine_lists([False, 'False'], ['True', True, 'bool'], ['None', 'undefined']), [[False, 'True', 'None'], ['False', True, 'undefined'], ['*', 'bool', '*']])
Test.assert_equals(combine_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [[1, 4, 7], [2, 5,  8], [3, 6, 9]])
Test.assert_equals(combine_lists(['Jack', 'Joe', 'Jill'], ['Stuart', 'Sammy', 'Silvia'], ['Rick', 'Raymond', 'Riri']), [['Jack', 'Stuart', 'Rick'], ['Joe', 'Sammy',  'Raymond'], ['Jill', 'Silvia', 'Riri']])
Test.assert_equals(combine_lists(['JS', 'TS', 'CS'], ['React', 'Vue', 'Angular'], ['C', 'C++']), [['JS', 'React', 'C'], ['TS', 'Vue', 'C++'], ['CS', 'Angular', '*']])
