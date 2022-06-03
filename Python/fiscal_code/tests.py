from fiscal_code import fiscal_code
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(fiscal_code("MRTMTT25D09F205"), "Z")
Test.assert_equals(fiscal_code("BTTRSE85M20C351"), "V")
Test.assert_equals(fiscal_code("MLLSNT82P65Z404"), "U")
Test.assert_equals(fiscal_code("CPNLAX99A17H501"), "O")
Test.assert_equals(fiscal_code("CRUMRA67S47F704"), "O")
Test.assert_equals(fiscal_code("MSOMKY28A16B230"), "V")
Test.assert_equals(fiscal_code("YUXHLN50T41E999"), "X")
Test.assert_equals(fiscal_code("CHEBND61T01Z799"), "R")
