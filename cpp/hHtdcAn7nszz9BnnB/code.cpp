std::string mdFormat(std::string word, char style) {
	
}

TestsConsoleDescribe(mdFormat_){

It(test1){Assert::That(mdFormat("Bold", 'b'), Equals("**Bold**"));}

It(test2){Assert::That(mdFormat("Italics", 'i'), Equals("_Italics_"));}

It(test3){Assert::That(mdFormat("Code", 'c'), Equals("`Code`"));}

It(test4){Assert::That(mdFormat("Ruby", 's'), Equals("~~Ruby~~"));}

It(test5){Assert::That(mdFormat("JavaScript", 'b'), Equals("**JavaScript**"));}

It(test6){Assert::That(mdFormat("Python", 'i'), Equals("_Python_"));}

It(test7){Assert::That(mdFormat("C++", 'c'), Equals("`C++`"));}

It(test8){Assert::That(mdFormat("Strikethrough", 's'), Equals("~~Strikethrough~~"));}

};