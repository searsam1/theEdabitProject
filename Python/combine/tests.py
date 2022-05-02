from combine import combine
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")
		
from random import randrange as rand

# generate FSAs
def convert(base):
	fsa = {
		'S%s' % k: ['S%s' % ((2*k + n) % base)
		for n in [0, 1]] for k in range(base)
	}
	lst = [[[k, 0, fsa[k][0]], [k, 1, fsa[k][1]]] for k in fsa]
	return fsa, sum(lst, [])

# example tests
divisible = [
	['S0', 0, 'S0'], ['S0', 1, 'S1'],
  ['S1', 0, 'S2'], ['S1', 1, 'S0'],
  ['S2', 0, 'S1'], ['S2', 1, 'S2']
]
prod = {
  'S0': ['S0', 'S1'],
  'S1': ['S2', 'S0'],
  'S2': ['S1', 'S2']
}
Test.assert_equals(combine(divisible), prod, 'Example 1')

# random tests
for _ in range(12):
	n = rand(5, 20)
	Test.assert_equals(combine(convert(n)[1]), convert(n)[0])
