from flatten import flatten
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

from inspect import getsource
from re import findall, MULTILINE

def check_recursive(fn):
  try:
    src, n = getsource(fn), fn.__name__
    if n == '<lambda>': n = src.split('=')[0].strip()
    return len(findall(n, src, flags=MULTILINE)) > 1
  except OSError: return True

for v in [True, False]:
  if v: Test.assert_equals(check_recursive(flatten), v)
  else: Test.assert_not_equals(check_recursive(flatten), v, 'Recursion is required!')

arr_vectors = [
  [[[[[['direction'], [372], ['one'], [[[[[['Era']]]], 'Sruth', 3337]]], 'First']]]],
  [[4666], [5394], [466], [[['Saskia', [[[[['DXTD']], 'Lexi']]]]]]],
  [[696], ['friend'], ['power'], [[[['Marcus']]]], ['philus']],
  [[['deep'], [[['ocean']]], [['Marge']], ['rase', 876]]],
  ['I', [19.79, 'love', [12.17], "edabit"]], 
  [['The', ['first', ['of', ["May", 0.0, 1, ]]], 2, 3, 4]],
  [7, [11, 'lived', [[229]]]], 
  ['and', 6, [3, 'scores', ['six', 100]]]]
res_vectors = [
  ['direction', 372, 'one', 'Era', 'Sruth', 3337, 'First'],
  [4666, 5394, 466, 'Saskia', 'DXTD', 'Lexi'],
  [696, 'friend', 'power', 'Marcus', 'philus'],
  ['deep', 'ocean', 'Marge', 'rase', 876],
  ['I', 19.79, 'love', 12.17, 'edabit'],
  ['The', 'first', 'of', 'May', 0.0, 1, 2, 3, 4],
  [7, 11, 'lived', 229],
  ['and', 6, 3, 'scores', 'six', 100]
]

for i, r in enumerate(arr_vectors):
  Test.assert_equals(flatten(r), res_vectors[i])
