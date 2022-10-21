def is_consecutive(s):
	# recursive code in here...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsolefrom inspect import getsource
from re import findall, MULTILINE as M

def is_recursive(src):
	try:
		n = getsource(src).split("=")[0].strip() if src.__name__ == "<lambda>" else src.__name__
		return len(findall(n, getsource(src), flags=M)) > 1
	except OSError: return True

Test.assert_not_equals(is_recursive(is_consecutive), False, 'Recursion is required!')

actual_param = [
  "121314151617", "123124125", "667666", "23242526", "444445", "1234567", "123412351236",
  "57585960616263", "500001500002500003", "919920921", "12341235123612371238", "326325324323",
  "54321", "56555453", "32332432536", "2324256", "1235", "121316", "12131213", "90090190290",
  "35236237238", "999897959493", "171615141312119", "1716171819181920", "273274273274"
]
expected = [
  True, True, True, True, True, True, True, True, True, True, True, True, True, True,
  False, False, False, False, False, False, False, False, False, False, False
]
for i, z in enumerate(actual_param): Test.assert_equals(is_consecutive(z), expected[i])