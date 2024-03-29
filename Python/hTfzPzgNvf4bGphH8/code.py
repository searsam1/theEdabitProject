

class Multiply:

    def __init__(self, lst) -> None:
        self.lst = lst
    
    def get_mult_sum(self):
        total = 1
        for i in self.lst:
            total *= i
        return total

m = Multiply([1, 2, 3, -4])
print(m.get_mult_sum())


from datetime import datetime
def convert_time(txt):
    t = datetime.strptime(txt, "%I:%M:%S%p")
    res = datetime.strftime(t, "%H:%M:%S")
    return res

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(convert_time("07:05:45PM"), "19:05:45")
Test.assert_equals(convert_time("12:40:22AM"), "00:40:22")
Test.assert_equals(convert_time("12:45:54PM"), "12:45:54")
Test.assert_equals(convert_time("05:32:33PM"), "17:32:33")
Test.assert_equals(convert_time("11:59:59PM"), "23:59:59")
Test.assert_equals(convert_time("11:59:59AM"), "11:59:59")
Test.assert_equals(convert_time("06:00:19AM"), "06:00:19")