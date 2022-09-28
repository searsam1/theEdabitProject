
from re import T
import time

def highest_occurrence(lst):
	lst2 = set(i for i in lst if lst.count(i) == lst.count(max(lst, key=lst.count)))
	strings = sorted(i for i in lst2 if isinstance(i, str))
	ints = sorted(i for i in lst2 if isinstance(i, int))
	return ints + strings
	

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

t1 = time.perf_counter()

TestsConsoleTest.assert_equals(highest_occurrence(["a"]), ["a"])
Test.assert_equals(highest_occurrence(["a","a"]), ["a"])
Test.assert_equals(highest_occurrence(["a","a","b"]), ["a"])
Test.assert_equals(highest_occurrence(["a","a","b"]), ["a"])
Test.assert_equals(highest_occurrence(["a","a","b","b"]), ["a","b"])
Test.assert_equals(highest_occurrence([1,"a","b","b"]), ["b"])
Test.assert_equals(highest_occurrence([1,2,2,3,3,3,4,4,4,4]), [4])
Test.assert_equals(highest_occurrence(["ab","ab","b"]), ["ab"])
Test.assert_equals(highest_occurrence(["ab","ab","b","bb","b"]), ["ab","b"])
Test.assert_equals(highest_occurrence([3,3,3,4,4,4,4,2,3,6,7,6,7,6,7,6,"a","a","a","a"]), [3,4,6,"a"])
Test.assert_equals(highest_occurrence([2,2,"2","2",4,4]), [2,4,"2"])

t2 = time.perf_counter()

res = t2 - t1
print(res / 1e9)