int yearsInOneHouse(int age, int moves) {
	
}

TestsConsoleDescribe(yearsInOneHouse_) {

	It(test1){Assert::That(yearsInOneHouse(30, 1), Equals(15));}

	It(test2){Assert::That(yearsInOneHouse(15, 2), Equals(5));}

	It(test3){Assert::That(yearsInOneHouse(80, 0), Equals(80));}

	It(test4){Assert::That(yearsInOneHouse(23, 2), Equals(8));}

	It(test5){Assert::That(yearsInOneHouse(31, 2), Equals(10));}

	It(test6){Assert::That(yearsInOneHouse(1, 0), Equals(1));}

};



// Author: Joshua Señoron