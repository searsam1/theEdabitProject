#
def prime(n):
	for i in range(2, n):
		if not n % i:
			return False
	return True 


def primal_strength(n):	
	n_minus, n_plus = n, n
	lower, upper = 1, 1
	n_minus -= 1
	n_plus += 1
	while not prime(n_minus):
		n_minus -= 1
		lower += 1
	while not prime(n_plus):
		n_plus += 1
		upper += 1
	return "Balanced" if lower == upper else ["Strong", "Weak"][lower < upper]
#

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(primal_strength(5), "Balanced")
Test.assert_equals(primal_strength(211), "Balanced")
Test.assert_equals(primal_strength(593), "Balanced")
Test.assert_equals(primal_strength(1693), "Strong")
Test.assert_equals(primal_strength(599), "Strong")
Test.assert_equals(primal_strength(2203), "Strong")
Test.assert_equals(primal_strength(19), "Weak")
Test.assert_equals(primal_strength(2971), "Weak")
Test.assert_equals(primal_strength(1493), "Weak")