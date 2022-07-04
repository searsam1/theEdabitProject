def palindrome_sieve(nums):
	

TestsConsoleTest.assert_equals(palindrome_sieve([443, 12, 639, 121, 3232]), [443, 121, 3232])

Test.assert_equals(palindrome_sieve([5, 55, 6655, 8787]), [5, 55, 6655, 8787])

Test.assert_equals(palindrome_sieve([897, 89, 23, 54, 6197, 53342]), [])

Test.assert_equals(palindrome_sieve([112, 334, 555, 656, 665, 444, 443, 7]), [112, 334, 555, 656, 665, 444, 443, 7])

Test.assert_equals(palindrome_sieve([1, 2, 123]), [1, 2])

Test.assert_equals(palindrome_sieve([1, 2, 3]), [1, 2, 3])

Test.assert_equals(palindrome_sieve([555, 687868877]), [555, 687868877])

Test.assert_equals(palindrome_sieve([555, 68786887]), [555, 68786887])