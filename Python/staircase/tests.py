from staircase import staircase
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

num_vector = [3, 7, 2, -8, 4, -12, 11, -6]
res_vector = [
  "__#
_##
###",
  "______#
_____##
____###
___####
__#####
_######
#######",
  "_#
##",
  "########
_#######
__######
___#####
____####
_____###
______##
_______#",
  "___#
__##
_###
####",
  "############
_###########
__##########
___#########
____########
_____#######
______######
_______#####
________####
_________###
__________##
___________#",
  "__________#
_________##
________###
_______####
______#####
_____######
____#######
___########
__#########
_##########
###########",
  "######
_#####
__####
___###
____##
_____#"
]
for i, x in enumerate(num_vector): Test.assert_equals(staircase(x), res_vector[i])
