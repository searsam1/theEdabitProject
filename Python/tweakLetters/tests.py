from tweakLetters import tweakLetters
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Describe(tweaking_letters_tests)
{
	It(test1){Assert::That(tweakLetters("apple", {0, 1, -1, 0, -1}), Equals("aqold"));}
	It(test2){Assert::That(tweakLetters("many", {0, 0, 0, -1}), Equals("manx"));}
	It(test3){Assert::That(tweakLetters("rhino", {1, 1, 1, 1, 1}), Equals("sijop"));}
	It(should_work_for_modulo_cases_1){Assert::That(tweakLetters("xyz", {1, 1, 1}), Equals("yza"));}
	It(should_work_for_modulo_cases_2){Assert::That(tweakLetters("abc", {-1, -1, -1}), Equals("zab"));} 
};
