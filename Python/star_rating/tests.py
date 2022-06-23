from star_rating import star_rating
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(star_rating([55, 67, 98, 115, 61]), "[3.15] ***")
Test.assert_equals(star_rating([75, 79, 50, 55, 25]), "[2.56] ***")
Test.assert_equals(star_rating([0, 2, 0, 1, 23]), "[4.73] *****")
Test.assert_equals(star_rating([16, 17, 23, 40, 45]), "[3.57] ****")
Test.assert_equals(star_rating([175, 790, 550, 1550, 1245]), "[3.67] ****")
Test.assert_equals(star_rating([0, 0, 0, 0, 5]), "[5.00] *****")
Test.assert_equals(star_rating([6713, 7809, 5350, 5005, 6250]), "[2.88] ***")
Test.assert_equals(star_rating([80, 79, 82, 155, 325]), "[3.79] ****")
