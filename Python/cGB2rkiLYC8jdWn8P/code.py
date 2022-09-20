def battle_outcome(num):...

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