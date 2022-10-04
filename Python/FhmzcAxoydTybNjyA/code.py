def carry_digits(n1, n2):
    
    n1, n2 = str(n1)[::-1], str(n2)[::-1]

    mx = max([n1, n2])
    carry = 0 
    count = 0 
    new_n = ""
    for i in range(len(mx)):
        try:
            c1 = int(n1[i])
        except IndexError:
            c1 = 0
        try:
            c2 = int(n2[i])
        except IndexError:
            c2 = 0
        res = c1 + c2

        if carry:
            res += carry 
            carry = 0 

        if res >= 10:
            carry = int(str(res)[0])
            count += 1
            res = int(str(res)[1])
        
        new_n += str(res)
    new_n += str(res)
    new_n = int(new_n[::-1])
    return count


class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(carry_digits(36, 135), 1)
Test.assert_equals(carry_digits(671, 329), 3)
Test.assert_equals(carry_digits(1111, 3333), 0)
Test.assert_equals(carry_digits(4, 5268), 1)
Test.assert_equals(carry_digits(53214, 16905), 2)
Test.assert_equals(carry_digits(53214, 56905), 3)
Test.assert_equals(carry_digits(515, 4), 0)
Test.assert_equals(carry_digits(515, 90), 1)
Test.assert_equals(carry_digits(63223, 70000), 1)