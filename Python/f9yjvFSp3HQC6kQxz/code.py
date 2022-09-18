
def semi(n):
    total = 1
    while n > 0:
        total *= n
        n -= 2
    return total

def fact(n):
    total = 1
    neg = None
    if n < 0:
        n *= -1
        neg = True
    while n > 0:
        total *= n
        n -= 1
    return total * -1 if neg else total


def alt(n):
    total = 0
    while n != 0:
        total += fact(n)
        if n < 0:
            n += 1
        else:
            n -= 1
        n *= -1
    return total

def alt_semi(n):
	return alt(n) - semi(n)

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(alt_semi(1), 0)
Test.assert_equals(alt_semi(3), 2)
Test.assert_equals(alt_semi(4), 11)
Test.assert_equals(alt_semi(6), 571)
Test.assert_equals(alt_semi(9), 326036)
Test.assert_equals(alt_semi(16), 19696498855099)
Test.assert_equals(alt_semi(21), 48773618867405512406)