from exit_maze import exit_maze
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

maze = [
	[1,1,1,1,1,1,1,1,0,1],
	[1,3,1,0,1,0,0,0,0,1],
	[1,0,1,0,0,0,1,1,0,1],
	[1,0,1,1,1,1,1,0,0,1],
	[1,0,1,0,0,0,0,0,0,1],
	[1,0,1,0,1,0,1,0,0,1],
	[1,0,1,0,1,0,0,0,0,0],
	[1,0,1,0,1,0,1,1,0,1],
	[1,0,0,0,1,0,0,0,0,1],
	[1,1,1,0,1,1,1,1,2,1]
]

Test.assert_equals(exit_maze(maze,["N","N","N","W","W","W","N","N","W","W","S","S","S","S","W","W","N","N","N","N","N","N","N"]), "Finish")
Test.assert_equals(exit_maze(maze,["N","N","N","N","N","N","N","N","W","W","W","S","W","W","N"]), "Lost")
Test.assert_equals(exit_maze(maze,["N","N","N","N","N","E","E","S","S","S","S","S","S"]), "Dead")
Test.assert_equals(exit_maze(maze,["N","W","W","W","W"]), "Dead")
Test.assert_equals(exit_maze(maze,["N","N","N","N","N","N","N","N","N","S","S","S","S","S","S","S","S","S"]), "Lost")
Test.assert_equals(exit_maze(maze,["N","E","E"]), "Dead")
Test.assert_equals(exit_maze(maze,["N","W","W","W","N","N","N","N","W","W","S","S","S","S","W","W","N","N","N","N","N","N","N","S","S"]), "Finish")
Test.assert_equals(exit_maze(maze,["N","W","W","W","N","N"]), "Lost")
Test.assert_equals(exit_maze(maze,["N","N","N","E"]), "Lost")
Test.assert_equals(exit_maze(maze,["N","N","N","W","W","W","N","N","W","W","S","S","S","S","S","S"]), "Dead")
Test.assert_equals(exit_maze(maze,["N","W","W","W","N","N","N","N","W","W","S","S","S","S","W","W","N","N","N","N","N","N","N"]), "Finish")
