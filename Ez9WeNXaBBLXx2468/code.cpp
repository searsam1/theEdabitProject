std::string nSidedShape(int n) {
	
}

TestsConsoleDescribe(tests)

{

  It(test1){Assert::That(nSidedShape(1), Equals("circle"));}

	It(test2){Assert::That(nSidedShape(2), Equals("semi-circle"));}

	It(test3){Assert::That(nSidedShape(3), Equals("triangle"));}

	It(test4){Assert::That(nSidedShape(4), Equals("square"));}

	It(test5){Assert::That(nSidedShape(5), Equals("pentagon"));}

	It(test6){Assert::That(nSidedShape(6), Equals("hexagon"));}

	It(test7){Assert::That(nSidedShape(7), Equals("heptagon"));}

	It(test8){Assert::That(nSidedShape(8), Equals("octagon"));}

	It(test9){Assert::That(nSidedShape(9), Equals("nonagon"));}

	It(test10){Assert::That(nSidedShape(10), Equals("decagon"));}

};