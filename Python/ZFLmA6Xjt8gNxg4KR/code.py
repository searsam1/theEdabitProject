def sum_consecutives(lst):    
    res = [] 
    for i in range(len(lst)):
        target = lst[i]
        total = target
        for j in range(len(lst)):
            if i == j:
                pass
            else:
                if lst[j] == target:
                    total += target
        try:
            if res[-1] != total:
                res.append(total)
        except Exception:
            if not res:
                res.append(total)
    return res





            
    

        
        

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(sum_consecutives([0, 7, 7, 7, 5, 4, 9, 9, 0]), [0, 21, 5, 4, 18, 0])
Test.assert_equals(sum_consecutives([4, 4, 5, 6, 8, 8, 8]), [8, 5, 6, 24])
Test.assert_equals(sum_consecutives([-5, -5, 7, 7, 12, 0]), [-10, 14, 12, 0])
Test.assert_equals(sum_consecutives([2, 2, 2, 2, 2, 7]), [10, 7])
Test.assert_equals(sum_consecutives([2, 2, -4, 4, 5, 5, 6, 6, 6, 6, 6, 1]), [4, -4, 4, 10, 30, 1])
Test.assert_equals(sum_consecutives([3, 3, 3, 3, 1]), [12, 1])
Test.assert_equals(sum_consecutives([1, -1, -2, 2, 3, -3, 4, -4]), [1, -1, -2, 2, 3, -3, 4, -4])