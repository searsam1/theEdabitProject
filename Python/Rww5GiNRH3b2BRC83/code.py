def data_regex_lovely(txt):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(data_regex_lovely("desc=dzgr&val=xyz54&time=01:41&id=1"), {'desc':"dzgr",'val':"xyz54",'time':"01:41",'id':1})
Test.assert_equals(data_regex_lovely("time=01:41&id=1&desc=dzgr&val=12345"), {'desc':"dzgr",'val':"12345",'time':"01:41",'id':1})
Test.assert_equals(data_regex_lovely("time=11:41&id=10&desc=dzgraa&val=54"), {'desc':"dzgraa",'val':"54",'time':"11:41",'id':10})