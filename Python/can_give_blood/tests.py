from can_give_blood import can_give_blood
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

tests = [
	(("O+", "A+"), True),
	(("A-", "B-"), False),
	(("A-", "AB+"), True),
	(("AB-", "B-"), False),
	(("AB+", "A+"), False),
	(("O-", "A-"), True),
	(("A-", "O-"), False),
	(("O+", "AB-"), False),
	(("O-", "AB+"), True),
	(("AB+", "AB+"), True),
	(("O+", "O-"), False),
	]
	
for test in tests:
	print("Input: " + str(test[0]))
	Test.assert_equals(can_give_blood(*test[0]), test[1])
