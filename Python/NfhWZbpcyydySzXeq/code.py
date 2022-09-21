def lunar_sum(n1, n2):
	n1, n2 = map(str, [n1, n2])
	mx = max(len(n1), len(n2))
	n1, n2 = n1.rjust(mx, "0"), n2.rjust(mx, "0")
	res = int("".join(max(i,j) for i,j in zip(n1, n2)))
	return res

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(lunar_sum(246, 317), 347)
Test.assert_equals(lunar_sum(134, 54), 154)
Test.assert_equals(lunar_sum(20, 140), 140)
Test.assert_equals(lunar_sum(1, 1), 1)
Test.assert_equals(lunar_sum(198, 44), 198)
Test.assert_equals(lunar_sum(36602, 696), 36696)
Test.assert_equals(lunar_sum(91, 8823), 8893)
Test.assert_equals(lunar_sum(123, 8), 128)
Test.assert_equals(lunar_sum(2289, 98211285), 98212289)
Test.assert_equals(lunar_sum(9, 11), 19)
Test.assert_equals(lunar_sum(11, 22), 22)