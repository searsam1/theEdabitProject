from find_glasses import find_glasses
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(find_glasses(['phone', 'O-O', 'coins', 'keys']), 1)
Test.assert_equals(find_glasses(['OO', 'wallet', 'O##O', 'O----O']), 3)
Test.assert_equals(find_glasses(['O_O', 'O-O', 'OwO']), 1)
Test.assert_equals(find_glasses(['O--#--O', 'dustO---Odust', 'more dust']), 1)
Test.assert_equals(find_glasses(['floor', 'the floor again', 'pockets', 'bed', 'cabinet', 'the top of my head O-O']), 5)
Test.assert_equals(find_glasses(['OOOO----~OOO', '-------', 'OOOOOOO', 'OO-OO-OO-O']), 3)
