from is_happy import is_happy
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

num_vector, res_vector = [
  [1, 10, 44, 67, 89, 139, 1327, 2871, 3970, 5209, 6329, 8888, 9331, 10000],
  [True, True, True, False, False, True, False, False, True, False, True, False, True, True]
]
for i, n in enumerate(num_vector): Test.assert_equals(res_vector[i], is_happy(n))
