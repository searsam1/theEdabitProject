def license(me, agents, others):
    all_p = sorted((me + " " + others).split())
    groups = [all_p[i:i+agents] for i in range(0, len(all_p), agents)]
    idx = [i for i in groups if me in i]
    return (groups.index(idx[0]) + 1) * 20

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(license("Zebediah", 1, "Bob Jim Becky Pat"), 100)
Test.assert_equals(license("Eric", 2, "Adam Caroline Rebecca Frank"), 40)
Test.assert_equals(license("Aaron", 3, "Jane Max Olivia Sam"), 20)
Test.assert_equals(license("Zebediah", 4, "Bob Jim Becky Pat"), 40)
Test.assert_equals(license("Zebediah", 5, "Bob Jim Becky Pat"), 20)