def recur_index(txt):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

from inspect import getsource
from re import findall, MULTILINE

def check_recursive(fn):
  try:
    src, n = getsource(fn), fn.__name__
    if n == '<lambda>': n = src.split('=')[0].strip()
    return len(findall(n, src, flags=MULTILINE)) > 1
  except OSError: return True

Test.assert_equals(check_recursive(recur_index), True)
Test.assert_not_equals(check_recursive(recur_index), False, 'Recursion is required!')

str_vectors, res_vectors = [
  'KDXTDATTDD', 'AKEDCBERSD', 'DXKETRETXD', 'ABCKPEPGBC', 'ABCDEFGHIJ', None, 'DXTDDTXD',
  'YXZETUVXWV', 'YZTQMNRTERXHQRX', 'YARDECBDER', '', 'ABCDEFGABCD', None, 'KLMNONMLK'], [
  {"D": [1, 4]}, {"E": [2, 6]}, {"E": [3, 6]}, {"P": [4, 6]}, {}, {}, {"D": [0, 3]},
  {"X": [1, 7]}, {"T": [2, 7]}, {"D": [3, 7]}, {}, {"A": [0, 7]}, {}, {"N": [3, 5]}
]

for i, s in enumerate(str_vectors):
  Test.assert_equals(recur_index(s), res_vectors[i])