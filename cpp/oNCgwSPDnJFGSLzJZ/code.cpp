int findBob(std::vector<std::string> names) {
	
}

TestsConsoleDescribe(findBob_){

It(test1){Assert::That(findBob({"Jimmy", "Layla", "Mandy"}), Equals(-1));}

It(test2){Assert::That(findBob({"Bob", "Nathan", "Hayden"}), Equals(0));}

It(test3){Assert::That(findBob({"Paul", "Layla", "Bob"}), Equals(2));}

It(test4){Assert::That(findBob({"Garry", "Maria", "Bethany", "Bob", "Pauline"}), Equals(3));}

};