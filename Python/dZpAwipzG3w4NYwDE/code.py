def highest_pair(cards):
	

TestsConsoleTest.assert_equals(highest_pair(['A', 'A', 'K', 'K', '3']), [True, 'A'])

Test.assert_equals(highest_pair(['A', 'K', 'Q', 'J', '10']), False)

Test.assert_equals(highest_pair(['A', 'K', 'K', 'K', 'Q']), [True, 'K'])

Test.assert_equals(highest_pair(['A', '3', '3', '4', '4']), [True, '4'])

Test.assert_equals(highest_pair(['A', 'K', 'Q', 'Q', '5']), [True, 'Q'])