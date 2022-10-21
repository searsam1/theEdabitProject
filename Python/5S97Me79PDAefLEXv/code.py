
import re
def lambda_to_def(code):
    try:
        name, func = map(lambda x: x.strip(), re.split(r"= lambda", code, 2))
    except Exception as e:
        arr = list(map(lambda x: x.strip(), re.split(r"= lambda", code, 2)))
        name = arr[0]
        func = arr[1] + arr[2]
    params, res = map(lambda x: x.strip(),re.split(r":", func, 1))
    res = res
    print(params)
    print(name)
    return "def {1}({0}):\n\treturn {2}".format(params, name, res)
class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            



Test.assert_equals(
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