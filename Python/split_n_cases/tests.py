from split_n_cases import split_n_cases
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(split_n_cases("Unscrupulous", 2), [ "Unscru", "pulous" ])
Test.assert_equals(split_n_cases("Incomprehensible", 4), [ "Inco", "mpre", "hens", "ible" ])
Test.assert_equals(split_n_cases("Evaluation", 10), [ "E", "v", "a", "l", "u", "a", "t", "i", "o", "n" ])
Test.assert_equals(split_n_cases("Strengthened", 6), [ "St", "re", "ng", "th", "en", "ed" ])
Test.assert_equals(split_n_cases("Fool's Errand", 20), [ "Error" ])
Test.assert_equals(split_n_cases("Flavorless", 1), [ "Flavorless" ])
Test.assert_equals(split_n_cases("Evolutionary Biology", 8), [ "Error" ])
Test.assert_equals(split_n_cases("Indefatigable Defender", 2), [ "Indefatigab", "le Defender" ])
Test.assert_equals(split_n_cases("Unimaginatively", 3), [ "Unima", "ginat", "ively" ])
Test.assert_equals(split_n_cases("Peppered Moth", 6), [ "Error" ])
Test.assert_equals(split_n_cases("Peppered Moth", 6013), [ "Error" ])
