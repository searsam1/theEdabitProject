def elapsed_time(sa, st):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(elapsed_time("11:00:00", "12:00:00"), "01:00:00") 
Test.assert_equals(elapsed_time("13:01:43", "21:41:57"), "08:40:14")
Test.assert_equals(elapsed_time("17:34:43", "17:34:42"), "23:59:59") 
Test.assert_equals(elapsed_time("15:01:27", "02:51:33"), "11:50:06") 
Test.assert_equals(elapsed_time("00:00:01", "17:34:42"), "17:34:41") 
Test.assert_equals(elapsed_time("07:59:59", "08:00:00"), "00:00:01") 
Test.assert_equals(elapsed_time("23:59:59", "00:00:00"), "00:00:01") 
Test.assert_equals(elapsed_time("15:00:00", "15:01:00"), "00:01:00") 
Test.assert_equals(elapsed_time("06:12:27", "10:34:13"), "04:21:46") 
Test.assert_equals(elapsed_time("03:22:44", "18:04:11"), "14:41:27")