from average_ascii import average_ascii
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(average_ascii("Edabit helps you learn in bitesize chunks"), "EDABIT HELPS you learn in BITESIZE CHUNKS")
Test.assert_equals(average_ascii("To be or not to be"), "To be or NOT to be")
Test.assert_equals(average_ascii("What you egg"), "WHAT you egg")
Test.assert_equals(average_ascii("Made by Harith Shah"), "Made by HARITH Shah")
Test.assert_equals(average_ascii("Boom"), "Boom")
Test.assert_equals(average_ascii("The most addictive way to learn"), "The most ADDICTIVE way to LEARN")
