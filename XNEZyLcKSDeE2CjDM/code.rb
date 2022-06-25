def fizz_buzz(num)
	
end

TestsConsoleTest.assert_equals(fizz_buzz(3), "Fizz", "You gave " + fizz_buzz(3) + " and Fizz was needed")

Test.assert_equals(fizz_buzz(5), "Buzz", "You gave " + fizz_buzz(5) + " and Buzz was needed")

Test.assert_equals(fizz_buzz(15), "FizzBuzz", "You gave " + fizz_buzz(15) + " and FizzBuzz was needed")

Test.assert_equals(fizz_buzz(10), "Buzz", "You gave " + fizz_buzz(10) + " and Buzz was needed")

Test.assert_equals(fizz_buzz(98), "98", "You gave " + fizz_buzz(98) + " and 98 was needed")