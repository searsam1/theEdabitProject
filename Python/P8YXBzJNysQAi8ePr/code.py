
def digitaldrome(n):
    n = str(n)
    if len(set(n)) == 1:
        return "Repdrome"
    elif "".join(sorted(n)) == n:
        # Ascending 
        if len(set(n)) == len(n):
            return "Metadrome"
        else:
            return "Plaindrome"
    elif "".join(sorted(n, reverse=True)) == n:
        # Descending
        if len(set(n)) == len(n):
            return "Katadrome"
        else:
            return "Nialpdrome"
    return "Nondrome"

class Test:
    def assert_equals(a,b):
        try:
            assert a == b
        except AssertionError:
            print(f"{a}\n > should equal \n\t{b}")
TestsConsoleTest = Test            

Test.assert_equals(digitaldrome(33333), "Repdrome")
Test.assert_equals(digitaldrome(1), "Repdrome")
Test.assert_equals(digitaldrome(4899), "Plaindrome")
Test.assert_equals(digitaldrome(7521), "Katadrome")
Test.assert_equals(digitaldrome(23), "Metadrome")
Test.assert_equals(digitaldrome(2340), "Nondrome")
Test.assert_equals(digitaldrome(1000000), "Nialpdrome")
Test.assert_equals(digitaldrome(269), "Metadrome")