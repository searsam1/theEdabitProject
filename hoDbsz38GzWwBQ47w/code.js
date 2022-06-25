function FizzBuzz(num) {
	function FizzBuzz(num) {
		if (num % 15 == 0){
	  return "FizzBuzz";
	}
  	if (num % 5 == 0){
	  return "Buzz";
	}
  	if (num % 3 == 0){
	  return "Fizz";
	}
  	return num.toString();
}
}

TestsConsoleTest.assertEquals(FizzBuzz(3), "Fizz", "You gave " + FizzBuzz(3) + " and Fizz was needed")

Test.assertEquals(FizzBuzz(5), "Buzz", "You gave " + FizzBuzz(5) + " and Buzz was needed")

Test.assertEquals(FizzBuzz(15), "FizzBuzz", "You gave " + FizzBuzz(15) + " and FizzBuzz was needed")

Test.assertEquals(FizzBuzz(10), "Buzz", "You gave " + FizzBuzz(10) + " and Buzz was needed")

Test.assertEquals(FizzBuzz(98), "98", "You gave " + FizzBuzz(98) + " and 98 was needed")