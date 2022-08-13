def ry_seq(n, s):
	

TestsConsoleTest.assert_equals(ry_seq(2, "all"), 5)

Test.assert_equals(ry_seq(1, "yellow"), 0)

Test.assert_equals(ry_seq(1, "blue"), False)

Test.assert_equals(ry_seq(28, "red"), 55)

Test.assert_equals(ry_seq(6, "all"), 61)

Test.assert_equals(ry_seq(3), False)

Test.assert_equals(ry_seq(0, "all"), 0)

Test.assert_equals(ry_seq(22, "all"), 925)

Test.assert_equals(ry_seq(28, "yellow"), 1458)

Test.assert_equals(ry_seq(23, "red"), 45)

Test.assert_equals(ry_seq(150, "all"), 44701)

Test.assert_equals(ry_seq(30, "yellow"), 1682)

Test.assert_equals(ry_seq(1000, "red"), 1999)

Test.assert_equals(ry_seq(28, "green"), False)