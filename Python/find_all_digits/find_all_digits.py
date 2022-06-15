# Alec Sears

import unittest
class Test(unittest.TestCase):
	def assert_equals(a,b,message=None):
		assert a == b

def find_all_digits(nums):
	"""
	* input:
		  [3129, 7689, 7449, 4389, 5855, 9670, 9245, 1291, 7367, 1810]
		  <list <int <length: 4>>
	*
	*Return the list element (3129, 7689, etc.) that contains the 
		last digit to all 10 digits. 
	*
	* e.g. 3.1.2.9.7.6.8.<already have 9>.<already have 7>...
		and that gives 9670 [idx 5]
	*
	* From: "https://edabit.com/challenge/rPnq2ugsM7zsWr3Pf"
	* By: tAF9Gf6PiGogbZuWs (zatoichi49)
	* "
	Taking each four digit number of a list in turn, 
		return the number that you are on when all of the digits 0-9
	 	have been discovered. If not all of the digits can be found, 
	 	return "Missing digits!".
	 	"("https://edabit.com/challenge/rPnq2ugsM7zsWr3Pf")
	"""

	res = list(map(str, nums))
	collection = [] 
	for idx,pair in enumerate(res):
		for digit in pair:
			if not digit in collection:
				collection.append(digit)
				if len(collection) == 10:
					return nums[idx]
	return "Missing digits!"

def run_tests():
	Test.assert_equals(find_all_digits([3129, 7689, 7449, 4389, 5855, 9670, 9245, 1291, 7367, 1810]), 9670)
	Test.assert_equals(find_all_digits([2758, 3737, 3349, 5118, 7004, 6106, 8868, 6687, 2510, 8911]), 6106)
	Test.assert_equals(find_all_digits([5343, 6743, 2922, 2423, 7050, 5116, 3992, 2707, 2435, 5251]), "Missing digits!")
	Test.assert_equals(find_all_digits([4169, 4511, 1498, 6945, 7959, 2666, 7872, 3217, 5408, 8662]), 5408)
	Test.assert_equals(find_all_digits([7985, 7130, 4625, 7392, 4933, 7163, 7130, 2145, 1596, 6188]), 4625)
	Test.assert_equals(find_all_digits([4823, 1049, 9555, 9466, 2191, 9316, 1105, 4489, 8318, 7081]), 7081)
	Test.assert_equals(find_all_digits([9827, 4405, 6317, 6086, 8091, 7800, 8365, 2544, 3402, 7248]), 6317)
	Test.assert_equals(find_all_digits([2227, 7262, 9322, 8967, 4807, 8708, 3317, 6543, 9522, 7106]), 6543)
	Test.assert_equals(find_all_digits([8452, 7326, 6786, 1893, 6546, 8714, 6699, 1361, 4891, 9797]), "Missing digits!")
	Test.assert_equals(find_all_digits([2627, 1146, 3964, 6280, 9759, 6188, 8917, 9375, 4012, 4217]), 9759)
	Test.assert_equals(find_all_digits([1291, 6903, 5887, 8914, 3906, 1465, 8452, 4909, 4143, 6921]), 8914)
	Test.assert_equals(find_all_digits([7433, 8245, 9603, 1446, 8158, 8756, 5066, 4996, 5233, 2856]), 1446)
	Test.assert_equals(find_all_digits([4661, 1207, 8411, 2010, 2092, 2441, 7885, 3810, 7433, 2034]), 3810)
	Test.assert_equals(find_all_digits([9429, 6519, 3795, 7924, 3042, 3425, 1371, 7194, 7680, 9007]), 7680)
	Test.assert_equals(find_all_digits([6621, 9480, 8239, 4542, 9772, 5108, 6872, 5057, 9477, 3602]), 9772)
	Test.assert_equals(find_all_digits([9701, 3828, 7183, 2727, 5212, 6721, 5413, 2351, 4237, 8207]), 5413)
	Test.assert_equals(find_all_digits([3914, 9923, 8187, 1657, 4271, 9538, 3759, 4543, 3438, 1943]), "Missing digits!")
	Test.assert_equals(find_all_digits([6572, 3752, 9661, 7017, 8139, 2596, 3054, 2730, 1350, 2483]), 3054)
	Test.assert_equals(find_all_digits([2102, 4519, 4229, 8347, 2019, 7342, 7181, 8977, 1339, 9988]), "Missing digits!")
	Test.assert_equals(find_all_digits([4467, 2849, 5706, 7330, 9488, 2529, 8837, 2256, 3975, 7311]), 7311)
	print("Pass")

if __name__ == '__main__':
	run_tests()

# Alec Sears	