def word_game(p1, p2):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(word_game(["edabit", "yellow", "growing"], ["tangy", "wedding", "ground"]), "Game continues...")
Test.assert_equals(word_game(["edabit", "yellow", "rowing"], ["tangy", "wedding", "ground"]), "Player 2 wins!")
Test.assert_equals(word_game(["edabit", "yellow", "growing"], ["tangy", "wedding", "round"]), "Player 1 wins!")
Test.assert_equals(word_game(["edabit", "yellow", "growing", "dart"], ["tangy", "wedding", "ground", "tangy"]), "Player 1 wins!")
Test.assert_equals(word_game(["edabit", "yellow", "growing", "dart", "tangy"], ["tangy", "wedding", "ground", "toast", "yellow"]), "Player 2 wins!")
Test.assert_equals(word_game(['banana',	'elephant',	'orange',	'elope',	'tiger',	'elipse',	'elevate',	'trust',	'time'], ['apple',	'tornado',	'ewe',	'event',	'rose',	'eradicate',	'eat',	'tonight',	'love']), "Player 1 wins!")