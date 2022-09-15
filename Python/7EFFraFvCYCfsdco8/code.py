def decompose_address(txt):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(decompose_address("3315 Vanity St Beverly Hills, CA 90210"), ["3315", "Vanity St", "Beverly Hills", "CA", "90210"])
Test.assert_equals(decompose_address("557 Farmer Rd Corner, MT 59105"), ["557", "Farmer Rd", "Corner", "MT", "59105"])
Test.assert_equals(decompose_address("8919 Scarecrow Ct Idaho Falls, ID 80193"), ["8919", "Scarecrow Ct", "Idaho Falls", "ID", "80193"])
Test.assert_equals(decompose_address("91 Ronald Dr Stenton, MS 39073"), ["91", "Ronald Dr", "Stenton", "MS", "39073"])
Test.assert_equals(decompose_address("25000 Meek Pl Bozerman, MT 59104"), ["25000", "Meek Pl", "Bozerman", "MT", "59104"])