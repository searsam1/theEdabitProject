def advanced_sort(lst):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(advanced_sort([1,2,1,2]) , [[1,1],[2,2]])
Test.assert_equals(advanced_sort([2,1,2,1]) , [[2,2],[1,1]])
Test.assert_equals(advanced_sort([3,2,1,3,2,1]) , [[3,3],[2,2],[1,1]])
Test.assert_equals(advanced_sort([5,5,4,3,4,4]) , [[5,5],[4,4,4],[3]])
Test.assert_equals(advanced_sort([80,80,4,60,60,3]),[[80,80],[4],[60,60],[3]])
Test.assert_equals(advanced_sort(['c','c','b','c','b',1,1]),[['c','c','c'],['b','b'],[1,1]])
Test.assert_equals(advanced_sort([1234, 1235, 1234, 1235, 1236, 1235]),[[1234, 1234],[1235, 1235, 1235],[1236]])
Test.assert_equals(advanced_sort(['1234', '1235', '1234', '1235', '1236', '1235']),[['1234', '1234'],['1235', '1235', '1235'],['1236']])