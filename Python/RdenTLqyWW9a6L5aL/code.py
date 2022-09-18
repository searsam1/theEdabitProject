def is_harshad(n):
	# recursive code here...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsolefrom inspect import getsource
from re import findall, MULTILINE

def check_recursive(fn):
  try:
    src, n = getsource(fn), fn.__name__
    if n == '<lambda>': n = src.split('=')[0].strip()
    return len(findall(n, src, flags=MULTILINE)) > 1
  except OSError: return True

Test.assert_not_equals(check_recursive(is_harshad), False, 'Recursion is required!')

num_vector, res_vector = [
  [75, 171, 481, 89, 516, 200, 209, 12345, 53, 27],
  [False, True, True, False, True, True, True, True, False, True]
]
for i, n in enumerate(num_vector): Test.assert_equals(is_harshad(n), res_vector[i])