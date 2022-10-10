def special_reverse_string(txt):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(special_reverse_string('Edabit'), 'Tibade')
Test.assert_equals(special_reverse_string('UPPER lower'), 'REWOL reppu')
Test.assert_equals(special_reverse_string('1 23 456'), '6 54 321')
Test.assert_equals(special_reverse_string('Hello World!'), '!dlro Wolleh')
Test.assert_equals(special_reverse_string("Where's your dog Daisy?"), "?ysiadg odru oys 'erehw")
Test.assert_equals(special_reverse_string('addition(3, 2) = 5'), '5=)2,3(noit id d a')
Test.assert_equals(special_reverse_string("It's known that CSS means Cascading Style Sheets"), "Stee hsely tsgn IDA csacs Naemsscta Htnwo Nks'ti")