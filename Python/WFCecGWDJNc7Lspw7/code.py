
from datetime import datetime as dt

def clock(time):
    t = dt.strptime(time, "%I:%M:%S")
    hh, mm, ss = t.hour, t.minute, t.second
    mm += ss / 60
    ss = 0    
    def hour_hand():
        deg_hh = hh * 30
        deg_mm = mm / 60 * 30
        return sum([deg_hh, deg_mm])

    def minute_hand():
        deg_mm = mm / 60 * 12 * 30
        return deg_mm

    x1, x2 = map(abs,[(minute_hand() - hour_hand()) - 360, (minute_hand() - hour_hand())])
    return round( min([x1,x2]), 3)

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(clock("12:00:00"), 0.0)
Test.assert_equals(clock("12:15:00"), 82.5)
Test.assert_equals(clock("12:32:44"), 179.967)
Test.assert_equals(clock("03:33:33"), 94.525)
Test.assert_equals(clock("01:59:59"), 60.092)


