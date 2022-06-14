from who_won import who_won
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(who_won([
	["X", "O", "X"],
	["X", "O", "O"],
	["X", "X", "O"],
]), "X")

Test.assert_equals(who_won([
	["O", "X", "O"],
	["X", "X", "O"],
	["O", "X", "X"],
]), "X")

Test.assert_equals(who_won([
	["X", "X", "O"],
	["O", "X", "O"],
	["X", "O", "O"],
]), "O")

Test.assert_equals(who_won([
	["X", "X", "X"],
	["O", "X", "O"],
	["X", "O", "O"],
]), "X")

Test.assert_equals(who_won([
	["X", "O", "X"],
	["O", "O", "O"],
	["X", "X", "O"],
]), "O")

Test.assert_equals(who_won([
	["O", "O", "X"],
	["X", "O", "X"],
	["O", "X", "O"],
]), "O")

Test.assert_equals(who_won([
	["O", "O", "X"],
	["O", "X", "X"],
	["X", "X", "O"],
]), "X")

Test.assert_equals(who_won([
	["X", "O", "X"],
	["O", "O", "O"],
	["X", "X", "O"],
]), "O")
Test.assert_equals(who_won([
	["O", "X", "X"],
	["O", "O", "X"],
	["O", "X", "O"],
]), "O")
