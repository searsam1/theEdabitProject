int license(std::string me, int agents, std::string others){
  
}

TestsConsoleDescribe(license_){

It(test1){Assert::That(license("Zebediah", 1, "Bob Jim Becky Pat"), Equals(100));}

It(test2){Assert::That(license("Eric", 2, "Adam Caroline Rebecca Frank"), Equals(40));}

It(test3){Assert::That(license("Aaron", 3, "Jane Max Olivia Sam"), Equals(20));}

It(test4){Assert::That(license("Zebediah", 4, "Bob Jim Becky Pat"), Equals(40));}

It(test5){Assert::That(license("Zebediah", 5, "Bob Jim Becky Pat"), Equals(20));}

};