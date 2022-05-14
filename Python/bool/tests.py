from bool import bool
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Describe(tests) {
  It(test1){Assert::That(is_curzon(5), Equals(true));}
	It(test2){Assert::That(is_curzon(10), Equals(false));}
	It(test3){Assert::That(is_curzon(14), Equals(true));}
	It(test4){Assert::That(is_curzon(7), Equals(false));}
	It(test5){Assert::That(is_curzon(20), Equals(false));}
	It(test6){Assert::That(is_curzon(1), Equals(true));}
};
