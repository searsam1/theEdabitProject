from tic_tac_toe import tic_tac_toe
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(tic_tac_toe(
 [["X", "O", "O"],
  ["O", "X", "O"],
  ["O", "#", "X"]]), "Player 1 wins")	

Test.assert_equals(tic_tac_toe(
 [["X", "O", "O"],
  ["O", "X", "O"],
  ["O", "#", "O"]]), "Player 2 wins")

Test.assert_equals(tic_tac_toe(
 [["X", "O", "O"],
  ["O", "X", "O"],
  ["O", "O", "#"]]), "It's a Tie")

Test.assert_equals(tic_tac_toe(
 [["X", "O", "O"],
  ["X", "X", "O"],
  ["X", "O", "#"]]), "Player 1 wins")

Test.assert_equals(tic_tac_toe(
 [["X", "#", "O"],
  ["X", "X", "O"],
  ["#", "O", "#"]]), "It's a Tie")

Test.assert_equals(tic_tac_toe(
 [["X", "X", "X"],
  ["X", "O", "O"],
  ["O", "O", "X"]]), "Player 1 wins")

Test.assert_equals(tic_tac_toe(
 [["X", "O", "O"],
  ["X", "O", "O"],
  ["O", "X", "X"]]), "Player 2 wins")

Test.assert_equals(tic_tac_toe(
 [["X", "O", "O"],
  ["X", "O", "O"],
  ["#", "X", "X"]]), "It's a Tie")

Test.assert_equals(tic_tac_toe(
 [["X", "O", "O"],
  ["O", "O", "O"],
  ["#", "X", "X"]]), "Player 2 wins")
