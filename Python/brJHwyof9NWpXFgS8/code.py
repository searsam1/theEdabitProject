def bill_count(money, bills):
    bills, total = bills[::-1], 0
    for bill in bills:
        total += money // bill
        money %= bill
        if not money: return total
    return total

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(bill_count(100, [1, 10, 20]), 5)
Test.assert_equals(bill_count(1050, [1, 10, 20, 100]), 13)
Test.assert_equals(bill_count(3, [1, 10]), 3)
Test.assert_equals(bill_count(555, [1, 10, 100]), 15)
Test.assert_equals(bill_count(222, [1, 10, 100]), 6)
Test.assert_equals(bill_count(60, [1, 10, 20]), 3)
Test.assert_equals(bill_count(55, [1, 5, 10, 50]), 2)