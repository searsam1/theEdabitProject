from find_longest import find_longest
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

actual_param, expected_param = [
  "Hello darkness my old friend.", "Yourself is your soul's captain and fate's master.",
  "The pretty daughter's toy, a doll, is as pretty as her.",
  "A thing of beauty is a joy forever.", "Forgetfulness is by all means powerless!",
  "Strengths is the longest and most commonly used word that contains only a single vowel."
], [
  "darkness", "yourself", "daughter", "forever", "forgetfulness", "strengths"
]
for i, s in enumerate(actual_param): Test.assert_equals(find_longest(s), expected_param[i])
