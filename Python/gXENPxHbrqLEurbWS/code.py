import math

def gcf(n):
    for i in range(math.ceil(n**.5) + 1, 0, -1):
        if n % i == 0:
            return i if i != 1 else n


def prime(n):
    for i in range(2,math.ceil(n**.5) + 1):
        if n % i == 0:
            return False
    return True


def facts(n):
    res = [] 
    for i in range(2,math.ceil(n**.5) + 1):
        if n % i == 0:
            res.append(i)
            res.append(n//i)
    
    while any(not prime(i) for i in res):
        
        for fact in res:
            if not

            
    

print(facts(100))


def factorize(n):
    ...



class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

Test.assert_equals(factorize(9870), [(2, 1), (3, 1), (5, 1), (7, 1), (47, 1)])
Test.assert_equals(factorize(  60), [(2, 2), (3, 1), (5, 1)])

# TestsConsoleTest.assert_equals(factorize(   2), [(2, 1)])
# Test.assert_equals(factorize(   4), [(2, 2)])
# Test.assert_equals(factorize(  10), [(2, 1), (5, 1)])
# Test.assert_equals(factorize(  11), [(11, 1)])
# Test.assert_equals(factorize(  29), [(29, 1)])

# Test.assert_equals(factorize( 100), [(2, 2), (5, 2)])
# Test.assert_equals(factorize( 151), [(151, 1)])
# Test.assert_equals(factorize( 323), [(17, 1), (19, 1)])
# Test.assert_equals(factorize( 997), [(997, 1)])
# Test.assert_equals(factorize(3349), [(17, 1), (197, 1)])
# Test.assert_equals(factorize(5040), [(2, 4), (3, 2), (5, 1), (7, 1)])
# Test.assert_equals(factorize(6097), [(7, 1), (13, 1), (67, 1)])
# Test.assert_equals(factorize(8192), [(2, 13)])

# Test.assert_equals(factorize(9973), [(9973, 1)])
# Test.assert_equals(factorize(9999), [(3, 2), (11, 1), (101, 1)])