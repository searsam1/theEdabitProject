
def firstlast(s):
    return [0, len(s) - 1]


def repeating(strings):
    offset = 0 
    res = []
    for string in strings:
        first, last = firstlast(string)
        first, last = first + offset, last + offset
        res.append([string[0], first, last, len(string)])
        offset += len(string)
    return res

def chunking(s):
    # s = "aaa"
    groups = []
    group = s[0]

    for c in s[1:]:
        if c in group:
            group += c
        elif c not in group:
            groups += [group]
            group = c
    groups.append(group)
    return groups


def find_repeating(txt):
    return repeating(chunking(txt)) if txt else []

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            



TestsConsoleTest.assert_equals(find_repeating(''), [])
# Test.assert_equals(find_repeating('a'), [['a', 0, 0, 1]])
# Test.assert_equals(find_repeating('1337'), [['1', 0, 0, 1], ['3', 1, 2, 2], ['7', 3, 3, 1]])
# Test.assert_equals(find_repeating('aabbb'), [['a', 0, 1, 2], ['b', 2, 4, 3]])
# Test.assert_equals(find_repeating('addressee'), [['a', 0, 0, 1], ['d', 1, 2, 2], ['r', 3, 3, 1], ['e', 4, 4, 1], ['s', 5, 6, 2], ['e', 7, 8, 2]])
# Test.assert_equals(find_repeating('aabbbaabbb'), [['a', 0, 1, 2], ['b', 2, 4, 3], ['a', 5, 6, 2], ['b', 7, 9, 3]])
# Test.assert_equals(find_repeating('1111222233334444'), [['1', 0, 3, 4], ['2', 4, 7, 4], ['3', 8, 11, 4], ['4', 12, 15, 4]])
# Test.assert_equals(find_repeating('1000000000000066600000000000001'), [['1', 0, 0, 1], ['0', 1, 13, 13], ['6', 14, 16, 3], ['0', 17, 29, 13], ['1', 30, 30, 1]])