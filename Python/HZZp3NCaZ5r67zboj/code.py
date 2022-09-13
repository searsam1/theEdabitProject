def instrument_range(instr, note):
	

TestsConsoleTest.assert_equals(instrument_range("Piccolo", "A3"), False)

Test.assert_equals(instrument_range("Violin", "G6"), True)

Test.assert_equals(instrument_range("Piano", "C8"), True)

Test.assert_equals(instrument_range("Piano", "C9"), False)

Test.assert_equals(instrument_range("Tuba", "C8"), False)

Test.assert_equals(instrument_range("Guitar", "F4"), True)

Test.assert_equals(instrument_range("Guitar", "C4"), True)

Test.assert_equals(instrument_range("Piccolo", "F4"), True)

Test.assert_equals(instrument_range("Tuba", "F6"), False)