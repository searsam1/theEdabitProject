std::vector<std::string> makeBox(int n) {
	
}

TestsConsoleDescribe(make_box)

{

	It(T1){Assert::That(makeBox(5), Equals(std::vector<std::string>({

		"#####", 

		"#   #", 

		"#   #", 

		"#   #", 

		"#####"

	})));}

	It(T2){Assert::That(makeBox(6), Equals(std::vector<std::string>({

		"######", 

		"#    #", 

		"#    #", 

		"#    #", 

		"#    #", 

		"######"

	})));}

	It(T3){Assert::That(makeBox(4), Equals(std::vector<std::string>({

		"####", 

		"#  #", 

		"#  #", 

		"####"

	})));}

	It(T4){Assert::That(makeBox(2), Equals(std::vector<std::string>({

		"##", 

		"##"

	})));}

	It(T5){Assert::That(makeBox(1), Equals(std::vector<std::string>({

		"#"

	})));}

};