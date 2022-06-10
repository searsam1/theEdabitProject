from pad_matrix import pad_matrix
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(pad_matrix([[]]), [[0,0],[0,0],[0,0]], 'Check empty case.')
Test.assert_equals(pad_matrix([['hi'],['downstairs']]), [[0,0,0],[0,'hi',0],[0,'downstairs',0],[0,0,0]])
Test.assert_equals(pad_matrix([[1,'beep',True],['oink',99,1.1],[[1,1],'e',99]]), [[0,0,0,0,0],[0,1,'beep',True,0],[0,'oink',99,1.1,0],[0,[1,1],'e',99,0],[0,0,0,0,0]])
for i in range(4):
	Test.assert_equals(pad_matrix([[i**2]]), [[0,0,0],[0,i**2,0],[0,0,0]])
	Test.assert_equals(pad_matrix([[i,i**3]]), [[0,0,0,0],[0,i,i**3,0],[0,0,0,0]])
