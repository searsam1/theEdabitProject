from is_disarium import is_disarium
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")
		
num_vector, res_vector = [
  [6, 75, 135, 466, 372, 175, 1, 696, 876, 89, 518, 598],
  [True, False, True, False, False, True, True, False, False, True, True, True]
]
for i, n in enumerate(num_vector): Test.assert_equals(is_disarium(n), res_vector[i])
