from evenOddTransform import evenOddTransform
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Describe(odd_even_transform)
{
	It(T1){Assert::That(evenOddTransform({3, 4, 9}, 3), Equals(std::vector<int>({9, -2, 15})));}
	It(T2){Assert::That(evenOddTransform({0, 0, 0}, 10), Equals(std::vector<int>({-20, -20, -20})));}
	It(T3){Assert::That(evenOddTransform({1, 2, 3}, 1), Equals(std::vector<int>({3, 0, 5})));}
	It(T4){Assert::That(evenOddTransform({55, 90, 830}, 2), Equals(std::vector<int>({59, 86, 826})));}
};
