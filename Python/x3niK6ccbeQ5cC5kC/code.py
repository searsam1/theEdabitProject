def elapsed(t1, t2):
    s  = t2 - t1
    days = s // 86400
    hours = s % 86400 // 3600 
    mins = s % 86400 % 3600 // 60
    seconds = s % 86400 % 3600 % 60
    
    def f(time, mode):
        if time:
            if time > 1:
                time = "{} {}s".format(time, mode)
            elif time == 1:
                time = "{} {}".format(time, mode)
        return time if time else None

    days = f(days, "day")
    hours = f(hours, "hour")
    mins = f(mins, 'minute')
    seconds = f(seconds, 'second')
    
    res = ", ".join(i for i in [days, hours, mins, seconds] if i)
    return res

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(elapsed(1559813526, 1559899926), "1 day")
Test.assert_equals(elapsed(1559681004, 1559899926), "2 days, 12 hours, 48 minutes, 42 seconds")
Test.assert_equals(elapsed(1557641659, 1559899926), "26 days, 3 hours, 17 minutes, 47 seconds")
Test.assert_equals(elapsed(1557652446, 1559899926), "26 days, 18 minutes")
Test.assert_equals(elapsed(1558773066, 1559899926), "13 days, 1 hour, 1 minute")
Test.assert_equals(elapsed(1552513985, 1559899926), "85 days, 11 hours, 39 minutes, 1 second")