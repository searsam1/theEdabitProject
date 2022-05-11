from anna_likes import anna_likes
import unittest

class Test(unittest.TestCase):
	
	checks = [] 
	def assert_equals(a,b,message=None,checks=checks):
		print(a,b,sep="  ->  ")
		checks.append(["Fail","Pass"][a==b])
		print("\t",checks,"\n")

Test.assert_equals(anna_likes("James"), False) ## Test 1
Test.assert_equals(anna_likes("John"), False) ## Test 2 
Test.assert_equals(anna_likes("Robert"), False) ## Test 3 
Test.assert_equals(anna_likes("Michael"), False) ## Test 4 
Test.assert_equals(anna_likes("William"), False) ## Test 5
Test.assert_equals(anna_likes("David"), False) ## Test 6 
Test.assert_equals(anna_likes("Richard"), False) ## Test 7 
Test.assert_equals(anna_likes("Joseph"), False) ## Test 8 
Test.assert_equals(anna_likes("Thomas"), False) ## Test 9 
Test.assert_equals(anna_likes("Charles"), False) ## Test 10 
Test.assert_equals(anna_likes("Christopher"), False) ## Test 11 
Test.assert_equals(anna_likes("Daniel"), True) ## Test 12 
Test.assert_equals(anna_likes("Matthew"), False) ## Test 13 
Test.assert_equals(anna_likes("Anthony"), False) ## Test 14 
Test.assert_equals(anna_likes("Donald"), False) ## Test 15 
Test.assert_equals(anna_likes("Mark"), False) ## Test 16 
Test.assert_equals(anna_likes("Paul"), True) ## Test 17 
Test.assert_equals(anna_likes("Steven"), False) ## Test 18 
Test.assert_equals(anna_likes("Andrew"), False) ## Test 19 
Test.assert_equals(anna_likes("Kenneth"), False) ## Test 20 
Test.assert_equals(anna_likes("Joshua"), True) ## Test 21 
Test.assert_equals(anna_likes("Kevin"), False) ## Test 22 
Test.assert_equals(anna_likes("Brian"), False) ## Test 23 
Test.assert_equals(anna_likes("George"), True) ## Test 24 
Test.assert_equals(anna_likes("Edward"), False) ## Test 25 
Test.assert_equals(anna_likes("Ronald"), False) ## Test 26 
Test.assert_equals(anna_likes("Timothy"), False) ## Test 27 
Test.assert_equals(anna_likes("Jason"), False) ## Test 28 
Test.assert_equals(anna_likes("Jeffrey"), False) ## Test 29 
Test.assert_equals(anna_likes("Ryan"), False) ## Test 30 
Test.assert_equals(anna_likes("Jacob"), False) ## Test 31 
Test.assert_equals(anna_likes("Gary"), False) ## Test 32 
Test.assert_equals(anna_likes("Nicholas"), False) ## Test 33 
Test.assert_equals(anna_likes("Eric"), True) ## Test 34 
Test.assert_equals(anna_likes("Jonathan"), False) ## Test 35 
Test.assert_equals(anna_likes("Stephen"), False) ## Test 36 
Test.assert_equals(anna_likes("Larry"), False) ## Test 37 
Test.assert_equals(anna_likes("Justin"), False) ## Test 38 
Test.assert_equals(anna_likes("Scott"), False) ## Test 39 
Test.assert_equals(anna_likes("Brandon"), False) ## Test 40 
Test.assert_equals(anna_likes("Benjamin"), False) ## Test 41 
Test.assert_equals(anna_likes("Samuel"), True) ## Test 42 
Test.assert_equals(anna_likes("Frank"), False) ## Test 43 
Test.assert_equals(anna_likes("Gregory"), False) ## Test 44 
Test.assert_equals(anna_likes("Raymond"), False) ## Test 45 
Test.assert_equals(anna_likes("Alexander"), False) ## Test 46 
Test.assert_equals(anna_likes("Patrick"), False) ## Test 47 
Test.assert_equals(anna_likes("Jack"), False) ## Test 48 
Test.assert_equals(anna_likes("Dennis"), False) ## Test 49 
Test.assert_equals(anna_likes("Jerry"), False) ## Test 50 
Test.assert_equals(anna_likes("Tyler"), False) ## Test 51 
Test.assert_equals(anna_likes("Aaron"), False) ## Test 52 
Test.assert_equals(anna_likes("Jose"), True) ## Test 53 
Test.assert_equals(anna_likes("Henry"), False) ## Test 54 
Test.assert_equals(anna_likes("Adam"), True) ## Test 55 
Test.assert_equals(anna_likes("Douglas"), False) ## Test 56 
Test.assert_equals(anna_likes("Nathan"), False) ## Test 57 
Test.assert_equals(anna_likes("Peter"), False) ## Test 58 
Test.assert_equals(anna_likes("Zachary"), False) ## Test 59 
Test.assert_equals(anna_likes("Kyle"), False) ## Test 60 
Test.assert_equals(anna_likes("Walter"), False) ## Test 61 
Test.assert_equals(anna_likes("Harold"), False) ## Test 62 
Test.assert_equals(anna_likes("Jeremy"), False) ## Test 63 
Test.assert_equals(anna_likes("Ethan"), False) ## Test 64 
Test.assert_equals(anna_likes("Carl"), False) ## Test 65 
Test.assert_equals(anna_likes("Keith"), False) ## Test 66 
Test.assert_equals(anna_likes("Roger"), False) ## Test 67 
Test.assert_equals(anna_likes("Gerald"), False) ## Test 68 
Test.assert_equals(anna_likes("Christian"), False) ## Test 69 
Test.assert_equals(anna_likes("Terry"), False) ## Test 70 
Test.assert_equals(anna_likes("Sean"), True) ## Test 71 
Test.assert_equals(anna_likes("Arthur"), False) ## Test 72 
Test.assert_equals(anna_likes("Austin"), True) ## Test 73 
Test.assert_equals(anna_likes("Noah"), True) ## Test 74 
Test.assert_equals(anna_likes("Lawrence"), False) ## Test 75 
Test.assert_equals(anna_likes("Jesse"), False) ## Test 76 
Test.assert_equals(anna_likes("Joe"), False) ## Test 77 
Test.assert_equals(anna_likes("Bryan"), False) ## Test 78 
Test.assert_equals(anna_likes("Billy"), False) ## Test 79 
Test.assert_equals(anna_likes("Jordan"), False) ## Test 80 
Test.assert_equals(anna_likes("Albert"), False) ## Test 81 
Test.assert_equals(anna_likes("Dylan"), False) ## Test 82 
Test.assert_equals(anna_likes("Bruce"), False) ## Test 83 
Test.assert_equals(anna_likes("Willie"), True) ## Test 84 
Test.assert_equals(anna_likes("Gabriel"), False) ## Test 85 
Test.assert_equals(anna_likes("Alan"), True) ## Test 86 
Test.assert_equals(anna_likes("Juan"), True) ## Test 87 
Test.assert_equals(anna_likes("Logan"), False) ## Test 88 
Test.assert_equals(anna_likes("Wayne"), False) ## Test 89 
Test.assert_equals(anna_likes("Ralph"), False) ## Test 90 
Test.assert_equals(anna_likes("Roy"), False) ## Test 91 
Test.assert_equals(anna_likes("Eugene"), False) ## Test 92 
Test.assert_equals(anna_likes("Randy"), False) ## Test 93 
Test.assert_equals(anna_likes("Vincent"), False) ## Test 94 
Test.assert_equals(anna_likes("Russell"), False) ## Test 95 
Test.assert_equals(anna_likes("Louis"), False) ## Test 96 
Test.assert_equals(anna_likes("Philip"), False) ## Test 97 
Test.assert_equals(anna_likes("Bobby"), False) ## Test 98 
Test.assert_equals(anna_likes("Johnny"), False) ## Test 99 
Test.assert_equals(anna_likes("Bradley"), False) ## Test 100
