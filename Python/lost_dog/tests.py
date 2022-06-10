from lost_dog import lost_dog
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(lost_dog([1,1,1,1,1,0], [0,1,1,1,1,1], [1,0,1,1,1,1], [1,1,0,1,1,1]), {'Dog1': 'House (1) and Room (6)', 'Dog2': 'House (2) and Room (1)', 'Dog3': 'House (3) and Room (2)', 'Dog4': 'House (4) and Room (3)'})
Test.assert_equals(lost_dog([1,1,0,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,0,1,1,1]), {'Dog1': 'House (1) and Room (3)', 'Dog2': 'House (4) and Room (3)'})
Test.assert_equals(lost_dog([1,1,0,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1]), {'Dog1': 'House (1) and Room (3)'})
Test.assert_equals(lost_dog([1,1,1,1,1,1], [0,1,1,1,1,1], [0,1,1,1,1,1], [1,1,1,1,1,1]),{'Dog1': 'House (2) and Room (1)', 'Dog2': 'House (3) and Room (1)'})
Test.assert_equals(lost_dog([1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1]), 'Dog not found!')
Test.assert_equals(lost_dog([1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,0,1,1]), {'Dog1': 'House (4) and Room (4)'})
