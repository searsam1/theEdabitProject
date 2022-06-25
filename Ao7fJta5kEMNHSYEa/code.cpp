#include <string>
using namespace std; 
string  fizzBuzz(int num){
	
}

TestsConsoleDescribe(FizzBuzz_test) {

	It(test1){Assert::That(fizzBuzz(3), Equals("Fizz"));}

	It(test2){Assert::That(fizzBuzz(5), Equals("Buzz"));}

	It(test3){Assert::That(fizzBuzz(15), Equals("FizzBuzz"));}

	It(test4){Assert::That(fizzBuzz(10), Equals("Buzz"));}

	It(test5){Assert::That(fizzBuzz(98), Equals("98"));}

};