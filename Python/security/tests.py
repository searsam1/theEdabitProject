from security import security
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(security("xxTxxx$xxxTxxxGxxT"), "ALARM!")
Test.assert_equals(security("xGxx$xxGxxxTTT"), "Safe")
Test.assert_equals(security("TxGxx$xxx$xxxGxxT"), "Safe")
Test.assert_equals(security("GxxxTxxGxxTxx$xx$xxTxxG"), "ALARM!")
Test.assert_equals(security("xxGTxx$xx$xxxxxxG"), "ALARM!")
Test.assert_equals(security("xxTxxxxxxxx$xGxxxxxxT"), "ALARM!")

