
from functools import reduce
import re

def battle_outcome(num): 
    
    n = str(num)
    p = r"\d\d|\d"
    prog = re.compile(p)
    prog = prog.findall(n)
    res = [] 
    for i in prog:
        if len(i) == 1:
            res.append(i)
        elif i[0] != i[1]:
            res.append(max([i[0], i[1]]))
    return int("".join(res))


    


class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(battle_outcome(32531), 351)
Test.assert_equals(battle_outcome(111), 1)
Test.assert_equals(battle_outcome(5289), 59)
Test.assert_equals(battle_outcome(76811), 781)
Test.assert_equals(battle_outcome(3245196), 3596)
Test.assert_equals(battle_outcome(93552129), 929)