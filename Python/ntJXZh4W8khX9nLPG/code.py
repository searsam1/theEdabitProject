def count(n):
	# your recursive solution in here...

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

Test.assert_not_equals(check_recursive(count), False, 'Recursion is required!')

num_vector, res_vector = [
  [0, 318, -92563, 4666, -314890, 654321, 638476, 12345, 1289396, -1232323, 12839393, -231273683],
  [1, 3, 5, 4, 6, 6, 6, 5, 7, 7, 8, 9]
]
for i, n in enumerate(num_vector): Test.assert_equals(count(n), res_vector[i])