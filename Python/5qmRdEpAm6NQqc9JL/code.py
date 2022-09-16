def hemisphere_season(hemisphere, date):
	...

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(hemisphere_season("N", "June, 30"), "Summer", "Example #1")
Test.assert_equals(hemisphere_season("N", "March, 1"), "Spring", "Example #2")
Test.assert_equals(hemisphere_season("S", "September, 22"), "Spring", "Example #3")
Test.assert_equals(hemisphere_season("S", "April, 20"), "Autumn")
Test.assert_equals(hemisphere_season("N", "November, 20"), "Autumn")
Test.assert_equals(hemisphere_season("S", "May, 8"), "Autumn")
Test.assert_equals(hemisphere_season("N", "February, 28"), "Winter")
Test.assert_equals(hemisphere_season("S", "August, 6"), "Winter")
Test.assert_equals(hemisphere_season("N", "July, 28"), "Summer")
Test.assert_equals(hemisphere_season("S", "October, 12"), "Spring")
Test.assert_equals(hemisphere_season("N", "December, 31"), "Winter")
Test.assert_equals(hemisphere_season("S", "January, 2"), "Summer")