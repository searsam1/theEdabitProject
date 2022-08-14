std::string dial(std::string str) {
	
}

TestsConsoleDescribe(dial_) {

	It(test1){Assert::That(dial("1-800-HOTLINEBLING"), Equals("1-800-468546325464"));}

	It(test2){Assert::That(dial("hello-world!"), Equals("43556-96753!"));}

	It(test3){Assert::That(dial("aaaabcccdefggg"), Equals("22222222333444"));}

	It(test4){Assert::That(dial("01023468adghijgkmz?"), Equals("010234682344454569?"));}

	It(test5){Assert::That(dial("SwApPeDcAsE"), Equals("79277332273"));}

	It(test6){Assert::That(dial("VAPORWAVE"), Equals("827679283"));}

};