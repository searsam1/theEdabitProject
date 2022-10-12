int profit(std::vector<float> prices, int inv){

}...

TestsConsoleDescribe(profit_tests){
	It(Test1){Assert::That(profit({32.67, 45.00}, 1200), Equals(14796));}
	It(Test2){Assert::That(profit({0.1, 0.18}, 259800), Equals(20784));}
	It(Test3){Assert::That(profit({185.00, 299.99}, 300), Equals(34497));}
	It(Test4){Assert::That(profit({378.11, 990.00}, 99), Equals(60577));}
	It(Test5){Assert::That(profit({4.67, 5.00}, 78000), Equals(25740));}
	It(Test6){Assert::That(profit({19.87, 110.00}, 350), Equals(31546));}
	It(Test7){Assert::That(profit({2.91, 4.50}, 6000), Equals(9540));}
	It(Test8){Assert::That(profit({68.01, 149.99}, 500), Equals(40990));}
	It(Test9){Assert::That(profit({1.45, 8.50}, 10000), Equals(70500));}
	It(Test10){Assert::That(profit({10780, 34999}, 10), Equals(242190));}
};