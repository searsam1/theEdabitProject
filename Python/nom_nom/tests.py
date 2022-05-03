from nom_nom import nom_nom
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(nom_nom([1, 2, 3]), [1, 2, 3])
Test.assert_equals(nom_nom([2, 1, 3]), [3, 3])
Test.assert_equals(nom_nom([8, 5, 9]), [22])
Test.assert_equals(nom_nom([5, 3, 7]), [15])
Test.assert_equals(nom_nom([5, 3, 9]), [8, 9])
Test.assert_equals(nom_nom([6, 5, 6, 100]), [17, 100])
