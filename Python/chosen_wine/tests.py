from chosen_wine import chosen_wine
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(chosen_wine([{"name": "Wine A", "price": 8.99}, {"name": "Wine 32", "price": 13.99}, {"name": "Wine 9", "price": 10.99}]), "Wine 9")
Test.assert_equals(chosen_wine([{"name": "Wine A", "price": 8.99}, {"name": "Wine B", "price": 9.99}]), "Wine B")
Test.assert_equals(chosen_wine([{"name": "Wine A", "price": 8.99}]), "Wine A")
Test.assert_equals(chosen_wine([]), None)
Test.assert_equals(chosen_wine([{"name": "Wine A", "price": 8.99}, {"name": "Wine 389", "price": 109.99}, {"name": "Wine 44", "price": 38.44}, {"name": "Wine 72", "price": 22.77}]), "Wine 72")
