param = ""...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleimport random

def search(txt):
	return {'Error': 'No products found.'}

for _ in range(14):
	users = {
		'user %s' % k: 'password' + str(random.randrange(10, 100))
		for k in range(5)
	}
	res = eval('search("%s")' % param)
	Test.assert_equals(res, users)