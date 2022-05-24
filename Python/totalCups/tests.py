from totalCups import totalCups
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Describe(tests)
{
  It(test1){Assert::That(totalCups(6), Equals(7));}
	It(test2){Assert::That(totalCups(3), Equals(3));}
	It(test3){Assert::That(totalCups(7), Equals(8));}
	It(test4){Assert::That(totalCups(12), Equals(14));}
	It(test5){Assert::That(totalCups(213), Equals(248));}
	It(test6){Assert::That(totalCups(16), Equals(18));}
};
