# G = 71 
# A = 65 



def musical_range(notes):
    # ex. notes = D4-C7
    start, stop = notes.split("-")
    res = [] 
    for j in range(10):
        for i in range(7):
            ele = chr(i + 65) + str(j)
            res.append(ele)
    idx_1, idx_2 = res.index(start), res.index(stop)
    res = res[idx_1:idx_2+1]
    return res


d = {
    "Piccolo" : musical_range("D4-C7"),
    "Tuba" : musical_range("D1-F4"),
    "Guitar": musical_range("E3-E6"),
    "Piano" : musical_range("A0-C8"),
    "Violin" : musical_range("G3-A7"),
    }

def instrument_range(instr, note):
	return note in d[instr]

# print(x)
# Test.assert_equals(instrument_range("Violin", "G6"), True)

# Test.assert_equals(instrument_range("Piano", "C8"), True)

# Test.assert_equals(instrument_range("Piano", "C9"), False)

# Test.assert_equals(instrument_range("Tuba", "C8"), False)

# Test.assert_equals(instrument_range("Guitar", "F4"), True)

# Test.assert_equals(instrument_range("Guitar", "C4"), True)

# Test.assert_equals(instrument_range("Piccolo", "F4"), True)

# Test.assert_equals(instrument_range("Tuba", "F6"), False)