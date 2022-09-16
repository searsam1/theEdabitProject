

def is_word_chain(words):
    res = 0 
    check_over = 0
    while len(words) > 1:
        first = words.pop(0)
        second = words[0]
        
        if len(first) != len(second):
            return False
        for idx, char in enumerate(first):
            other = second[idx]
            if other != char:
                check_over += 1
                if check_over > 1:
                    return False
        check_over = 0 
    return True








class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(is_word_chain(['meal', 'seal', 'seat', 'beat', 'beet']), True)
Test.assert_equals(is_word_chain(['red', 'bed', 'bet', 'bat', 'sat']), True)
Test.assert_equals(is_word_chain(['heady', 'ready', 'beady', 'beads', 'meads', 'meats', 'seats', 'feats']), True)
Test.assert_equals(is_word_chain(['score', 'scare', 'stare', 'spare', 'spire']), True)
Test.assert_equals(is_word_chain(['more', 'mire', 'dire', 'dare', 'date']), True)
Test.assert_equals(is_word_chain(['read', 'red', 'led', 'lad', 'lady']), False)
Test.assert_equals(is_word_chain(['red', 'bat', 'cat', 'sat']), False)
Test.assert_equals(is_word_chain(['candy', 'candies', 'fat', 'rat']), False)