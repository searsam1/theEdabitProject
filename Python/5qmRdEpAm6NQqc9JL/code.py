
from datetime import datetime

d = {
    (3,4,5): {"start": "March", "end":  "May", "N": "Spring", "S": "Autumn"},
    (6,7,8): {"start": "June", "end":  "August", "N": "Summer", "S": "Winter"},
    (9,10,11): {"start": "September", "end":  "November", "N": "Autumn", "S": "Spring"},
    (12,1,2): {"start": "December", "end":  "February", "N": "Winter", "S": "Summer"}

}

def hemisphere_season(hemisphere, date):
    date = datetime.strptime(date.split(",")[0],"%B")
    
    for k in d:
        if date.month in k:
            res = d[k][hemisphere]
            return res


class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

TestsConsoleTest.assert_equals(hemisphere_season("N", "June, 30"), "Summer")
Test.assert_equals(hemisphere_season("N", "March, 1"), "Spring")
Test.assert_equals(hemisphere_season("S", "September, 22"), "Spring")
Test.assert_equals(hemisphere_season("S", "April, 20"), "Autumn")
Test.assert_equals(hemisphere_season("N", "November, 20"), "Autumn")
Test.assert_equals(hemisphere_season("S", "May, 8"), "Autumn")
Test.assert_equals(hemisphere_season("N", "February, 28"), "Winter")
Test.assert_equals(hemisphere_season("S", "August, 6"), "Winter")
Test.assert_equals(hemisphere_season("N", "July, 28"), "Summer")
Test.assert_equals(hemisphere_season("S", "October, 12"), "Spring")
Test.assert_equals(hemisphere_season("N", "December, 31"), "Winter")
Test.assert_equals(hemisphere_season("S", "January, 2"), "Summer")