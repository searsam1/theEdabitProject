def word_game(p1, p2):
    z = list(zip(p1, p2))
    
    for i in z:
        if i[0][-1] != i[-1][0]:
            return "Player 1 wins!"
    for i in range(1,len(z)):
        e1, e2 = z[i-1], z[i]
        if e1[-1][-1] != e2[0][0]:
            return "Player 2 wins!"

    words = [] 
    for i in range(len(p1)):
        w1, w2 = p1[i], p2[i]

        if w1 in words:
            return "Player 2 wins!"
        else:
            words.append(w1)
        if w2 in words:
            return "Player 1 wins!"
        else:
            words.append(w2)
    return "Game continues..."

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