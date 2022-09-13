
class Test:
    def assert_equals(a,b,message=None):
        assert a == b
        print("Test Passed.")


def highest_pair(cards):
	c = set(i for i in cards if cards.count(i) >= 2)
	
	if "A" in c:
		return [True, "A"]
	if "K" in c:
		return [True, "K"]
	if "Q" in c:
		return [True, "Q"]	
	if "J" in c:
		return [True, "J"]	
	return [True, max(c)] if c else False


Test.assert_equals(highest_pair(['A', 'A', 'K', 'K', '3']), [True, 'A'])
Test.assert_equals(highest_pair(['A', 'K', 'Q', 'J', '10']), False)
Test.assert_equals(highest_pair(['A', 'K', 'K', 'K', 'Q']), [True, 'K'])
Test.assert_equals(highest_pair(['A', '3', '3', '4', '4']), [True, '4'])
Test.assert_equals(highest_pair(['A', 'K', 'Q', 'Q', '5']), [True, 'Q'])    