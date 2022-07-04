def prime_pair_list(num):
	

TestsConsoleTest.assert_equals(prime_pair_list(10), ["3+7", "5+5"])

Test.assert_equals(prime_pair_list(20), ["3+17", "7+13"])

Test.assert_equals(prime_pair_list(30), ["7+23", "11+19", "13+17"])

Test.assert_equals(prime_pair_list(50), ["3+47", "7+43", "13+37", "19+31"])

Test.assert_equals(prime_pair_list(80), ["7+73", "13+67", "19+61", "37+43"])

Test.assert_equals(prime_pair_list(100), ["3+97", "11+89", "17+83", "29+71", "41+59", "47+53"])