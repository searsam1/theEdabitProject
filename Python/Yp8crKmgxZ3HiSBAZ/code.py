


def freq_count(lst, el):
    res = [] 

    for i in lst:
        if isinstance(i, list):
            res.append( *freq_count(i, el) )
        else:
            res.append(i)
    return res
			
			
class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

# TestsConsoleTest.assert_equals(freq_count([1, 1, 1, 1], 1), [[0, 4]])
# Test.assert_equals(freq_count([1, 1, 2, 2], 1), [[0, 2]])
# Test.assert_equals(freq_count([1, 1, 2, [1]], 1), [[0, 2], [1, 1]])
Test.assert_equals(freq_count([1, 1, 2, [[1]]], 1), [[0, 2], [1, 0], [2, 1]])
# Test.assert_equals(freq_count([[[1]]], 1), [[0, 0], [1, 0], [2, 1]])
Test.assert_equals(freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1), [[0, 1], [1, 2], [2, 3]])
Test.assert_equals(freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5), [[0, 3], [1, 4], [2, 0]])
Test.assert_equals(freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2), [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]])