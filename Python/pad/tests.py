from pad import pad
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(pad("Even"), "Even lololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololol")
Test.assert_equals(pad("Odd"), "Oddlolololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololol")
Test.assert_equals(pad("I love the new challenge"), "I love the new challenge lololololololololololololololololololololololololololololololololololololololololololololololololololololololololol")
Test.assert_equals(pad("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus dolor purus, finibus eget magna vel, suscipit semper nibh. Quisque posuere."), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus dolor purus, finibus eget magna vel, suscipit semper nibh. Quisque posuere.")
