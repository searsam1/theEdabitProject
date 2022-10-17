def lambda_to_def(code):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(
    lambda_to_def("func = lambda a, b: a * (b - 2)"),
    "def func(a, b):\n\treturn a * (b - 2)"
)

Test.assert_equals(
    lambda_to_def("func = lambda w: w + 'lambda'"),
    "def func(w):\n\treturn w + 'lambda'"
)

Test.assert_equals(
    lambda_to_def("a = lambda x, y=2: x**y"),
    "def a(x, y=2):\n\treturn x**y"
)

Test.assert_equals(
    lambda_to_def("z = lambda lambdadef: lambdadef.split(':')"),
    "def z(lambdadef):\n\treturn lambdadef.split(':')"
)

Test.assert_equals(
    lambda_to_def("t = lambda s='t = lambda s: s + 1': s + 's'"),
    "def t(s='t = lambda s: s + 1'):\n\treturn s + 's'"
)