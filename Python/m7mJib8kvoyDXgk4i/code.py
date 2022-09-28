

def max_sum(nums):
	
    sums = [] 
    res = [] 
    for n in nums:
        res.append(n)
        if sum(res) < 0:
            sums.append(res)
            res = [] 
    
    sums.append(res)

    lst = [] 
    for res in sums:
        r = []
        for idx,i in enumerate(res):
            if idx == 0 or idx == len(res) - 1:
                if i > 0:
                    r.append(i)
            else:
                r.append(i)
        lst.append(r)
    return sum(max(lst, key=sum))
            
                

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(max_sum((3, -10, 4, -1, 2, 3, 6, -7)), 14)
Test.assert_equals(max_sum((1, -9, 0, -8, 76, 5, 43)), 124)
Test.assert_equals(max_sum([-1, -9, 0, -8, 76, 5, 43]), 124)
Test.assert_equals(max_sum([10, -9, 0, -8, 76, 5, -40, 43]), 84)
Test.assert_equals(max_sum([10, -9, 0, 8, 3, -1, -4, 6]), 13)
Test.assert_equals(max_sum([-1, -9, 0, 8, -76, 5, 3]), 8)
Test.assert_equals(max_sum([-1, -9, -4, -8, -1, -2]), 0)